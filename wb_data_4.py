import plotly.express as px
import difflib
import pandas as pd
import plotly as plt 
import matplotlib.pyplot as plt

df = pd.read_excel("WDI_data.xlsx")
### Viewing the first 10 rows & Columns to get an idea of what the dataset looks like
# print(df.iloc[0:10, 0:10])

### Making a new df without the following columns, keeping the pervious df becasue it still has important
column_to_drop = ["Country Code", "Series Code"]
df_simple = df.drop(columns = column_to_drop)

### Trying to rename the year rows to just have the year 
# df_simple.columns.values[2:] = [c.split("_"[0]) for c in df_simple.columns.values[2:]]
### Managed to rename the columns to have just the years
df_simple.columns.values[2:] = [''.join(filter(str.isdigit, c)) for c in df_simple.columns.values[2:]]
df_simple.columns.values[2:] = df_simple.columns.values[2:].astype(int) // 10000

### Checking new df
#   print(df_simple.iloc[0:10 , 0:10])
# print(df_simple.columns.values[2:])

### Now trying to create a simple graph for the first row
# print(df_simple.iloc[0])
df_simple.iloc[1].plot()
plt.show()