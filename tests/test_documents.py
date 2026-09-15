from python_foundations.documents import get_high_quality_texts


def test_get_high_quality_texts() -> None:
    documents = [
        {
            "id": "doc-1",
            "text": "Python is useful for AI engineering.",
            "score": 0.91,
        },
        {
            "id": "doc-2",
            "text": "React is a frontend framework.",
            "score": 0.72,
        },
        {
            "id": "doc-3",
            "text": "RAG combines retrieval and generation.",
            "score": 0.88,
        },
    ]

    results = get_high_quality_texts(documents, minimum_score=0.85)

    assert results == [
        "Python is useful for AI engineering.",
        "RAG combines retrieval and generation.",
    ]
