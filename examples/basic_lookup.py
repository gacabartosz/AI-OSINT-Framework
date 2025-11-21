#!/usr/bin/env python3
"""
Basic OSINT Lookup Example

This example demonstrates how to perform a basic WHOIS lookup
using the AI-OSINT-Framework.
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.technical.whois_lookup import WHOISModule
from core.utils import DataFormatter


def main():
    """Run basic WHOIS lookup example."""
    print("=" * 60)
    print("AI-OSINT-Framework - Basic WHOIS Lookup Example")
    print("=" * 60)
    print()

    # Initialize WHOIS module
    whois = WHOISModule()

    # Domain to lookup
    domain = "example.com"
    print(f"Looking up domain: {domain}")
    print("-" * 60)
    print()

    try:
        # Perform lookup
        result = whois.lookup(domain)

        # Display results
        print("✅ Lookup successful!")
        print()
        print("Domain Information:")
        print("-" * 60)

        data = result["data"]

        if data.get("registrar"):
            print(f"Registrar: {data['registrar']}")

        if data.get("creation_date"):
            print(f"Created: {data['creation_date']}")

        if data.get("expiration_date"):
            print(f"Expires: {data['expiration_date']}")

        if data.get("name_servers"):
            print(f"\nName Servers:")
            for ns in data["name_servers"]:
                print(f"  - {ns}")

        if data.get("status"):
            print(f"\nStatus:")
            for status in data["status"]:
                print(f"  - {status}")

        print()
        print("-" * 60)
        print(f"Legal Compliance: {'✅ PASSED' if result['legal'] else '❌ FAILED'}")
        print(f"Timestamp: {result['timestamp']}")
        print()

        # Optionally save to JSON file
        save = input("Save results to JSON file? (y/n): ").strip().lower()
        if save == "y":
            import json

            filename = f"{domain.replace('.', '_')}_whois.json"
            with open(filename, "w") as f:
                json.dump(result, f, indent=2)
            print(f"✅ Results saved to {filename}")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
