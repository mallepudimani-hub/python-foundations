import json

from pydantic import BaseModel, ValidationError


class UsageModel(BaseModel):
    input_tokens: int
    output_tokens: int


class AIResponseModel(BaseModel):
    id: str
    model: str
    usage: UsageModel


class AIResponseParseError(Exception):
    """Raised when an external AI response cannot be parsed or validated."""


def get_output_tokens(response: AIResponseModel) -> int:
    return response.usage.output_tokens


def parse_ai_response(json_text: str) -> AIResponseModel:
    try:
        data = json.loads(json_text)
        return AIResponseModel(**data)
    except (json.JSONDecodeError, ValidationError) as error:
        raise AIResponseParseError("Invalid AI response") from error
