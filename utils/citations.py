class CitationManager:

    @staticmethod
    def get_source(node):

        metadata = node.metadata

        source = (
            metadata.get("source")
            or metadata.get("file_name")
            or metadata.get("filename")
            or "Unknown source"
        )

        page = (
            metadata.get("page")
            or metadata.get("page_number")
            or metadata.get("page_label")
        )

        document_id = metadata.get(
            "document_id",
            "unknown"
        )

        return {
            "document_id": document_id,
            "source": source,
            "page": page
        }

    @staticmethod
    def format_citation(node, index):

        source = CitationManager.get_source(node)

        citation = f"[{index}] {source['source']}"

        if source["page"] is not None:
            citation += f" — Page {source['page']}"

        return citation