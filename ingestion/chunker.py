from llama_index.core.node_parser import SentenceSplitter

class EnterpriseChunker:

    def __init__(self):

        self.parser = SentenceSplitter(
            chunk_size=512,
            chunk_overlap=100
        )

    def chunk(self, docs):

        nodes = self.parser.get_nodes_from_documents(docs)

        return nodes