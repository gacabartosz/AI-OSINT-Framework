"""
DNS Lookup Module

Performs DNS queries to gather domain intelligence.
All queries use public DNS resolvers and comply with DNS standards.
"""

import socket
from typing import Dict, Any, List
from datetime import datetime
import logging

try:
    import dns.resolver
    import dns.reversename
except ImportError:
    dns = None

logger = logging.getLogger(__name__)


class DNSModule:
    """DNS lookup module for technical OSINT.

    Queries:
    - A records (IPv4 addresses)
    - AAAA records (IPv6 addresses)
    - MX records (mail servers)
    - NS records (nameservers)
    - TXT records (metadata, SPF, DKIM)
    - CNAME records (aliases)
    - Reverse DNS (PTR records)
    """

    name = "dns"
    description = "DNS lookup using public resolvers"
    category = "technical"
    legal_sources_only = True

    def __init__(self, nameserver: str = "8.8.8.8"):
        """Initialize DNS module.

        Args:
            nameserver: DNS resolver to use (default: Google DNS)
        """
        if dns is None:
            raise ImportError(
                "dnspython not installed. Install with: pip install dnspython"
            )

        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [nameserver]

    def lookup(self, domain: str) -> Dict[str, Any]:
        """Perform comprehensive DNS lookup.

        Args:
            domain: Domain name to query

        Returns:
            DNS records for domain
        """
        results = {
            "domain": domain,
            "records": {},
            "legal": True,
            "timestamp": datetime.utcnow().isoformat(),
            "module": self.name,
        }

        # Query all record types
        record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

        for rtype in record_types:
            try:
                answers = self.resolver.resolve(domain, rtype)
                results["records"][rtype] = [
                    str(rdata) for rdata in answers
                ]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                results["records"][rtype] = []
            except Exception as e:
                logger.error(f"DNS query failed for {rtype}: {e}")
                results["records"][rtype] = []

        return results

    def reverse_lookup(self, ip: str) -> Dict[str, Any]:
        """Perform reverse DNS lookup.

        Args:
            ip: IP address to query

        Returns:
            PTR record (hostname)
        """
        try:
            rev_name = dns.reversename.from_address(ip)
            answers = self.resolver.resolve(rev_name, "PTR")
            hostnames = [str(rdata) for rdata in answers]

            return {
                "ip": ip,
                "hostnames": hostnames,
                "legal": True,
                "timestamp": datetime.utcnow().isoformat(),
            }

        except Exception as e:
            logger.error(f"Reverse DNS failed for {ip}: {e}")
            return {
                "ip": ip,
                "hostnames": [],
                "error": str(e),
                "legal": True,
                "timestamp": datetime.utcnow().isoformat(),
            }

    def execute(self, target: str) -> Dict[str, Any]:
        """Execute DNS lookup (called by OSINT engine)."""
        return self.lookup(target)
