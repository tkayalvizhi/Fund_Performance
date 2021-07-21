import pandas as pd
import json

file = 'Resources/icici_fund_performance.xlsx'

df = pd.read_excel(file, 'Sheet1')

fund_names = df.columns
df = df.set_index('Date')
print(df)

with open(r'Resources/current_investment.json', 'r') as cur_investment:
    cur_investment_dict: dict = json.load(cur_investment)

my_investment = pd.DataFrame(cur_investment_dict)
my_investment = my_investment.set_index('Date')

my_investment.to_excel(file, 'Sheet2', index_label='Date')

# print(my_investment.loc['July 19, 2021'].multiply(df.loc['July 19, 2021'], axis='index'))
