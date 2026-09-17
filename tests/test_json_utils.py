import json

import pytest

from python_foundations.json_utils import JsonLoadError, load_json_file, save_json_file


def test_load_json_file_returns_python_dictionary(tmp_path) -> None:
    document = tmp_path / "document.json"

    document.write_text(
        json.dumps(
            {
                "id": "doc-1",
                "text": "Python is useful for AI engineering.",
                "score": 0.91,
            }
        ),
        encoding="utf-8",
    )

    result = load_json_file(str(document))

    assert result["id"] == "doc-1"
    assert result["text"] == "Python is useful for AI engineering."
    assert result["score"] == 0.91


def test_load_json_file_raises_error_for_invalid_json(tmp_path) -> None:
    document = tmp_path / "document.json"

    document.write_text(
        '{"id": "doc-1", "text": "Python is useful for AI engineering."',
        encoding="utf-8",
    )

    with pytest.raises(JsonLoadError) as error:
        load_json_file(str(document))

    assert str(error.value) == f"Invalid JSON in file: {document}"


def test_save_json_file_creates_file_with_correct_content(tmp_path) -> None:
    document = tmp_path / "document.json"
    data = {
        "id": "doc-1",
        "text": "Python is useful for AI engineering.",
        "score": 0.91,
    }

    save_json_file(str(document), data)

    with open(document, "r", encoding="utf-8") as file:
        content = json.load(file)

    assert content == data
