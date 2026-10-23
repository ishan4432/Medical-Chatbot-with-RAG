import pytest

from app.ingestion.chunker import create_chunks


def test_empty_text_returns_no_chunks():
    assert create_chunks("") == []
    assert create_chunks("   ") == []


def test_long_text_produces_multiple_chunks():
    text = " ".join(
        f"Medical sentence number {i} describes a health topic."
        for i in range(1, 101)
    )

    chunks = create_chunks(
        text,
        chunk_size=200,
        chunk_overlap=30,
    )

    assert len(chunks) > 1


def test_chunks_are_nonempty_and_within_size_limit():
    text = " ".join(
        f"Medical sentence number {i} describes a health topic."
        for i in range(1, 101)
    )

    chunks = create_chunks(
        text,
        chunk_size=200,
        chunk_overlap=30,
    )

    assert all(chunk.strip() for chunk in chunks)
    assert all(len(chunk) <= 200 for chunk in chunks)


def test_invalid_chunk_settings_are_rejected():
    with pytest.raises(ValueError):
        create_chunks("Sample medical text.", chunk_size=0)

    with pytest.raises(ValueError):
        create_chunks("Sample medical text.", chunk_overlap=-1)

    with pytest.raises(ValueError):
        create_chunks(
            "Sample medical text.",
            chunk_size=100,
            chunk_overlap=100,
        )
