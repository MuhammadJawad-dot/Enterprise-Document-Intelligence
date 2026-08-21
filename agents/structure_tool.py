from llama_index.core.tools import FunctionTool


def get_revenue(data_engine, year: int):

    return data_engine.get_revenue(year)


def get_profit(data_engine, year: int):

    return data_engine.get_profit(year)


def compare_revenue(
    data_engine,
    year1: int,
    year2: int
):

    return data_engine.compare_revenue(
        year1,
        year2
    )


def create_structured_tools(data_engine):

    revenue_tool = FunctionTool.from_defaults(
        fn=lambda year: get_revenue(
            data_engine,
            year
        ),
        name="get_revenue",
        description=(
            "Get the revenue for a specific year "
            "from the financial table."
        )
    )

    profit_tool = FunctionTool.from_defaults(
        fn=lambda year: get_profit(
            data_engine,
            year
        ),
        name="get_profit",
        description=(
            "Get the profit for a specific year "
            "from the financial table."
        )
    )

    comparison_tool = FunctionTool.from_defaults(
        fn=lambda year1, year2: compare_revenue(
            data_engine,
            year1,
            year2
        ),
        name="compare_revenue",
        description=(
            "Compare revenue between two years and "
            "calculate the percentage change."
        )
    )

    return [
        revenue_tool,
        profit_tool,
        comparison_tool
    ]