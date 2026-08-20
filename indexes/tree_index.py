from llama_index.core import TreeIndex
import os
from llama_index.core import TreeIndex, StorageContext, load_index_from_storage


class EnterpriseTreeIndex:

    def __init__(self, documents):
        self.documents = documents
        self.index = None

    # def build(self):

    #     self.index = TreeIndex.from_documents(
    #         self.documents
    #     )

    #     return self.index

    # def query_engine(self):

    #     if self.index is None:
    #         raise ValueError(
    #             "Tree index has not been built yet."
    #         )

    #     return self.index.as_query_engine()
    def build(self):
        persist_dir = "./tree_db"
        
        # 1. Check if we already saved the index previously
        if os.path.exists(persist_dir):
            print("Loading existing Tree Index from disk...")
                # Load the buckets from the folder
            storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
            # Rebuild the index from the storage
            self.index = load_index_from_storage(storage_context)
        
        else:
            print("Building new Tree Index from scratch...")
            # 2. If it doesn't exist, build it normally using your documents
            self.index = TreeIndex.from_documents(self.documents)
            
            # 3. Save the doc store and index store buckets to the folder!
            self.index.storage_context.persist(persist_dir=persist_dir)

        return self.index
    def query_engine(self):
        if self.index is None:
            raise ValueError(
                "Tree index has not been built yet."
            )
        return self.index.as_query_engine()