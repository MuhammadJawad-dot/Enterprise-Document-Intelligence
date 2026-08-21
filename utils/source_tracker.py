from utils.citations import CitationManager


class SourceTracker:

    def __init__(self):

        self.citation_manager = CitationManager()

    def collect(self, nodes):

        sources = []

        seen = set()

        for node in nodes:

            source = self.citation_manager.get_source(
                node
            )

            key = (
                source["document_id"],
                source["source"],
                source["page"]
            )

            if key in seen:
                continue

            seen.add(key)

            sources.append(source)

        return sources

    def format_sources(self, nodes):

        sources = self.collect(nodes)

        output = []

        for i, source in enumerate(
            sources,
            start=1
        ):

            text = f"[{i}] {source['source']}"

            if source["page"] is not None:
                text += f" — Page {source['page']}"

            output.append(text)

        return "\n".join(output)