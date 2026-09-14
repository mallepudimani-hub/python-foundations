def search_documents(documents: list[str], query: str) -> list[str]:
    normalized_query = query.lower()
    return [document for document in documents if normalized_query in document.lower()]


documents = [
    "Python is widely used for AI engineering.",
    "RAG combines retrieval with generation.",
    "FastAPI is useful for building Python APIs.",
]

search_query = "python"
search_results = search_documents(documents, search_query)
print(f"Search results for '{search_query}':")
for result in search_results:
    print(result)
