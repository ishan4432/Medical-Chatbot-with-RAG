import pytest

from app.ingestion.loader import load_documents
from app.ingestion.pipeline import ingest_documents


def test_load_documents_returns_source_and_text():
    documents = load_documents("data/documents")

    assert len(documents) >= 1

    for document in documents:
        assert document["text"].strip()
        assert document["source"]


def test_ingestion_returns_traceable_metadata():
    records = ingest_documents("data/documents")

    assert len(records) >= 1

    for record in records:
        assert record["text"].strip()
        assert record["source"]
        assert record["document_id"]
        assert record["chunk_id"]
        assert isinstance(record["chunk_index"], int)
        assert record["metadata"]["source"] == record["source"]
        assert record["metadata"]["document_id"] == record["document_id"]


def test_chunk_ids_are_unique():
    records = ingest_documents("data/documents")
    chunk_ids = [record["chunk_id"] for record in records]

    assert len(chunk_ids) == len(set(chunk_ids))


def test_repeated_ingestion_produces_same_ids():
    first_run = ingest_documents("data/documents")
    second_run = ingest_documents("data/documents")

    assert [r["chunk_id"] for r in first_run] == [
        r["chunk_id"] for r in second_run
    ]


def test_missing_directory_raises_error():
    with pytest.raises(FileNotFoundError):
        load_documents("data/directory_that_does_not_exist")
