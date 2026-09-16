class DocumentLoadError(Exception):
    pass


def load_document(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise DocumentLoadError(f"Could not find document: {file_path}")
