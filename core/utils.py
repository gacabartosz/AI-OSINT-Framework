"""
Utility Functions - Helper classes and functions

This module provides utility classes for logging, rate limiting,
caching, and other common operations.
"""

import logging
import time
from typing import Dict, Optional, Any
from datetime import datetime, timedelta
from collections import defaultdict
import hashlib
import json


class Logger:
    """Enhanced logger with OSINT-specific features.

    Provides structured logging with automatic PII redaction
    and audit trail capabilities.
    """

    def __init__(self, name: str, redact_pii: bool = True):
        """Initialize logger.

        Args:
            name: Logger name
            redact_pii: Whether to redact PII from logs
        """
        self.logger = logging.getLogger(name)
        self.redact_pii = redact_pii
        self._setup_logger()

    def _setup_logger(self) -> None:
        """Set up logger configuration."""
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def _redact_sensitive(self, message: str) -> str:
        """Redact sensitive information from log message.

        Args:
            message: Log message

        Returns:
            Redacted message
        """
        if not self.redact_pii:
            return message

        # Redact API keys
        import re

        message = re.sub(
            r"(api[_-]?key|token)[\s:=]+[\w-]+",
            r"\1=REDACTED",
            message,
            flags=re.IGNORECASE,
        )

        # Redact email addresses
        message = re.sub(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "EMAIL_REDACTED",
            message,
        )

        return message

    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(self._redact_sensitive(message))

    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(self._redact_sensitive(message))

    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(self._redact_sensitive(message))

    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(self._redact_sensitive(message))


class RateLimiter:
    """Rate limiter to prevent API abuse and ToS violations.

    Implements token bucket algorithm for rate limiting.
    """

    def __init__(
        self,
        requests_per_minute: int = 60,
        requests_per_hour: int = 1000,
    ):
        """Initialize rate limiter.

        Args:
            requests_per_minute: Max requests per minute
            requests_per_hour: Max requests per hour
        """
        self.requests_per_minute = requests_per_minute
        self.requests_per_hour = requests_per_hour
        self.minute_buckets: Dict[str, list] = defaultdict(list)
        self.hour_buckets: Dict[str, list] = defaultdict(list)

    def check_limit(self, identifier: str) -> bool:
        """Check if request is within rate limits.

        Args:
            identifier: Unique identifier (user, IP, target, etc.)

        Returns:
            True if within limits, False otherwise
        """
        now = time.time()

        # Clean old entries
        self._clean_buckets(identifier, now)

        # Check minute limit
        if len(self.minute_buckets[identifier]) >= self.requests_per_minute:
            return False

        # Check hour limit
        if len(self.hour_buckets[identifier]) >= self.requests_per_hour:
            return False

        # Add request
        self.minute_buckets[identifier].append(now)
        self.hour_buckets[identifier].append(now)

        return True

    def _clean_buckets(self, identifier: str, now: float) -> None:
        """Remove old entries from buckets.

        Args:
            identifier: Unique identifier
            now: Current timestamp
        """
        # Clean minute bucket (entries older than 60 seconds)
        self.minute_buckets[identifier] = [
            ts for ts in self.minute_buckets[identifier] if now - ts < 60
        ]

        # Clean hour bucket (entries older than 3600 seconds)
        self.hour_buckets[identifier] = [
            ts for ts in self.hour_buckets[identifier] if now - ts < 3600
        ]

    def get_remaining(self, identifier: str) -> Dict[str, int]:
        """Get remaining requests for identifier.

        Args:
            identifier: Unique identifier

        Returns:
            Dictionary with remaining requests per minute and hour
        """
        now = time.time()
        self._clean_buckets(identifier, now)

        return {
            "per_minute": self.requests_per_minute
            - len(self.minute_buckets[identifier]),
            "per_hour": self.requests_per_hour
            - len(self.hour_buckets[identifier]),
        }


