from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceWindowNodeParser


class SentenceWindowRetriever:

    def __init__(self):

        self.parser = SentenceWindowNodeParser.from_defaults(
            window_size=3,
            window_metadata_key="window",
            original_text_metadata_key="original_text"
        )

        self.index = None

    def build(self, documents):

        nodes = self.parser.get_nodes_from_documents(
            documents
        )

        self.index = VectorStoreIndex(
            nodes
        )

        return self.index

    def query_engine(self):

        if self.index is None:
            raise ValueError(
                "Sentence Window index has not been built."
            )

        return self.index.as_query_engine(
            similarity_top_k=5
        )