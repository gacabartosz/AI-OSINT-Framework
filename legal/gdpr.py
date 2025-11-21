"""
GDPR Compliance Module

Ensures compliance with EU General Data Protection Regulation (GDPR)
for OSINT data collection and processing.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
import re
import logging

logger = logging.getLogger(__name__)


class LegalBasis(Enum):
    """GDPR legal basis for processing personal data."""

    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTERESTS = "vital_interests"
    PUBLIC_TASK = "public_task"
    LEGITIMATE_INTEREST = "legitimate_interest"


class GDPRCompliance:
    """GDPR compliance checker for OSINT operations.

    Validates that OSINT data collection complies with GDPR requirements:
    - Legal basis for processing
    - Purpose limitation
    - Data minimization
    - Storage limitation
    - Data subject rights
    """

    def __init__(self):
        """Initialize GDPR compliance checker."""
        self.sensitive_patterns = self._load_sensitive_patterns()

    def _load_sensitive_patterns(self) -> Dict[str, str]:
        """Load regex patterns for sensitive personal data."""
        return {
            "ssn": r"\b\d{3}-\d{2}-\d{4}\b",  # US SSN
            "credit_card": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
            "passport": r"\b[A-Z]{1,2}\d{6,9}\b",
        }

    def check_legal_basis(
        self, data_type: str, purpose: str, legal_basis: LegalBasis
    ) -> Dict[str, Any]:
        """Verify legal basis for processing personal data.

        Args:
            data_type: Type of data being collected
            purpose: Purpose of data collection
            legal_basis: Legal basis claimed

        Returns:
            Validation result with compliance status
        """
        is_valid = self._validate_legal_basis(
            data_type, purpose, legal_basis
        )

        return {
            "compliant": is_valid,
            "data_type": data_type,
            "purpose": purpose,
            "legal_basis": legal_basis.value,
            "recommendation": self._get_recommendation(
                is_valid, legal_basis
            ),
        }

    def _validate_legal_basis(
        self, data_type: str, purpose: str, legal_basis: LegalBasis
    ) -> bool:
        """Validate if legal basis is appropriate."""
        # For OSINT, typically legitimate interest or public interest
        valid_bases = [
            LegalBasis.LEGITIMATE_INTEREST,
            LegalBasis.PUBLIC_TASK,
        ]

        # Consent rarely appropriate for OSINT (can't get it)
        if legal_basis == LegalBasis.CONSENT:
            logger.warning(
                "Consent not appropriate for OSINT investigations"
            )
            return False

        return legal_basis in valid_bases

    def _get_recommendation(
        self, is_valid: bool, legal_basis: LegalBasis
    ) -> str:
        """Get compliance recommendation."""
        if not is_valid:
            return (
                "Invalid legal basis for OSINT. Use 'legitimate_interest' "
                "for business due diligence or 'public_task' for "
                "law enforcement/journalistic purposes."
            )
        return "Legal basis is appropriate for OSINT purposes."

    def check_data_minimization(
        self, collected_fields: List[str], required_fields: List[str]
    ) -> Dict[str, Any]:
        """Check if data collection is minimized.

        Args:
            collected_fields: Fields actually collected
            required_fields: Fields necessary for purpose

        Returns:
            Compliance check result
        """
        excessive_fields = set(collected_fields) - set(required_fields)

        return {
            "compliant": len(excessive_fields) == 0,
            "collected_fields": len(collected_fields),
            "required_fields": len(required_fields),
            "excessive_fields": list(excessive_fields),
            "recommendation": "Remove excessive fields to comply with data minimization"
            if excessive_fields
            else "Data collection is minimized",
        }

    def check_sensitive_data(self, text: str) -> Dict[str, Any]:
        """Detect sensitive personal data in text.

        Args:
            text: Text to scan

        Returns:
            Detection results with types found
        """
        detected = {}

        for data_type, pattern in self.sensitive_patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                detected[data_type] = len(matches)

        return {
            "has_sensitive_data": len(detected) > 0,
            "detected_types": list(detected.keys()),
            "counts": detected,
            "recommendation": "Anonymize or delete sensitive data"
            if detected
            else "No sensitive data detected",
        }

    def anonymize_text(self, text: str) -> str:
        """Anonymize sensitive data in text.

        Args:
            text: Text to anonymize

        Returns:
            Anonymized text
        """
        anonymized = text

        replacements = {
            "ssn": "XXX-XX-XXXX",
            "credit_card": "XXXX-XXXX-XXXX-XXXX",
            "email": "[EMAIL REDACTED]",
            "phone": "XXX-XXX-XXXX",
            "passport": "[PASSPORT REDACTED]",
        }

        for data_type, pattern in self.sensitive_patterns.items():
            anonymized = re.sub(
                pattern, replacements[data_type], anonymized
            )

        return anonymized

    def check_retention_period(
        self, data_age_days: int, max_retention_days: int = 365
    ) -> Dict[str, Any]:
        """Check if data retention period is compliant.

        Args:
            data_age_days: Age of data in days
            max_retention_days: Maximum allowed retention

        Returns:
            Retention compliance check
        """
        is_compliant = data_age_days <= max_retention_days

        return {
            "compliant": is_compliant,
            "data_age_days": data_age_days,
            "max_retention_days": max_retention_days,
            "days_remaining": max_retention_days - data_age_days
            if is_compliant
            else 0,
            "recommendation": "Data should be deleted"
            if not is_compliant
            else f"Data can be retained for {max_retention_days - data_age_days} more days",
        }


# Convenience function
def is_gdpr_compliant(
    data_type: str,
    purpose: str,
    legal_basis: str = "legitimate_interest",
) -> bool:
    """Quick GDPR compliance check.

    Args:
        data_type: Type of data
        purpose: Purpose of collection
        legal_basis: Legal basis for processing

    Returns:
        True if compliant
    """
    gdpr = GDPRCompliance()
    basis = LegalBasis(legal_basis)
    result = gdpr.check_legal_basis(data_type, purpose, basis)
    return result["compliant"]
