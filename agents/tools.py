from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import RetrieverQueryEngine



# ----------------------------------
# AUTO-MERGE ENGINE
# ----------------------------------
def create_auto_merge_engine(auto_merge_retriever):
    return RetrieverQueryEngine(
        retriever=auto_merge_retriever
    )
def create_retrieval_tools(
    vector_engine,
    tree_engine,
    sentence_engine,
    auto_merge_engine
):

    tools = []

    vector_tool = QueryEngineTool(
        query_engine=vector_engine,
        metadata=ToolMetadata(
            name="vector_search",
            description=(
                "Use for general semantic questions and "
                "specific factual information."
            )
        )
    )

    tree_tool = QueryEngineTool(
        query_engine=tree_engine,
        metadata=ToolMetadata(
            name="tree_search",
            description=(
                "Use for document-level summaries, chapters, "
                "sections, and hierarchical questions."
            )
        )
    )
    
    auto_merge_tool = QueryEngineTool(
    query_engine=auto_merge_engine,
    metadata=ToolMetadata(
            name="auto_merge_search",
            description=(
                "Use for complex questions where information "
                "may be distributed across multiple related "
                "sections or hierarchical chunks."
            )
        )
    )
    sentence_tool = QueryEngineTool(
        query_engine=sentence_engine,
        metadata=ToolMetadata(
            name="sentence_window_search",
            description=(
                "Use when the question requires precise contextual "
                "information around a specific sentence or statement."
            )
        )
    )

    tools.extend([
        vector_tool,
        tree_tool,
        sentence_tool,
        auto_merge_tool
    ])

    return tools