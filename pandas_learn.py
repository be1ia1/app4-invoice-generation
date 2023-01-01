import pandas as pd

df = pd.read_excel('invoices/10001-2023.1.18.xlsx')
empty_cell = df.shape[1] - 1
total_row = ['' for x in range(empty_cell)]
total_row.append(df['total_price'].sum())
df.loc[len(df.index)] = total_row
print(df.columns.values)
# print(df.loc[0,:])