class Cache:
    """Simple in-memory cache with TTL support.

    Used for caching OSINT results to reduce API calls
    and improve performance.
    """

    def __init__(self, default_ttl: int = 3600):
        """Initialize cache.

        Args:
            default_ttl: Default time-to-live in seconds
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found/expired
        """
        if key not in self.cache:
            return None

        entry = self.cache[key]
        if datetime.now() > entry["expires"]:
            del self.cache[key]
            return None

        return entry["value"]

    def set(
        self, key: str, value: Any, ttl: Optional[int] = None
    ) -> None:
        """Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (uses default if None)
        """
        ttl = ttl or self.default_ttl
        expires = datetime.now() + timedelta(seconds=ttl)

        self.cache[key] = {"value": value, "expires": expires}

    def delete(self, key: str) -> None:
        """Delete value from cache.

        Args:
            key: Cache key
        """
        if key in self.cache:
            del self.cache[key]

    def clear(self) -> None:
        """Clear all cached values."""
        self.cache.clear()

    def cleanup(self) -> None:
        """Remove expired entries from cache."""
        now = datetime.now()
        expired_keys = [
            key
            for key, entry in self.cache.items()
            if now > entry["expires"]
        ]

        for key in expired_keys:
            del self.cache[key]


class Hasher:
    """Utility for hashing data for anonymization and deduplication."""

    @staticmethod
    def hash_string(data: str, algorithm: str = "sha256") -> str:
        """Hash a string.

        Args:
            data: String to hash
            algorithm: Hash algorithm (md5, sha1, sha256)

        Returns:
            Hexadecimal hash string
        """
        if algorithm == "md5":
            return hashlib.md5(data.encode()).hexdigest()
        elif algorithm == "sha1":
            return hashlib.sha1(data.encode()).hexdigest()
        else:  # sha256
            return hashlib.sha256(data.encode()).hexdigest()

    @staticmethod
    def anonymize_identifier(identifier: str) -> str:
        """Create anonymized version of identifier.

        Args:
            identifier: Original identifier

        Returns:
            Anonymized hash
        """
        return Hasher.hash_string(identifier, "sha256")[:16]


class DataFormatter:
    """Format data for different output types."""

    @staticmethod
    def to_json(data: Any, pretty: bool = True) -> str:
        """Convert data to JSON.

        Args:
            data: Data to convert
            pretty: Whether to pretty-print

        Returns:
            JSON string
        """
        if pretty:
            return json.dumps(data, indent=2, default=str)
        return json.dumps(data, default=str)

    @staticmethod
    def to_csv(data: list, headers: Optional[list] = None) -> str:
        """Convert list of dicts to CSV.

        Args:
            data: List of dictionaries
            headers: Optional list of headers

        Returns:
            CSV string
        """
        import csv
        from io import StringIO

        if not data:
            return ""

        output = StringIO()
        headers = headers or list(data[0].keys())
        writer = csv.DictWriter(output, fieldnames=headers)

        writer.writeheader()
        writer.writerows(data)

        return output.getvalue()

    @staticmethod
    def to_markdown_table(data: list) -> str:
        """Convert list of dicts to Markdown table.

        Args:
            data: List of dictionaries

        Returns:
            Markdown table string
        """
        if not data:
            return ""

        headers = list(data[0].keys())

        # Header row
        table = "| " + " | ".join(headers) + " |\n"

        # Separator row
        table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

        # Data rows
        for row in data:
            table += (
                "| "
                + " | ".join(str(row.get(h, "")) for h in headers)
                + " |\n"
            )

        return table


class TimeUtils:
    """Time-related utility functions."""

    @staticmethod
    def get_timestamp() -> str:
        """Get current ISO 8601 timestamp.

        Returns:
            ISO 8601 formatted timestamp
        """
        return datetime.utcnow().isoformat() + "Z"

    @staticmethod
    def parse_timestamp(timestamp: str) -> datetime:
        """Parse ISO 8601 timestamp.

        Args:
            timestamp: ISO 8601 timestamp string

        Returns:
            datetime object
        """
        return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    @staticmethod
    def time_ago(timestamp: str) -> str:
        """Get human-readable time ago string.

        Args:
            timestamp: ISO 8601 timestamp

        Returns:
            Human-readable string like "2 hours ago"
        """
        dt = TimeUtils.parse_timestamp(timestamp)
        now = datetime.now(dt.tzinfo)
        diff = now - dt

        seconds = diff.total_seconds()

        if seconds < 60:
            return f"{int(seconds)} seconds ago"
        elif seconds < 3600:
            return f"{int(seconds / 60)} minutes ago"
        elif seconds < 86400:
            return f"{int(seconds / 3600)} hours ago"
        else:
            return f"{int(seconds / 86400)} days ago"
