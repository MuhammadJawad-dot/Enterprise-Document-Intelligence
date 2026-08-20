from indexes.vector_index import VectorIndex
from indexes.tree_index import EnterpriseTreeIndex


class IndexManager:

    def __init__(self, documents, nodes):

        self.documents = documents
        self.nodes = nodes

        self.vector_index = None
        self.tree_index = None

    def build_indexes(self):

        print("Building Vector Index...")

        vector = VectorIndex(self.nodes)

        self.vector_index = vector.build()

        print("[SUCCESS] Vector Index created")

        print("Building Tree Index...")

        tree = EnterpriseTreeIndex(
            self.documents
        )

        self.tree_index = tree.build()

        print("[SUCCESS] Tree Index created")

    def get_vector_engine(self):

        return self.vector_index.as_query_engine(
            similarity_top_k=5
        )

    def get_tree_engine(self):

        return self.tree_index.as_query_engine()