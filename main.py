# import asyncio
# from llama_index.core import Settings
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# # Import pipelines and indexes
# from ingestion.pipeline import IngestionPipeline
# from indexes.index_manager import IndexManager
# from retrieval.sentence_window import SentenceWindowRetriever
# from retrieval.auto_merge import AutoMergeRetriever
# from llm.llm import configure_llm

# # Import Agent/Tools
# from agents.tools import create_retrieval_tools, create_auto_merge_engine
# from agents.planner import QueryPlanner
# from utils.response_formatter import ResponseFormatter

# def setup_environment():
#     """Configure embeddings and LLM."""
#     print("Setting up environment...")
#     Settings.embed_model = HuggingFaceEmbedding(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )
#     configure_llm()

# async def main():
#     setup_environment()

#     # 1. Ingest Documents
#     print("\n[1/4] Ingesting Documents...")
#     pipeline = IngestionPipeline()
#     documents, nodes = pipeline.process_folder("data/documents")
#     print(f"Loaded {len(documents)} documents and created {len(nodes)} default nodes.")

#     # 2. Build Basic Indexes (Vector & Tree)
#     print("\n[2/4] Building Vector and Tree Indexes...")
#     manager = IndexManager(documents, nodes)
#     manager.build_indexes()
    
#     vector_engine = manager.get_vector_engine()
#     tree_engine = manager.get_tree_engine()
#         # 2. Build Basic Indexes (Vector & Tree)
#     print("\n[2/4] Building Vector and Tree Indexes...")
#     manager = IndexManager(documents, nodes)
#     manager.build_indexes()
    
#     vector_engine = manager.get_vector_engine()
#     tree_engine = manager.get_tree_engine()

#     # --- START OF YOUR TEST CODE ---
#     print("\n--- TESTING RESPONSE FORMATTER ---")
#     response = vector_engine.query("Profit Sharing in Ottit?")
#     formatter = ResponseFormatter()
#     final_answer = formatter.format(response)
    
#     print(final_answer)
    # return  # Stops the rest of main.py from running for this quick test
    # --- END OF YOUR TEST CODE ---

     
#     # 3. Build Advanced Retrievers (Sentence Window & Auto Merge)
#     print("\n[3/4] Building Advanced Retrievers...")
    
#     sentence_window = SentenceWindowRetriever()
#     sentence_window.build(documents)
#     sentence_engine = sentence_window.query_engine()

#     auto_merge = AutoMergeRetriever()
#     auto_merge_retriever = auto_merge.build(documents)
#     auto_merge_engine = create_auto_merge_engine(auto_merge_retriever)

#     # 4. Setup Tools and Planner
#     print("\n[4/4] Setting up Agentic Query Planner...")
#     tools = create_retrieval_tools(
#         vector_engine=vector_engine,
#         tree_engine=tree_engine,
#         sentence_engine=sentence_engine,
#         auto_merge_engine=auto_merge_engine
#     )

#     planner = QueryPlanner(llm=Settings.llm, tools=tools)

#     # 5. Run Test Questions
#     test_questions = [
#         "What is the company's revenue?",
#         "What are the main risks mentioned in the report?",
#         "Give me an overview of Chapter 3.",
#         "Explain the relationship between the company's strategy and employee training.",
#         "Compare the company's performance across two years."
#     ]

#     print("\n" + "*" * 60)
#     print("STARTING TEST QUERIES")
#     print("*" * 60)

#     for i, question in enumerate(test_questions, 1):
#         print("\n" + "=" * 60)
#         print(f"QUESTION {i}: {question}")
#         print("-" * 60)
        
#         response = await planner.run(question)
        
#         print("\nANSWER:")
#         print(response)
#         print("=" * 60)
#         # print(f"TOOLS USED: ")
#         # for source in response.sources:
#         #     print(f"- {source.tool_name}")

# if __name__ == "__main__":
#     asyncio.run(main())
import asyncio
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Import pipelines and indexes
from ingestion.pipeline import IngestionPipeline
from indexes.index_manager import IndexManager
from llm.llm import configure_llm
from utils.response_formatter import ResponseFormatter

def setup_environment():
    """Configure embeddings and LLM."""
    print("Setting up environment...")
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    configure_llm()

async def main():
    setup_environment()

    # 1. Ingest Documents
    print("\n[1/2] Ingesting Documents...")
    pipeline = IngestionPipeline()
    documents, nodes = pipeline.process_folder("data/documents")
    print(f"Loaded {len(documents)} documents and created {len(nodes)} default nodes.")

    # 2. Build Indexes
    print("\n[2/2] Building Indexes...")
    manager = IndexManager(documents, nodes)
    manager.build_indexes()
    
    # Get stateless query engine (faster, no chat history pollution)
    query_engine = manager.get_vector_engine()
    formatter = ResponseFormatter()

    print("\n" + "="*50)
    print("CHAT WITH YOUR DOCUMENTS INITIALIZED")
    print("Type 'exit' or 'quit' to stop.")
    print("="*50)

    # Interactive Chat Loop
    while True:
        question = input("\nYou: ")
        
        if not question.strip():
            continue
            
        if question.lower() in ['exit', 'quit']:
            print("Ending chat. Goodbye!")
            break
            
        print("\nThinking...")
        response = query_engine.query(question)
        
        # Format the response with your custom source citations
        final_answer = formatter.format(response)
        
        print("\nAI:")
        print(final_answer)

if __name__ == "__main__":
    asyncio.run(main())
