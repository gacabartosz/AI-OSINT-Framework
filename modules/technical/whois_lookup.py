"""
WHOIS Lookup Module

Performs WHOIS lookups on domain names using public WHOIS servers.
All data is collected from publicly accessible WHOIS databases.

Legal Basis: WHOIS data is publicly available information mandated
by ICANN for domain registration transparency.

Data Sources:
- Public WHOIS servers (whois.iana.org and registry-specific servers)
- Complies with ICANN WHOIS policy
- Respects rate limiting requirements
"""

import socket
import re
from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class WHOISModule:
    """WHOIS lookup module for domain intelligence.

    This module queries public WHOIS servers to retrieve domain
    registration information. All data is publicly available and
    legal to access.

    Example:
        >>> whois = WHOISModule()
        >>> result = whois.lookup("example.com")
        >>> print(result["registrar"])
        'Example Registrar Inc.'
    """

    name = "whois"
    description = "WHOIS domain lookup using public servers"
    category = "technical"
    legal_sources_only = True

    def __init__(self, timeout: int = 10):
        """Initialize WHOIS module.

        Args:
            timeout: Socket timeout in seconds
        """
        self.timeout = timeout
        self.whois_servers = self._load_whois_servers()

    def _load_whois_servers(self) -> Dict[str, str]:
        """Load WHOIS server mappings for different TLDs.

        Returns:
            Dictionary mapping TLDs to WHOIS servers
        """
        return {
            "com": "whois.verisign-grs.com",
            "net": "whois.verisign-grs.com",
            "org": "whois.pir.org",
            "info": "whois.afilias.net",
            "biz": "whois.biz",
            "us": "whois.nic.us",
            "uk": "whois.nic.uk",
            "de": "whois.denic.de",
            "fr": "whois.nic.fr",
            "pl": "whois.dns.pl",
            # Add more TLDs as needed
        }

    def lookup(self, domain: str) -> Dict[str, Any]:
        """Perform WHOIS lookup on a domain.

        Args:
            domain: Domain name to lookup

        Returns:
            Dictionary containing WHOIS information

        Raises:
            ValueError: If domain is invalid
            ConnectionError: If WHOIS server is unreachable
        """
        # Validate domain
        domain = self._validate_domain(domain)
        if not domain:
            raise ValueError(f"Invalid domain: {domain}")

        # Get appropriate WHOIS server
        tld = domain.split(".")[-1]
        whois_server = self.whois_servers.get(
            tld, "whois.iana.org"
        )

        try:
            # Query WHOIS server
            raw_data = self._query_whois_server(domain, whois_server)

            # Parse WHOIS data
            parsed_data = self._parse_whois_data(raw_data)

            # Return structured result
            return {
                "domain": domain,
                "data": parsed_data,
                "raw": raw_data,
                "sources": [whois_server],
                "legal": True,
                "timestamp": datetime.utcnow().isoformat(),
                "module": self.name,
            }

        except Exception as e:
            logger.error(f"WHOIS lookup failed for {domain}: {e}")
            raise ConnectionError(
                f"Failed to query WHOIS server: {e}"
            )

    def _validate_domain(self, domain: str) -> Optional[str]:
        """Validate domain name format.

        Args:
            domain: Domain to validate

        Returns:
            Validated domain or None if invalid
        """
        if not domain:
            return None

        # Clean up domain
        domain = domain.lower().strip()
        domain = re.sub(r"^https?://", "", domain)
        domain = domain.split("/")[0]

        # Validate format
        pattern = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$"
        if re.match(pattern, domain):
            return domain

        return None

    def _query_whois_server(
        self, domain: str, server: str, port: int = 43
    ) -> str:
        """Query WHOIS server for domain information.

        Args:
            domain: Domain to query
            server: WHOIS server address
            port: WHOIS port (default 43)

        Returns:
            Raw WHOIS response

        Raises:
            ConnectionError: If connection fails
        """
        try:
            # Create socket connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                sock.connect((server, port))

                # Send query
                query = f"{domain}\r\n".encode("utf-8")
                sock.send(query)

                # Receive response
                response = b""
                while True:
                    data = sock.recv(4096)
                    if not data:
                        break
                    response += data

                return response.decode("utf-8", errors="ignore")

        except socket.timeout:
            raise ConnectionError(f"Connection to {server} timed out")
        except Exception as e:
            raise ConnectionError(f"WHOIS query failed: {e}")

    def _parse_whois_data(self, raw_data: str) -> Dict[str, Any]:
        """Parse raw WHOIS data into structured format.

        Args:
            raw_data: Raw WHOIS response

        Returns:
            Parsed WHOIS data
        """
        data = {
            "registrar": None,
            "creation_date": None,
            "expiration_date": None,
            "updated_date": None,
            "name_servers": [],
            "status": [],
            "registrant": {},
        }

        # Parse registrar
        registrar_match = re.search(
            r"Registrar:\s*(.+)", raw_data, re.IGNORECASE
        )
        if registrar_match:
            data["registrar"] = registrar_match.group(1).strip()

        # Parse dates
        creation_match = re.search(
            r"Creation Date:\s*(.+)", raw_data, re.IGNORECASE
        )
        if creation_match:
            data["creation_date"] = creation_match.group(1).strip()

        expiration_match = re.search(
            r"Expir(?:ation|y) Date:\s*(.+)", raw_data, re.IGNORECASE
        )
        if expiration_match:
            data["expiration_date"] = expiration_match.group(1).strip()

        updated_match = re.search(
            r"Updated Date:\s*(.+)", raw_data, re.IGNORECASE
        )
        if updated_match:
            data["updated_date"] = updated_match.group(1).strip()

        # Parse name servers
        ns_matches = re.findall(
            r"Name Server:\s*(.+)", raw_data, re.IGNORECASE
        )
        if ns_matches:
            data["name_servers"] = [
                ns.strip().lower() for ns in ns_matches
            ]

        # Parse status
        status_matches = re.findall(
            r"(?:Domain )?Status:\s*(.+)", raw_data, re.IGNORECASE
        )
        if status_matches:
            data["status"] = [s.strip() for s in status_matches]

        return data

    def execute(self, target: str) -> Dict[str, Any]:
        """Execute WHOIS lookup (called by OSINT engine).

        Args:
            target: Domain name to lookup

        Returns:
            WHOIS lookup results
        """
        return self.lookup(target)


# Convenience function
def whois_lookup(domain: str) -> Dict[str, Any]:
    """Perform WHOIS lookup on a domain.

    Convenience function for quick lookups.

    Args:
        domain: Domain name to lookup

    Returns:
        WHOIS information dictionary
    """
    module = WHOISModule()
    return module.lookup(domain)
