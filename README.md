# RAG Project

A small Retrieval-Augmented Generation (RAG) project using Python, Jupyter Notebooks, and OpenAI.

## Overview

This project demonstrates a simple RAG workflow:

1. Load documents or text data
2. Split the text into chunks
3. Create embeddings
4. Retrieve relevant chunks for a user query
5. Generate an answer using the retrieved context

## Files

* `Mini_RAG.ipynb`
  Basic RAG implementation.

* `Mini_RAG_Upgrade.ipynb`
  Improved version with additional functionality.

## Setup
Install dependencies:

```bash
pip install openai jupyter python-dotenv
```

## API Key

Create a local `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Important: `.env` must not be committed to GitHub.

## Run

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open one of the notebooks in your browser.

## Notes

This repository is intended as a compact learning project for understanding the basic structure of a RAG pipeline.

## License

MIT
