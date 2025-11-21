#!/usr/bin/env python3
"""
Advanced OSINT Analysis Example

This example demonstrates how to use the OSINT engine with
multiple modules and AI analysis capabilities.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.engine import OSINTEngine
from modules.technical.whois_lookup import WHOISModule


def main():
    """Run advanced OSINT analysis."""
    print("=" * 60)
    print("AI-OSINT-Framework - Advanced Analysis Example")
    print("=" * 60)
    print()

    # Initialize OSINT Engine
    engine = OSINTEngine()

    # Register modules
    engine.register_module("whois", WHOISModule())

    # Show available modules
    print("Available modules:")
    for module_name in engine.get_available_modules():
        info = engine.get_module_info(module_name)
        print(f"  - {module_name}: {info['description']}")
    print()

    # Target domain
    target = input("Enter domain to analyze (or press Enter for 'example.com'): ").strip()
    if not target:
        target = "example.com"

    print(f"\nAnalyzing: {target}")
    print("-" * 60)
    print()

    try:
        # Gather intelligence
        print("🔍 Gathering intelligence...")
        result = engine.gather(
            target=target,
            modules=["whois"],
            ai_analysis=False,  # Set to True when AI integration is complete
        )

        # Display results
        print("✅ Analysis complete!")
        print()
        print("Results Summary:")
        print("-" * 60)

        # WHOIS data
        if "whois" in result.data:
            whois_data = result.data["whois"]["data"]
            print("\nWHOIS Information:")
            print(f"  Registrar: {whois_data.get('registrar', 'N/A')}")
            print(f"  Created: {whois_data.get('creation_date', 'N/A')}")
            print(f"  Expires: {whois_data.get('expiration_date', 'N/A')}")

            if whois_data.get("name_servers"):
                print(f"  Name Servers: {len(whois_data['name_servers'])} found")

        print()
        print("-" * 60)
        print(f"Compliance Score: {result.compliance_score}%")
        print(f"Legal Compliance: {'✅ PASSED' if result.legal_compliance else '❌ FAILED'}")
        print(f"Sources Used: {len(result.sources)}")
        print()

        # Display full JSON
        view_json = input("View full JSON output? (y/n): ").strip().lower()
        if view_json == "y":
            print("\nFull JSON Output:")
            print("=" * 60)
            print(result.to_json())

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
