class StructuredQueryEngine:

    def __init__(self, dataframe):

        self.df = dataframe

    def get_revenue(self, year):

        row = self.df[
            self.df["Year"] == year
        ]

        if row.empty:
            return None

        return row.iloc[0]["Revenue_USD_M"]

    def get_profit(self, year):

        row = self.df[
            self.df["Year"] == year
        ]

        if row.empty:
            return None

        return row.iloc[0]["Profit_USD_M"]

    def compare_revenue(self, year1, year2):

        revenue1 = self.get_revenue(year1)
        revenue2 = self.get_revenue(year2)

        if revenue1 is None or revenue2 is None:
            return None

        difference = revenue2 - revenue1

        percentage = (
            difference / revenue1
        ) * 100

        return {
            "year1": year1,
            "year2": year2,
            "revenue1": revenue1,
            "revenue2": revenue2,
            "difference": difference,
            "percentage_change": percentage
        }