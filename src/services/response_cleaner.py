import re


class ResponseCleaner:

    @staticmethod
    def clean(text: str) -> str:
        text = text.strip()

        # Remove markdown code fences
        text = re.sub(r"^```json\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

        return text.strip()