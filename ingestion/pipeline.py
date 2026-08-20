from pathlib import Path

from ingestion.loaders import EnterpriseLoader
from ingestion.metadata import MetadataEnricher
from ingestion.chunker import EnterpriseChunker


class IngestionPipeline:

    def __init__(self):

        self.loader = EnterpriseLoader()
        self.metadata = MetadataEnricher()
        self.chunker = EnterpriseChunker()

    def process_folder(self, folder_path):

        all_docs = []

        for file in Path(folder_path).iterdir():

            if file.suffix == ".pdf":
                docs = self.loader.load_pdf(str(file))

            elif file.suffix == ".docx":
                docs = self.loader.load_docx(str(file))

            elif file.suffix == ".txt":
                docs = self.loader.load_txt(str(file))

            else:
                continue

            docs = self.metadata.enrich(docs)

            all_docs.extend(docs)

        nodes = self.chunker.chunk(all_docs)

        return all_docs,nodes