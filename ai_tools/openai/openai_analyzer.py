"""
OpenAI OSINT Analyzer

Integrates OpenAI's GPT models for OSINT analysis and data extraction.
Optimized for structured data extraction and entity recognition.
"""

from typing import Dict, Any, List, Optional
import logging
from datetime import datetime
import json

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

logger = logging.getLogger(__name__)


class OpenAIAnalyzer:
    """OpenAI-powered OSINT analysis engine.

    Uses GPT models for:
    - Structured data extraction
    - Entity recognition and tagging
    - Information synthesis
    - Q&A on collected intelligence
    - Translation and multilingual analysis

    Example:
        >>> analyzer = OpenAIAnalyzer(api_key="your-key")
        >>> result = analyzer.extract_entities(text=document)
        >>> print(result["entities"])
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4-turbo-preview",
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ):
        """Initialize OpenAI analyzer.

        Args:
            api_key: OpenAI API key (or set OPENAI_API_KEY env var)
            model: GPT model to use
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum tokens in response

        Raises:
            ImportError: If openai package not installed
            ValueError: If API key not provided
        """
        if OpenAI is None:
            raise ImportError(
                "openai package not installed. "
                "Install with: pip install openai"
            )

        if not api_key:
            raise ValueError(
                "API key required. Set OPENAI_API_KEY environment "
                "variable or pass api_key parameter."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        logger.info(f"Initialized OpenAI analyzer with model {model}")

    def analyze_osint_data(
        self,
        data: Dict[str, Any],
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Analyze OSINT data using GPT.

        Args:
            data: OSINT data to analyze
            prompt: Analysis question/prompt
            system_prompt: Optional system prompt

        Returns:
            Dictionary with analysis results
        """
        if system_prompt is None:
            system_prompt = self._get_default_system_prompt()

        data_str = json.dumps(data, indent=2, default=str)

        user_message = f"""{prompt}

OSINT Data:
```json
{data_str}
```
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
            )

            analysis = response.choices[0].message.content

            return {
                "analysis": analysis,
                "model": self.model,
                "timestamp": datetime.utcnow().isoformat(),
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens,
                },
                "success": True,
            }

        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return {
                "analysis": None,
                "error": str(e),
                "success": False,
            }

    def extract_entities(
        self, text: str, entity_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Extract named entities from text.

        Args:
            text: Text to analyze
            entity_types: Types of entities to extract
                (people, organizations, locations, etc.)

        Returns:
            Dictionary with extracted entities
        """
        if entity_types is None:
            entity_types = [
                "people",
                "organizations",
                "locations",
                "dates",
                "emails",
                "phone_numbers",
                "domains",
            ]

        prompt = f"""
Extract the following entity types from the text:
{', '.join(entity_types)}

Return results as JSON with entity type as key and list of entities as value.
For each entity, include context (surrounding text).

Text to analyze:
{text}
"""

        result = self.analyze_osint_data(data={}, prompt=prompt)

        return {
            "entities": result.get("analysis"),
            "entity_types": entity_types,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def summarize_intelligence(
        self, intelligence: Dict[str, Any], max_bullets: int = 10
    ) -> str:
        """Generate concise summary of intelligence.

        Args:
            intelligence: Collected intelligence
            max_bullets: Maximum number of bullet points

        Returns:
            Markdown summary
        """
        prompt = f"""
Summarize the OSINT intelligence in {max_bullets} bullet points or less.

Focus on:
- Key findings
- Risks identified
- Confidence levels
- Actionable insights

Use professional intelligence summary format.
"""

        result = self.analyze_osint_data(
            data=intelligence, prompt=prompt
        )

        return result.get("analysis", "")

    def translate_text(
        self, text: str, target_language: str = "English"
    ) -> str:
        """Translate text for multilingual OSINT.

        Args:
            text: Text to translate
            target_language: Target language

        Returns:
            Translated text
        """
        prompt = f"Translate the following text to {target_language}:\n\n{text}"

        result = self.analyze_osint_data(data={}, prompt=prompt)

        return result.get("analysis", "")

    def _get_default_system_prompt(self) -> str:
        """Get default system prompt."""
        return """You are an expert OSINT analyst specializing in:
- Information extraction and entity recognition
- Intelligence synthesis and summarization
- Pattern analysis and correlation
- Structured data formatting

Provide precise, factual analysis with citations.
Use structured formats (JSON, markdown tables) when appropriate.
Distinguish facts from inferences.
"""


# Convenience function
def analyze_with_openai(
    data: Dict[str, Any],
    prompt: str,
    api_key: str,
    model: str = "gpt-4-turbo-preview",
) -> Dict[str, Any]:
    """Quick OSINT analysis with OpenAI.

    Args:
        data: OSINT data to analyze
        prompt: Analysis question
        api_key: OpenAI API key
        model: GPT model to use

    Returns:
        Analysis results
    """
    analyzer = OpenAIAnalyzer(api_key=api_key, model=model)
    return analyzer.analyze_osint_data(data=data, prompt=prompt)
