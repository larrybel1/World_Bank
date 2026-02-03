import plotly.express as px
import difflib
import pandas as pd
import plotly as plt 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("WDI_data.xlsx")
### Viewing the first 10 rows & Columns to get an idea of what the dataset looks like
# print(df.iloc[0:10, 0:10])

### Making a new df without the following columns, keeping the pervious df becasue it still has important
column_to_drop = ["Country Code", "Series Code"]
df_simple = df.drop(columns = column_to_drop)

### Trying to rename the year rows to just have the year 
# df_simple.columns.values[2:] = [c.split("_"[0]) for c in df_simple.columns.values[2:]]
### Managed to rename the columns to have just the years
df_simple = df_simple.replace(['..'], "NaN")
df_simple.columns.values[2:] = [''.join(filter(str.isdigit, c)) for c in df_simple.columns.values[2:]]
df_simple.columns.values[2:] = df_simple.columns.values[2:].astype(int) // 10000
af_data = df_simple.loc[df_simple['Country Name'] == 'Afghanistan']

### Checking new df
#print(df_simple.iloc[0:10 , 0:10])
print(af_data)



# ### Now trying to create a simple graph for the first row
# print(df_simple.iloc[0])
# years = df_simple.columns.values[2:]
# rowone = df_simple.iloc[1]#.reset_index()
# rowdata = rowone[2:].reset_index()
# rowdata = rowdata.iloc[0:, 1].astype(float).to_numpy()
# print(type(rowdata))
# print(type(years))
# print(np.size(rowdata))
# print(np.size(years))

# # print(rowdata)
# plt.scatter(years, rowdata)
# # plt.xlabel('Years')
# # plt.ylabel('GDP Growth (annual %)')

# # plt.figure(figsize=(8,5))
# # rowdata.plot()
# # plt.xlabel('Years')
# # plt.ylabel('GDP Growth (annual %)')

# plt.show()