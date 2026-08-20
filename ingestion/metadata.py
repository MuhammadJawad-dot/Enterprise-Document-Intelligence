# from pathlib import Path


# def enrich_metadata(document):
#     """
#     Add standardized metadata to a LlamaIndex Document.
#     """

#     metadata = document.metadata or {}

#     file_path = metadata.get("file_path", "")

#     if file_path:
#         path = Path(file_path)

#         metadata["file_name"] = path.name
#         metadata["file_extension"] = path.suffix.lower()

#     metadata["source_type"] = metadata.get(
#         "file_extension",
#         "unknown"
#     )

#     document.metadata = metadata

#     return document

# for document in documents:
#     enrich_metadata(document)

from datetime import datetime

class MetadataEnricher:

    # def enrich(self, docs):

    #     for doc in docs:

    #         doc.metadata["ingestion_time"] = str(datetime.now())

    #         if "department" not in doc.metadata:
    #             doc.metadata["department"] = "general"

    #     return docs
    def enrich(self, docs):
        for doc in docs:
            doc.metadata["ingestion_time"] = str(datetime.now())
            
            # Check the source file name to determine the department
            source_file = doc.metadata.get("source", "")
            
            if "Policies" in source_file:
                doc.metadata["department"] = "hr"
            elif "Our Code of Conduct" in source_file:
                doc.metadata["department"] = "jp_morgan"
            elif "department" not in doc.metadata:
                    doc.metadata["department"] = "general"

        return docs
