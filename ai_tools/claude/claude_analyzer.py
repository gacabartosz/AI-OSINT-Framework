"""
Claude OSINT Analyzer

Integrates Anthropic's Claude API for OSINT analysis and synthesis.
Optimized for intelligence analysis, report generation, and pattern detection.
"""

from typing import Dict, Any, List, Optional
import logging
from datetime import datetime
import json

try:
    import anthropic
except ImportError:
    anthropic = None

logger = logging.getLogger(__name__)


class ClaudeAnalyzer:
    """Claude-powered OSINT analysis engine.

    Uses Claude's advanced reasoning capabilities for:
    - Synthesizing intelligence from multiple sources
    - Identifying patterns and connections
    - Risk assessment and scoring
    - Report generation
    - Fact-checking and validation

    Example:
        >>> analyzer = ClaudeAnalyzer(api_key="your-key")
        >>> result = analyzer.analyze_osint_data(
        ...     data=collected_intelligence,
        ...     prompt="Assess business risk"
        ... )
        >>> print(result["analysis"])
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        max_tokens: int = 4096,
        temperature: float = 0.7,
    ):
        """Initialize Claude analyzer.

        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
            model: Claude model to use
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0.0-1.0)

        Raises:
            ImportError: If anthropic package not installed
            ValueError: If API key not provided
        """
        if anthropic is None:
            raise ImportError(
                "anthropic package not installed. "
                "Install with: pip install anthropic"
            )

        if not api_key:
            raise ValueError(
                "API key required. Set ANTHROPIC_API_KEY environment "
                "variable or pass api_key parameter."
            )

        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

        logger.info(f"Initialized Claude analyzer with model {model}")

    def analyze_osint_data(
        self,
        data: Dict[str, Any],
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Analyze OSINT data using Claude.

        Args:
            data: OSINT data to analyze (from OSINT engine)
            prompt: Analysis question/prompt
            system_prompt: Optional system prompt for context

        Returns:
            Dictionary with analysis results

        Raises:
            anthropic.APIError: If API call fails
        """
        # Default system prompt for OSINT analysis
        if system_prompt is None:
            system_prompt = self._get_default_system_prompt()

        # Format data for Claude
        data_str = json.dumps(data, indent=2, default=str)

        # Construct user message
        user_message = f"""
{prompt}

OSINT Data to Analyze:
```json
{data_str}
```

Please provide your analysis following these guidelines:
1. Cite specific data points from the sources
2. Distinguish between facts and inferences
3. Assign confidence levels (HIGH/MEDIUM/LOW)
4. Identify any contradictions or gaps
5. Provide actionable insights
"""

        try:
            # Call Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )

            # Extract analysis
            analysis = response.content[0].text

            return {
                "analysis": analysis,
                "model": self.model,
                "timestamp": datetime.utcnow().isoformat(),
                "usage": {
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens,
                },
                "success": True,
            }

        except anthropic.APIError as e:
            logger.error(f"Claude API error: {e}")
            return {
                "analysis": None,
                "error": str(e),
                "success": False,
            }

    def generate_executive_summary(
        self, findings: List[Dict[str, Any]]
    ) -> str:
        """Generate executive summary from OSINT findings.

        Args:
            findings: List of OSINT findings

        Returns:
            Executive summary (max 10 bullets)
        """
        prompt = """
Based on the OSINT findings provided, generate an executive summary with:
- Maximum 10 bullet points
- Each bullet 1-2 sentences
- Lead with most critical findings
- Use labels: CONFIRMED, LIKELY, HYPOTHESIS, RISK, OPPORTUNITY
- Confidence levels for each claim

Format as markdown bullets.
"""

        result = self.analyze_osint_data(
            data={"findings": findings}, prompt=prompt
        )

        return result.get("analysis", "")

    def assess_risk(
        self,
        target: str,
        intelligence: Dict[str, Any],
        risk_categories: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Perform risk assessment using Claude.

        Args:
            target: Target entity (person, company, domain)
            intelligence: Collected intelligence
            risk_categories: Specific risk categories to assess

        Returns:
            Risk assessment with scores and recommendations
        """
        if risk_categories is None:
            risk_categories = [
                "Legal/Compliance",
                "Financial",
                "Reputational",
                "Security",
                "Operational",
            ]

        prompt = f"""
Perform a comprehensive risk assessment for: {target}

Risk Categories to Assess:
{chr(10).join(f'- {cat}' for cat in risk_categories)}

For each category, provide:
1. Risk Level (CRITICAL/HIGH/MEDIUM/LOW/NONE)
2. Specific risks identified (with evidence)
3. Likelihood assessment
4. Potential impact
5. Mitigation recommendations

Use the OSINT intelligence provided to support your assessment.
"""

        result = self.analyze_osint_data(
            data=intelligence, prompt=prompt
        )

        return {
            "target": target,
            "assessment": result.get("analysis"),
            "categories": risk_categories,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def validate_facts(
        self, claims: List[Dict[str, Any]], sources: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Cross-validate facts against sources.

        Args:
            claims: List of claims to validate
            sources: List of source data

        Returns:
            Validation results with confidence scores
        """
        prompt = """
Cross-validate each claim against the provided sources.

For each claim, provide:
1. Validation Status (VERIFIED/LIKELY/UNVERIFIED/CONTRADICTED)
2. Supporting sources (cite specific sources)
3. Confidence level (0-100%)
4. Contradicting evidence (if any)
5. Recommendation (accept/reject/need more data)

Return results in structured format.
"""

        data = {"claims": claims, "sources": sources}

        result = self.analyze_osint_data(data=data, prompt=prompt)

        return {
            "validation_results": result.get("analysis"),
            "claims_validated": len(claims),
            "timestamp": datetime.utcnow().isoformat(),
        }

    def identify_patterns(
        self, data_points: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Identify patterns and connections in OSINT data.

        Args:
            data_points: List of data points to analyze

        Returns:
            Identified patterns and relationships
        """
        prompt = """
Analyze the data points and identify:
1. Patterns (temporal, geographic, behavioral)
2. Connections between entities
3. Anomalies or outliers
4. Significant correlations
5. Network relationships (if applicable)

Provide visual description of relationships and suggest visualization approach.
"""

        result = self.analyze_osint_data(
            data={"data_points": data_points}, prompt=prompt
        )

        return {
            "patterns": result.get("analysis"),
            "data_points_analyzed": len(data_points),
            "timestamp": datetime.utcnow().isoformat(),
        }

    def generate_report(
        self,
        target: str,
        intelligence: Dict[str, Any],
        report_type: str = "detailed",
    ) -> str:
        """Generate formatted OSINT report.

        Args:
            target: Target entity
            intelligence: Collected intelligence
            report_type: Type of report (executive/detailed/risk)

        Returns:
            Formatted markdown report
        """
        prompts = {
            "executive": "Generate a concise executive summary (max 1 page)",
            "detailed": "Generate a comprehensive intelligence report (5-10 pages)",
            "risk": "Generate a risk-focused assessment report",
        }

        base_prompt = prompts.get(
            report_type, prompts["detailed"]
        )

        prompt = f"""
{base_prompt}

Target: {target}

Report Structure:
1. Executive Summary (max 10 bullets)
2. Key Findings
3. Risk Assessment
4. Recommendations
5. Source Attribution

Use professional intelligence report formatting.
Cite all sources.
Distinguish facts from inferences.
Include confidence levels.
"""

        result = self.analyze_osint_data(
            data=intelligence, prompt=prompt
        )

        return result.get("analysis", "")

    def _get_default_system_prompt(self) -> str:
        """Get default system prompt for OSINT analysis."""
        return """You are an expert OSINT analyst with deep expertise in:
- Open source intelligence gathering and analysis
- Risk assessment and threat intelligence
- Pattern recognition and network analysis
- Fact verification and source evaluation
- Intelligence report writing

Your analysis style:
- Precise and factual
- Cite specific evidence
- Distinguish facts from inferences
- Assign confidence levels to all claims
- Identify gaps and contradictions
- Provide actionable recommendations

You follow these principles:
- Transparency: Always cite sources
- Accuracy: Verify facts when possible
- Ethics: Operate within legal boundaries
- Objectivity: Avoid bias and speculation
- Clarity: Write for decision-makers

Confidence levels:
- CONFIRMED/HIGH (90-100%): Multiple reliable sources
- LIKELY/MEDIUM (70-89%): Good evidence, some uncertainty
- HYPOTHESIS/LOW (<70%): Single source or speculative

Always use structured markdown formatting for readability.
"""


# Convenience function
def analyze_with_claude(
    data: Dict[str, Any],
    prompt: str,
    api_key: str,
    model: str = "claude-3-5-sonnet-20241022",
) -> Dict[str, Any]:
    """Quick OSINT analysis with Claude.

    Args:
        data: OSINT data to analyze
        prompt: Analysis question
        api_key: Anthropic API key
        model: Claude model to use

    Returns:
        Analysis results
    """
    analyzer = ClaudeAnalyzer(api_key=api_key, model=model)
    return analyzer.analyze_osint_data(data=data, prompt=prompt)
