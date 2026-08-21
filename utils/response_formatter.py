from utils.source_tracker import SourceTracker


class ResponseFormatter:

    def __init__(self):

        self.source_tracker = SourceTracker()

    def format(self, response):

        answer = str(response)

        nodes = getattr(
            response,
            "source_nodes",
            []
        )

        sources = self.source_tracker.format_sources(
            nodes
        )

        if not sources:
            return (
                f"{answer}\n\n"
                "Sources:\n"
                "No source metadata available."
            )

        return (
            f"{answer}\n\n"
            "Sources:\n"
            f"{sources}"
        )