
from pathlib import Path


def load_documents(directory: str) -> list[dict[str, str]]:
    """Load UTF-8 text files and preserve their source paths."""

    folder = Path(directory)

    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {folder}")

    documents = []

    for file_path in sorted(folder.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        documents.append(
            {
                "text": text,
                "source": str(file_path),
            }
        )

    return documents
