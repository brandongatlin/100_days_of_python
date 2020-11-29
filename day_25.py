import pandas as pd
import csv
import time

start = time.time()
# df = pd.read_csv('squirrel_data.csv') 0.03495192527770996
# fur_col = df['Primary Fur Color'].dropna()
# furs = pd.unique(fur_col)

# formatted = []

# for fur in furs:
#   count = fur_col.where(fur_col == fur).count()
#   formatted.append([fur, count])
  
# formatted_df = pd.DataFrame(formatted)
# formatted_df.to_csv('squirrel_summary.csv')

df = pd.read_csv('squirrel_data.csv')

# grays = df[df['Primary Fur Color'] == 'Gray']
grays = len(df[df["Primary Fur Color"] == "Gray"])
reds = len(df[df['Primary Fur Color'] == 'Cinnamon'])
blacks = len(df[df['Primary Fur Color'] == 'Black'])

df = pd.DataFrame([['Gray', grays], ['Cinnamon', reds],['Black', blacks] ])
# print(df)
df.to_csv('squirrel_summary2.csv')


print(time.time() - start)
