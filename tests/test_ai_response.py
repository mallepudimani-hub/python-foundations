import pytest
from pydantic import ValidationError

from python_foundations.ai_response import (
    AIResponseModel,
    get_output_tokens,
    parse_ai_response,
)


def test_get_output_tokens_valid_response() -> None:
    response = {
        "id": "resp-1",
        "model": "gpt-3.5",
        "usage": {"input_tokens": 100, "output_tokens": 50},
    }

    validated_response = AIResponseModel(**response)

    assert get_output_tokens(validated_response) == 50


def test_get_output_tokens_with_invalid_response() -> None:
    response = {
        "id": "resp-2",
        "model": "gpt-3.5",
        "usage": {"input_tokens": 100, "output_tokens": "not-a-number"},
    }

    with pytest.raises(ValidationError):
        AIResponseModel(**response)


def test_parse_ai_response_valid_json() -> None:
    json_text = '{"id": "resp-3", "model": "gpt-3.5", "usage": {"input_tokens": 100, "output_tokens": 50}}'
    response_model = parse_ai_response(json_text)

    assert response_model.id == "resp-3"
    assert response_model.model == "gpt-3.5"
    assert response_model.usage.input_tokens == 100
    assert response_model.usage.output_tokens == 50
