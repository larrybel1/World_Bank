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
### The line right below takes the .. and can turn them into NaN or 0, depending on what we are looking to do with the data
### For certain countries, we cant use any of the data in certain column becasue there isnt enough togo off of 
df_simple = df_simple.replace(['..'], 0)

### Renames the columns to just contain the Year and nothing else
df_simple.columns.values[2:] = [''.join(filter(str.isdigit, c)) for c in df_simple.columns.values[2:]]
df_simple.columns.values[2:] = df_simple.columns.values[2:].astype(int) // 10000
### Pick a country to take a look at, in this case we are looking at Afganistan
country_data = df_simple.loc[df_simple['Country Name'] == 'Afghanistan']
### Dropping all rows containing all NaNs or 0s 
country_data = country_data.dropna(how = 'all').drop(columns = 'Country Name').set_index(country_data.columns[1])
country_data = country_data#.set_index(country_data.columns[0])
### Trying to get the averages for all the rows
#averages = country_data.iloc[2:].mean()






### Checking new df
print(country_data)#.info())
#print(averages)




















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