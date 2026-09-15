from typing import TypedDict


class Document(TypedDict):
    id: str
    text: str
    score: float


documents: list[Document] = [
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


def get_high_quality_texts(
    documents: list[Document], minimum_score: float
) -> list[str]:
    return [
        document["text"] for document in documents if document["score"] >= minimum_score
    ]


def main() -> None:
    search_results = get_high_quality_texts(documents, minimum_score=0.85)
    print(search_results)


if __name__ == "__main__":
    main()
