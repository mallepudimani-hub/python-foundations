from python_foundations.search import search_documents


def test_search_documents_returns_matching_documents() -> None:
    documents = [
        "Python is widely used for AI engineering.",
        "RAG combines retrieval with generation.",
        "FastAPI is useful for building Python APIs.",
    ]

    results = search_documents(documents, "python")

    assert results == [
        "Python is widely used for AI engineering.",
        "FastAPI is useful for building Python APIs.",
    ]
