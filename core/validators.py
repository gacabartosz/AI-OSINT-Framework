"""
Validators Module - Input and Source Validation

This module provides validators for ensuring legal compliance,
input sanitization, and data source verification.
"""

import re
from typing import List, Optional
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)


class SourceValidator:
    """Validates that data sources are legal and compliant.

    This validator checks:
    - Source is publicly accessible
    - No authentication bypass
    - Respects robots.txt
    - Complies with Terms of Service
    - No unauthorized access
    """

    def __init__(self):
        """Initialize the source validator."""
        self.approved_sources = self._load_approved_sources()
        self.blocked_sources = self._load_blocked_sources()

    def _load_approved_sources(self) -> List[str]:
        """Load list of pre-approved sources.

        Returns:
            List of approved source domains
        """
        return [
            "whois.domaintools.com",
            "api.github.com",
            "api.twitter.com",
            "newsapi.org",
            "archive.org",
            # Add more approved sources
        ]

    def _load_blocked_sources(self) -> List[str]:
        """Load list of blocked sources.

        Returns:
            List of blocked source domains
        """
        return [
            # Add sources that should never be used
        ]

    def validate(self, source: str) -> bool:
        """Validate that a source is legal to use.

        Args:
            source: URL or domain of the source

        Returns:
            True if source is legal, False otherwise
        """
        try:
            parsed = urlparse(source)
            domain = parsed.netloc or source

            # Check if blocked
            if domain in self.blocked_sources:
                logger.warning(f"Blocked source attempted: {domain}")
                return False

            # Check if approved
            if domain in self.approved_sources:
                return True

            # Additional validation logic
            return self._validate_public_access(source)

        except Exception as e:
            logger.error(f"Error validating source {source}: {e}")
            return False

    def _validate_public_access(self, source: str) -> bool:
        """Validate that source is publicly accessible.

        Args:
            source: The source to validate

        Returns:
            True if publicly accessible
        """
        # Placeholder - implement actual public access check
        # This would check robots.txt, require no auth, etc.
        return True

    def check_robots_txt(self, url: str) -> bool:
        """Check if robots.txt allows access.

        Args:
            url: URL to check

        Returns:
            True if allowed by robots.txt
        """
        # Placeholder for robots.txt checking
        return True


class InputValidator:
    """Validates and sanitizes user inputs.

    Prevents:
    - SQL injection
    - Command injection
    - XSS attacks
    - Path traversal
    - Invalid input formats
    """

    def __init__(self):
        """Initialize the input validator."""
        self.domain_pattern = re.compile(
            r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
            r"[a-zA-Z]{2,}$"
        )
        self.ip_pattern = re.compile(
            r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        )
        self.email_pattern = re.compile(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        )

    def validate(self, input_data: str) -> bool:
        """Validate general input.

        Args:
            input_data: The input to validate

        Returns:
            True if input is valid
        """
        if not input_data or len(input_data) > 1000:
            return False

        # Check for dangerous characters
        dangerous_chars = ["<", ">", ";", "&", "|", "`", "$"]
        if any(char in input_data for char in dangerous_chars):
            logger.warning(f"Dangerous characters in input: {input_data}")
            return False

        return True

    def validate_domain(self, domain: str) -> Optional[str]:
        """Validate and sanitize domain name.

        Args:
            domain: Domain name to validate

        Returns:
            Sanitized domain or None if invalid
        """
        if not domain:
            return None

        domain = domain.lower().strip()

        # Remove protocol if present
        domain = re.sub(r"^https?://", "", domain)

        # Remove path if present
        domain = domain.split("/")[0]

        if self.domain_pattern.match(domain):
            return domain

        logger.warning(f"Invalid domain format: {domain}")
        return None

    def validate_ip(self, ip: str) -> Optional[str]:
        """Validate IP address.

        Args:
            ip: IP address to validate

        Returns:
            Validated IP or None if invalid
        """
        if not ip:
            return None

        ip = ip.strip()

        if self.ip_pattern.match(ip):
            return ip

        logger.warning(f"Invalid IP format: {ip}")
        return None

    def validate_email(self, email: str) -> Optional[str]:
        """Validate email address.

        Args:
            email: Email address to validate

        Returns:
            Validated email or None if invalid
        """
        if not email:
            return None

        email = email.lower().strip()

        if self.email_pattern.match(email):
            return email

        logger.warning(f"Invalid email format: {email}")
        return None

    def sanitize(self, input_data: str) -> str:
        """Sanitize input by removing dangerous characters.

        Args:
            input_data: The input to sanitize

        Returns:
            Sanitized input string
        """
        if not input_data:
            return ""

        # Remove potentially dangerous characters
        sanitized = re.sub(r"[<>;&|`$]", "", input_data)

        # Limit length
        sanitized = sanitized[:1000]

        return sanitized.strip()

    def validate_query(self, query: str) -> bool:
        """Validate a search query.

        Args:
            query: Search query to validate

        Returns:
            True if query is valid
        """
        if not query or len(query) < 2 or len(query) > 500:
            return False

        # Check for SQL injection patterns
        sql_patterns = [
            r"(\bUNION\b.*\bSELECT\b)",
            r"(\bDROP\b.*\bTABLE\b)",
            r"(\bINSERT\b.*\bINTO\b)",
            r"(--)",
            r"(/\*.*\*/)",
        ]

        for pattern in sql_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                logger.warning(f"SQL injection attempt detected: {query}")
                return False

        return True


class ComplianceValidator:
    """Validates GDPR and CCPA compliance.

    Ensures:
    - No unauthorized PII collection
    - Proper data handling
    - Right to deletion support
    - Consent requirements
    """

    def __init__(self):
        """Initialize compliance validator."""
        self.pii_patterns = [
            r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
            r"\b\d{16}\b",  # Credit card
            r"\b\d{3}-\d{3}-\d{4}\b",  # Phone number
        ]

    def check_pii(self, data: str) -> bool:
        """Check if data contains PII.

        Args:
            data: Data to check

        Returns:
            True if PII detected
        """
        for pattern in self.pii_patterns:
            if re.search(pattern, data):
                return True
        return False

    def anonymize_pii(self, data: str) -> str:
        """Anonymize PII in data.

        Args:
            data: Data to anonymize

        Returns:
            Anonymized data
        """
        result = data

        # Replace SSN
        result = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "XXX-XX-XXXX", result)

        # Replace credit cards
        result = re.sub(r"\b\d{16}\b", "XXXX-XXXX-XXXX-XXXX", result)

        # Replace phone numbers
        result = re.sub(r"\b\d{3}-\d{3}-\d{4}\b", "XXX-XXX-XXXX", result)

        return result
