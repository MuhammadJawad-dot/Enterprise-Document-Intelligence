from llama_index.core.agent.workflow import FunctionAgent


class QueryPlanner:

    def __init__(self, llm, tools):

        self.agent = FunctionAgent(
            tools=tools,
            llm=llm,
            # verbose=True,
            system_prompt="""
You are an enterprise document query planner.

For simple questions:
- Use the most appropriate retrieval tool directly.

For complex questions:
- Break the question into logical sub-questions.
- Retrieve the required information.
- Combine the retrieved information.
- Produce a final answer based only on the documents.

Never invent missing information.
"""
        )

    async def run(self, question):

        response = await self.agent.run(
            user_msg=question
        )

        return response