import pytest

from python_foundations.file_loader import DocumentLoadError, load_document


def test_load_document_raises_error_for_missing_file() -> None:
    with pytest.raises(DocumentLoadError) as error:
        load_document("missing.txt")

    assert str(error.value) == "Could not find document: missing.txt"


def test_load_document_returns_file_content(tmp_path) -> None:
    document = tmp_path / "knowledge.txt"
    document.write_text("Python is useful for AI engineering.")

    content = load_document(str(document))

    assert content == "Python is useful for AI engineering."
