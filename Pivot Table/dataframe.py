import pandas as pd

data = {
    "Sn": ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 "],
    "Person": ["a", "b", "c", "d", "e", "f", "g"],
    "Sales": [1500, 1000, 300, 400, 500, 800, 700],
    "Quarter": [1, 1, 1, 1, 1, 2, 2],
    "Country": ["US", "Japan", "Brazil", "UK", "US", "Japan", "US"],
}

df = pd.DataFrame(data)

# Total sale per Person
total_sale_per_person = df.groupby("Person")["Sales"].sum().reset_index()
print(total_sale_per_person)

# Total sale per country
total_sale_per_country = df.groupby("Country")["Sales"].sum().reset_index()
print(total_sale_per_country)

# Mean medium and maximum sale by country

stats_sale_by_country = (
    df.groupby("Country")["Sales"].agg(["mean", "median", "min", "max"]).reset_index()
)
print(stats_sale_by_country)
