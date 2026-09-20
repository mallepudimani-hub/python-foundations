import pytest
from pydantic import ValidationError

from python_foundations.ai_response import (
    AIResponseModel,
    AIResponseParseError,
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


def test_parse_ai_response_raises_custom_error_for_invalid_structure() -> None:
    invalid_json_text = '{"id": "resp-4", "model": "gpt-3.5"}'  # Missing usage

    with pytest.raises(AIResponseParseError) as exc_info:
        parse_ai_response(invalid_json_text)

    assert str(exc_info.value) == "Invalid AI response"


def test_parse_ai_response_raises_custom_error_for_invalid_json() -> None:
    invalid_json = '{"id": "resp-4", "model": "gpt-3.5"'

    with pytest.raises(AIResponseParseError) as exc_info:
        parse_ai_response(invalid_json)

    assert str(exc_info.value) == "Invalid AI response"
