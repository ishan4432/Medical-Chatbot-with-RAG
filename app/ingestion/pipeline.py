import hashlib
from pathlib import Path

from app.ingestion.chunker import create_chunks
from app.ingestion.loader import load_documents


def ingest_documents(directory: str) -> list[dict]:
    """Load documents and produce chunks with traceable metadata."""

    documents = load_documents(directory)
    records = []

    for document in documents:
        source = document["source"]

        # Derive a repeatable ID from the source path.
        document_id = hashlib.sha256(
            source.encode("utf-8")
        ).hexdigest()[:16]

        chunks = create_chunks(document["text"])

        for index, chunk in enumerate(chunks):
            chunk_id = f"{document_id}-{index:04d}"

            records.append(
                {
                    "chunk_id": chunk_id,
                    "document_id": document_id,
                    "text": chunk,
                    "source": source,
                    "chunk_index": index,
                    "metadata": {
                        "source": source,
                        "document_id": document_id,
                        "chunk_index": index,
                    },
                }
            )

    return records
