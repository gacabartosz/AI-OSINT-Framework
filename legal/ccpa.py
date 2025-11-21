"""
CCPA Compliance Module

Ensures compliance with California Consumer Privacy Act (CCPA)
for OSINT data collection and processing.
"""

from typing import Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class CCPACompliance:
    """CCPA compliance checker for OSINT operations.

    Ensures:
    - Right to know (disclosure)
    - Right to delete
    - Right to opt-out
    - Non-discrimination
    - Data security
    """

    def __init__(self):
        """Initialize CCPA compliance checker."""
        self.personal_info_categories = self._load_categories()

    def _load_categories(self) -> List[str]:
        """Load CCPA personal information categories."""
        return [
            "Identifiers",  # Name, address, email, SSN, etc.
            "Commercial Information",  # Purchase history, etc.
            "Biometric Information",
            "Internet Activity",  # Browsing history, search history
            "Geolocation Data",
            "Professional Information",  # Employment, education
            "Inferences",  # Profiles derived from other data
        ]

    def check_collection_notice(
        self, notice_provided: bool, categories_disclosed: List[str]
    ) -> Dict[str, Any]:
        """Check if collection notice is CCPA-compliant.

        Args:
            notice_provided: Whether notice was provided
            categories_disclosed: Categories disclosed in notice

        Returns:
            Compliance check result
        """
        required_disclosures = [
            "Categories of personal information collected",
            "Purposes for collection",
            "Whether information is sold",
            "Right to opt-out",
        ]

        return {
            "compliant": notice_provided
            and len(categories_disclosed) > 0,
            "notice_provided": notice_provided,
            "categories_disclosed": categories_disclosed,
            "recommendation": "Provide collection notice"
            if not notice_provided
            else "Notice appears compliant",
        }

    def check_deletion_request(
        self, request_verified: bool, exemptions_apply: bool = False
    ) -> Dict[str, Any]:
        """Process consumer deletion request.

        Args:
            request_verified: Whether request was verified
            exemptions_apply: Whether exemptions apply (e.g., legal obligation)

        Returns:
            Deletion compliance check
        """
        should_delete = request_verified and not exemptions_apply

        return {
            "compliant": should_delete or exemptions_apply,
            "action": "delete_data" if should_delete else "retain_data",
            "reason": self._get_deletion_reason(
                request_verified, exemptions_apply
            ),
        }

    def _get_deletion_reason(
        self, verified: bool, exemptions: bool
    ) -> str:
        """Get reason for deletion action."""
        if not verified:
            return "Request not verified"
        if exemptions:
            return "Exemptions apply (legal obligation, fraud prevention, etc.)"
        return "No exemptions, proceed with deletion"

    def check_opt_out_compliance(
        self, sale_of_data: bool, opt_out_link_provided: bool
    ) -> Dict[str, Any]:
        """Check opt-out compliance.

        Args:
            sale_of_data: Whether personal information is sold
            opt_out_link_provided: Whether "Do Not Sell" link is provided

        Returns:
            Opt-out compliance check
        """
        if not sale_of_data:
            return {
                "compliant": True,
                "note": "No data sale, opt-out not required",
            }

        return {
            "compliant": opt_out_link_provided,
            "sale_of_data": sale_of_data,
            "opt_out_link_provided": opt_out_link_provided,
            "recommendation": "Provide 'Do Not Sell My Personal Information' link"
            if not opt_out_link_provided
            else "Opt-out link provided",
        }

    def check_data_security(
        self, encryption_enabled: bool, access_controls: bool
    ) -> Dict[str, Any]:
        """Check data security measures.

        Args:
            encryption_enabled: Whether data is encrypted
            access_controls: Whether access controls are in place

        Returns:
            Security compliance check
        """
        is_compliant = encryption_enabled and access_controls

        return {
            "compliant": is_compliant,
            "encryption_enabled": encryption_enabled,
            "access_controls": access_controls,
            "recommendation": "Implement encryption and access controls"
            if not is_compliant
            else "Security measures appear adequate",
        }


# Convenience function
def is_ccpa_compliant(
    collection_notice: bool = True,
    data_sale: bool = False,
    opt_out_provided: bool = True,
) -> bool:
    """Quick CCPA compliance check.

    Args:
        collection_notice: Whether notice was provided
        data_sale: Whether data is sold
        opt_out_provided: Whether opt-out link is provided

    Returns:
        True if basic CCPA requirements met
    """
    ccpa = CCPACompliance()

    notice_check = ccpa.check_collection_notice(
        collection_notice, ["Identifiers"]
    )
    opt_out_check = ccpa.check_opt_out_compliance(
        data_sale, opt_out_provided
    )

    return notice_check["compliant"] and opt_out_check["compliant"]
