from llama_index.core import VectorStoreIndex


class VectorIndex:

    def __init__(self, nodes):
        self.nodes = nodes
        self.index = None

    def build(self):
        self.index = VectorStoreIndex(
            self.nodes
        )

        return self.index

    def query_engine(self, similarity_top_k=5):

        if self.index is None:
            raise ValueError("Index has not been built yet.")

        return self.index.as_query_engine(
            similarity_top_k=similarity_top_k
        )