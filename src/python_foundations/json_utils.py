import json


class JsonLoadError(Exception):
    pass


def load_json_file(file_path: str) -> dict[str, object]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        raise JsonLoadError(f"Invalid JSON in file: {file_path}") from error


def save_json_file(file_path: str, data: dict[str, object]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
