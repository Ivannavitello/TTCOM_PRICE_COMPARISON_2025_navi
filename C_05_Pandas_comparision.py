import pandas
from tabulate import tabulate


# These are the column for the display in the end
every_item = ["white rice", "Brown Rice", "jasmine rice", "Sushi Rice", "Eggs"]
Item_amount = [0, 0, 0, 0, 12]
unit_per_grams_Ml = [15000, 10000, 12000, 5000, 0]
unit_per_kg_liters =[15, 10, 12, 5, 0]
price_per_item = [25, 30, 28, 17, 15]
unit_price_kg_lites = [25 / 15, 7.50 / 10, 10.50 / 12, 10.50 / 5, 0]
amount_price_cost = [0,0,0,0,1.25]

# Listing by rows
item_lists = {
    'Item': every_item,
    'Item amount': Item_amount,
    'Unit of item (grams/ml)' : unit_per_grams_Ml,
    'Unit of item (kg/liter)': unit_per_kg_liters,
    'Price per item': price_per_item,
    'Amount cost': amount_price_cost,
    ' Unit Price': unit_price_kg_lites
}
# create dataframe / table from dictionary
item_lists = pandas.DataFrame(item_lists)
print(tabulate(item_lists, headers='keys', tablefmt='psql', showindex=False))
print()


