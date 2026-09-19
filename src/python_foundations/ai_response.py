import json

from pydantic import BaseModel


class UsageModel(BaseModel):
    input_tokens: int
    output_tokens: int


class AIResponseModel(BaseModel):
    id: str
    model: str
    usage: UsageModel


def get_output_tokens(response: AIResponseModel) -> int:
    return response.usage.output_tokens


def parse_ai_response(json_text: str) -> AIResponseModel:
    data = json.loads(json_text)
    return AIResponseModel(**data)
