"""
OSINT Engine - Core Processing System

This module contains the main OSINT engine that orchestrates
data collection, validation, and analysis across all modules.
"""

from typing import Dict, List, Optional, Any
import logging
from datetime import datetime
import json

from .validators import SourceValidator, InputValidator
from .utils import Logger, RateLimiter

logger = logging.getLogger(__name__)


class OSINTResult:
    """Container for OSINT query results.

    Attributes:
        data: The collected data
        sources: List of data sources used
        timestamp: When the data was collected
        legal_compliance: Whether all sources were legal
        compliance_score: Percentage of legal sources (0-100)
        metadata: Additional metadata about the query
    """

    def __init__(
        self,
        data: Dict[str, Any],
        sources: List[str],
        legal_compliance: bool = True,
        metadata: Optional[Dict] = None,
    ):
        self.data = data
        self.sources = sources
        self.timestamp = datetime.utcnow().isoformat()
        self.legal_compliance = legal_compliance
        self.compliance_score = 100 if legal_compliance else 0
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary.

        Returns:
            Dictionary representation of the result
        """
        return {
            "data": self.data,
            "sources": self.sources,
            "timestamp": self.timestamp,
            "legal_compliance": self.legal_compliance,
            "compliance_score": self.compliance_score,
            "metadata": self.metadata,
        }

    def to_json(self) -> str:
        """Convert result to JSON string.

        Returns:
            JSON string representation
        """
        return json.dumps(self.to_dict(), indent=2)


class OSINTEngine:
    """Main OSINT Engine for orchestrating data collection.

    The engine manages multiple OSINT modules, ensures legal compliance,
    handles rate limiting, and coordinates AI analysis when requested.

    Example:
        >>> engine = OSINTEngine()
        >>> result = engine.gather(
        ...     target="example.com",
        ...     modules=["whois", "dns"],
        ...     ai_analysis=True
        ... )
        >>> print(result.compliance_score)
        100
    """

    def __init__(self, config: Optional[Dict] = None):
        """Initialize the OSINT engine.

        Args:
            config: Optional configuration dictionary

        Raises:
            ValueError: If configuration is invalid
        """
        self.config = config or {}
        self.validator = SourceValidator()
        self.input_validator = InputValidator()
        self.rate_limiter = RateLimiter()
        self.modules = {}
        self.logger = Logger(__name__)

        self.logger.info("OSINT Engine initialized")

    def register_module(self, name: str, module: Any) -> None:
        """Register an OSINT module with the engine.

        Args:
            name: Unique name for the module
            module: The module instance

        Raises:
            ValueError: If module name already exists
        """
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered")

        self.modules[name] = module
        self.logger.info(f"Registered module: {name}")

    def gather(
        self,
        target: str,
        modules: List[str],
        ai_analysis: bool = False,
        ai_provider: str = "claude",
    ) -> OSINTResult:
        """Gather intelligence from multiple sources.

        Args:
            target: The target to investigate (domain, person, etc.)
            modules: List of module names to use
            ai_analysis: Whether to perform AI analysis
            ai_provider: AI provider to use (claude, openai, perplexity)

        Returns:
            OSINTResult containing collected data and metadata

        Raises:
            ValueError: If target is invalid or modules not found
            ComplianceError: If legal requirements not met
        """
        # Validate input
        if not self.input_validator.validate(target):
            raise ValueError(f"Invalid target: {target}")

        # Check rate limiting
        if not self.rate_limiter.check_limit(target):
            raise RuntimeError("Rate limit exceeded")

        # Collect data from each module
        results = {}
        sources_used = []
        all_legal = True

        for module_name in modules:
            if module_name not in self.modules:
                self.logger.warning(f"Module not found: {module_name}")
                continue

            try:
                module = self.modules[module_name]
                module_result = module.execute(target)

                # Validate legal compliance
                if not module_result.get("legal", False):
                    all_legal = False
                    self.logger.warning(
                        f"Module {module_name} returned non-legal data"
                    )
                    continue

                results[module_name] = module_result
                sources_used.extend(module_result.get("sources", []))

            except Exception as e:
                self.logger.error(f"Error in module {module_name}: {e}")
                continue

        # Perform AI analysis if requested
        if ai_analysis and results:
            ai_summary = self._perform_ai_analysis(
                results, ai_provider
            )
            results["ai_analysis"] = ai_summary

        # Create and return result
        return OSINTResult(
            data=results,
            sources=sources_used,
            legal_compliance=all_legal,
            metadata={
                "target": target,
                "modules_used": modules,
                "ai_provider": ai_provider if ai_analysis else None,
            },
        )

    def _perform_ai_analysis(
        self, data: Dict, provider: str
    ) -> Dict[str, Any]:
        """Perform AI analysis on collected data.

        Args:
            data: Collected OSINT data
            provider: AI provider to use

        Returns:
            AI analysis results
        """
        # Placeholder for AI integration
        # This will be implemented in ai_tools modules
        return {
            "summary": "AI analysis pending implementation",
            "provider": provider,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def get_available_modules(self) -> List[str]:
        """Get list of available module names.

        Returns:
            List of registered module names
        """
        return list(self.modules.keys())

    def get_module_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific module.

        Args:
            name: Module name

        Returns:
            Module information dictionary or None if not found
        """
        if name not in self.modules:
            return None

        module = self.modules[name]
        return {
            "name": name,
            "description": getattr(module, "description", "No description"),
            "category": getattr(module, "category", "uncategorized"),
            "legal_only": getattr(module, "legal_sources_only", False),
        }


class ComplianceError(Exception):
    """Raised when a legal compliance requirement is violated."""

    pass
