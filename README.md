
# Medical RAG Chatbot

A Python project exploring Retrieval-Augmented Generation (RAG) for
grounded answers from medical reference documents.

## Current progress

- [x] Project structure and virtual environment
- [x] Initial text chunking component
- [x] Basic chunking assertions
- [ ] Document loading and metadata
- [ ] Embedding generation
- [ ] Vector retrieval with Pinecone
- [ ] Grounded answer generation
- [ ] Evaluation and benchmarking
- [ ] API and deployment

## Current implementation

The chunker uses LangChain's
`RecursiveCharacterTextSplitter`.

The initial test uses synthetic text and checks that:
- Multiple chunks are produced.
- Each chunk stays within the configured character limit.
- No empty chunks are returned.

## Status of performance claims

Retrieval precision, hallucination reduction, latency, and cost savings
have not yet been measured. These will be evaluated using documented
experiments before being reported as results.

## Development setup

Create and activate a virtual environment, then install dependencies
from `requirements.txt` after they have been defined.
