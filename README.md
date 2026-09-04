# Enterprise Document Intelligence

Enterprise Document Intelligence is a RAG (Retrieval-Augmented Generation) application designed for querying and extracting information from various types of enterprise documents. It leverages state-of-the-art embedding models and LLMs to provide a chat interface with your own data.

## Features

- **Multi-format Ingestion**: Processes PDFs, DOCX, and TXT files.
- **Advanced Indexing**: Utilizes both Vector Indexes (for similarity search) and Tree Indexes (for hierarchical summarization).
- **Extensibility**: Includes advanced retrieval mechanisms like `SentenceWindowRetriever` and `AutoMergeRetriever` (ready to be integrated).
- **Agentic Planner**: Framework designed to integrate an agentic `QueryPlanner` for complex querying workflows.
- **LLM Integration**: Configured to use the fast Groq API for LLM completion, utilizing high-performance models.
- **Interactive Chat**: A built-in terminal-based chat interface to instantly query your ingested documents.

## Project Structure

```
Enterprise-Document-Intelligence/
├── agents/             # Agent tools and query planners (e.g., router, tools)
├── data/               # Contains documents and tables for ingestion
│   └── documents/      # Place your raw PDF, DOCX, and TXT files here
├── indexes/            # Index management (VectorIndex, TreeIndex)
├── ingestion/          # Document loading, chunking, and metadata enrichment
├── llm/                # LLM configuration (Groq setup)
├── retrieval/          # Advanced retrieval techniques (Sentence Window, Auto Merge)
├── utils/              # Utilities like response formatting and source tracking
├── main.py             # Entry point for running the application
├── .env                # Environment variables (API keys)
└── requirements.txt    # (Assuming dependencies are tracked)
```

## Prerequisites

- Python 3.8+
- [Groq API Key](https://console.groq.com/) for LLM inference.
- HuggingFace account (optional, though it uses `sentence-transformers/all-MiniLM-L6-v2` locally).

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd Enterprise-Document-Intelligence
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   Make sure you have `llama-index`, `llama-index-llms-groq`, `llama-index-embeddings-huggingface`, `python-dotenv`, and other necessary packages installed.
   ```bash
   pip install llama-index llama-index-llms-groq llama-index-embeddings-huggingface python-dotenv
   ```
   *(Note: Adjust this step based on the actual requirements file if provided)*

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. **Add Documents:**
   Place the documents you want to analyze (PDF, DOCX, TXT) inside the `data/documents/` directory.

2. **Run the Application:**
   Execute the `main.py` script to start the ingestion process and the interactive chat session.
   ```bash
   python main.py
   ```

3. **Chat Interface:**
   Once the indexes are built, you will be prompted with a chat interface in the terminal. Type your questions regarding the documents. Type `exit` or `quit` to stop.

## Advanced Features (Under Development)

The codebase contains scaffolding for more advanced RAG features:
- **Sentence Window Retrieval**: Retrieves a broader context around a matching sentence for better LLM comprehension.
- **Auto Merge Retrieval**: Hierarchically merges smaller chunks into parent chunks for cohesive answers.
- **Agentic Tools**: `QueryPlanner` and retrieval tools designed for complex reasoning tasks.

## License

This project is licensed under the MIT License.
