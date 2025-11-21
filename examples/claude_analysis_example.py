#!/usr/bin/env python3
"""
Claude AI Analysis Example

Demonstrates how to use Claude for OSINT analysis.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_tools.claude import ClaudeAnalyzer
from modules.technical.whois_lookup import WHOISModule


def main():
    print("=" * 60)
    print("Claude AI OSINT Analysis Example")
    print("=" * 60)
    print()

    # Get API key
    api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: Set CLAUDE_API_KEY or ANTHROPIC_API_KEY environment variable")
        print("\nExample:")
        print("  export CLAUDE_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize Claude analyzer
    analyzer = ClaudeAnalyzer(api_key=api_key)

    # Collect OSINT data
    print("🔍 Collecting OSINT data for example.com...")
    whois = WHOISModule()

    try:
        osint_data = whois.lookup("example.com")
    except Exception as e:
        print(f"❌ WHOIS lookup failed: {e}")
        sys.exit(1)

    print("✅ Data collected\n")

    # Analyze with Claude
    print("🤖 Analyzing with Claude AI...")
    print("-" * 60)

    analysis_prompt = """
    Analyze this WHOIS data and provide:
    1. Key findings about the domain
    2. Age and registration details
    3. Any notable patterns or observations
    4. Confidence level in the data

    Format as a professional intelligence brief.
    """

    result = analyzer.analyze_osint_data(
        data=osint_data, prompt=analysis_prompt
    )

    if result["success"]:
        print("\n📊 Claude Analysis:")
        print("=" * 60)
        print(result["analysis"])
        print("\n" + "=" * 60)
        print(f"\n📈 Token Usage:")
        print(f"   Input: {result['usage']['input_tokens']}")
        print(f"   Output: {result['usage']['output_tokens']}")
        print(f"   Model: {result['model']}")
    else:
        print(f"❌ Analysis failed: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
