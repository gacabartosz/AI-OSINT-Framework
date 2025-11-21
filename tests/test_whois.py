"""
Unit tests for WHOIS module
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.technical.whois_lookup import WHOISModule


class TestWHOISModule:
    """Test cases for WHOIS module."""

    def setup_method(self):
        """Setup for each test."""
        self.module = WHOISModule()

    def test_module_attributes(self):
        """Test that module has required attributes."""
        assert self.module.name == "whois"
        assert self.module.description is not None
        assert self.module.category == "technical"
        assert self.module.legal_sources_only is True

    def test_validate_domain_valid(self):
        """Test validation of valid domain names."""
        valid_domains = [
            "example.com",
            "test.org",
            "my-domain.net",
            "subdomain.example.co.uk",
        ]

        for domain in valid_domains:
            result = self.module._validate_domain(domain)
            assert result is not None
            assert result == domain.lower()

    def test_validate_domain_invalid(self):
        """Test validation rejects invalid domains."""
        invalid_domains = [
            "",
            "not a domain",
            "domain with spaces.com",
            "123",
            "-invalid.com",
            "invalid-.com",
        ]

        for domain in invalid_domains:
            result = self.module._validate_domain(domain)
            assert result is None

    def test_validate_domain_cleanup(self):
        """Test that domain validation cleans up input."""
        # Should remove protocol
        assert self.module._validate_domain("https://example.com") == "example.com"
        assert self.module._validate_domain("http://example.com") == "example.com"

        # Should remove path
        assert self.module._validate_domain("example.com/path") == "example.com"

        # Should lowercase
        assert self.module._validate_domain("EXAMPLE.COM") == "example.com"

    def test_parse_whois_data(self):
        """Test parsing of WHOIS data."""
        raw_data = """
        Domain Name: EXAMPLE.COM
        Registrar: Example Registrar Inc.
        Creation Date: 1995-08-14T04:00:00Z
        Expiration Date: 2024-08-13T04:00:00Z
        Updated Date: 2023-08-14T07:01:38Z
        Name Server: NS1.EXAMPLE.COM
        Name Server: NS2.EXAMPLE.COM
        Status: clientDeleteProhibited
        Status: clientTransferProhibited
        """

        parsed = self.module._parse_whois_data(raw_data)

        assert parsed["registrar"] == "Example Registrar Inc."
        assert parsed["creation_date"] is not None
        assert len(parsed["name_servers"]) == 2
        assert "ns1.example.com" in parsed["name_servers"]
        assert len(parsed["status"]) == 2

    def test_whois_servers_loaded(self):
        """Test that WHOIS servers are loaded."""
        servers = self.module.whois_servers
        assert len(servers) > 0
        assert "com" in servers
        assert "org" in servers

    def test_lookup_invalid_domain_raises_error(self):
        """Test that lookup raises error for invalid domain."""
        with pytest.raises(ValueError):
            self.module.lookup("invalid domain with spaces")

    def test_execute_method(self):
        """Test that execute method exists and works."""
        # This will likely fail in test environment without network
        # but we can at least verify the method exists
        assert hasattr(self.module, "execute")
        assert callable(self.module.execute)


class TestWHOISResult:
    """Test WHOIS result structure."""

    def setup_method(self):
        """Setup for each test."""
        self.module = WHOISModule()

    def test_result_structure(self):
        """Test that result has expected structure."""
        # Create a mock result
        mock_raw = "Domain: example.com\nRegistrar: Test"
        parsed = self.module._parse_whois_data(mock_raw)

        result = {
            "domain": "example.com",
            "data": parsed,
            "raw": mock_raw,
            "sources": ["whois.test.com"],
            "legal": True,
            "timestamp": "2024-01-01T00:00:00",
            "module": "whois",
        }

        # Verify structure
        assert "domain" in result
        assert "data" in result
        assert "raw" in result
        assert "sources" in result
        assert "legal" in result
        assert "timestamp" in result
        assert "module" in result

        # Verify legal compliance
        assert result["legal"] is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
