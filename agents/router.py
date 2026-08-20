from llama_index.core.agent.workflow import FunctionAgent


class EnterpriseQueryRouter:

    def __init__(
        self,
        llm,
        tools
    ):

        self.agent = FunctionAgent(
            tools=tools,
            llm=llm,
            system_prompt="""
You are an enterprise document intelligence query router.

Your job is to answer user questions using the
most appropriate document retrieval tool.

Routing rules:

1. Use vector_search for:
   - specific facts
   - concepts
   - semantic questions
   - questions about particular information

2. Use tree_search for:
   - document summaries
   - chapter-level questions
   - section-level questions
   - questions about overall document structure

Always use the available tools instead of
inventing information.

Provide concise answers and rely only on
retrieved document information.
"""
        )

    async def query(self, question):

        response = await self.agent.run(
            user_msg=question
        )

        return response