from typing import Optional


class LLMResponse:
    """
    `LLMResponse` stores information parsed from LLM's response
    """

    def __init__(self, code: Optional[str] = None, explanation: Optional[str] = None):
        self.code = code
        self.explanation = explanation

    def __str__(self):
        code_brief = self.code[:20] + "..." if len(self.code) > 20 else self.code
        explanation_brief = self.explanation[:20] + "..." if len(self.explanation) > 20 else self.explanation
        return f"LLMResponse(code={code_brief}, explanation={explanation_brief})"

    def __repr__(self):
        return self.__str__()


class Example:
    """
    `Example` stores an example for the developer to learn how to do the task
    """
    def __init__(self, query: str, response: str):
        self.query = query
        self.response = response

    def __str__(self):
        query_brief = self.query[:20] + "..." if len(self.query) > 20 else self.query
        response_brief = self.response[:20] + "..." if len(self.response) > 20 else self.response
        return f"Example(query={query_brief}, response={response_brief})"

    def __repr__(self):
        return self.__str__()
