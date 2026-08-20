from llama_index.core import VectorStoreIndex,StorageContext
from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core.storage.docstore import SimpleDocumentStore


class AutoMergeRetriever:

    def __init__(self):

        self.index = None
        self.retriever = None

    def build(self, documents):

        # Create hierarchical nodes
        node_parser = HierarchicalNodeParser.from_defaults(
            chunk_sizes=[2048, 512, 128]
        )

        nodes = node_parser.get_nodes_from_documents(
            documents
        )

        # Keep only leaf nodes for vector indexing
        leaf_nodes = [
            node
            for node in nodes
            if node.child_nodes is None
            or len(node.child_nodes) == 0
        ]

        docstore = SimpleDocumentStore()
        docstore.add_documents(nodes)
        
        storage_context = StorageContext.from_defaults(docstore=docstore)

        self.index = VectorStoreIndex(
            leaf_nodes,
            storage_context=storage_context
        )

        base_retriever = self.index.as_retriever(
            similarity_top_k=6
        )

        self.retriever = AutoMergingRetriever(
            base_retriever,
            storage_context=self.index.storage_context
        )

        return self.retriever