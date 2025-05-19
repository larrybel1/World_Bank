import plotly.express as px
import wbgapi as wb
import difflib
import pandas as pd
import plotly as plt 
# Ask the user for a keyword to search for indicators
search_keyword = str(input('What keyword are you interested in looking for in indicators?: '))
search_keyword_2 = str(input('What keyword are you interested in looking for in the second indicators?: '))

# Sets the Global chosen indicators so that they can be called outside the function
chosen_indicator = ' '
chosen_indicator_2 = ' '

def indicators(x,y):
    # Calls the global variables into the function
    global chosen_indicator
    global chosen_indicator_2
    # sets the counters 
    choice = 1
    choice_2 = 1
    # Sets the lists for the indicators matching the keywords
    indicators_list = []
    indicators_list_2 = []
    # Loop and print indicators matching the keyword
    for x in wb.series.list():
        id_title = x['id']
        indicator_name = x['value']

        if search_keyword.lower() in indicator_name.lower():
            print(f"{choice}: {id_title} - {indicator_name}")
            choice += 1
            indicators_list.append(x)
    selection = int(input('\nEnter the number of the indicator you want to use: ')) - 1
    chosen_indicator = indicators_list[selection]['id']

    # Loop and print indicators matching the second keyword
    for y in wb.series.list():
        id_title_2 = y['id']
        indicator_name_2 = y['value'] 

        if search_keyword_2.lower() in indicator_name_2.lower():
            print(f"{choice_2}: {id_title_2} - {indicator_name_2}")
            choice_2 += 1
            indicators_list_2.append(y)
    selection_2 = int(input('\nEnter the number of the second indicator you want to use: ')) - 1
    chosen_indicator_2 = indicators_list_2[selection_2]['id']


# Starts the function using the keywords chosen at the top of the code
indicators(search_keyword,search_keyword_2)

# Modifies and sets the data frames 

df = wb.data.DataFrame(chosen_indicator)
df_2 = wb.data.DataFrame(chosen_indicator_2)

# I honestly thing that using two different dfs would make it easier to graph and draw comparisons between them
df_long = df.reset_index().melt(id_vars = 'economy', var_name = 'Year', value_name = chosen_indicator)
print(df_long)
df_2_long = df_2.reset_index().melt(id_vars = 'economy', var_name = 'Year', value_name = chosen_indicator_2)
print(df_2_long)
df_merge = pd.merge(df_long, df_2_long, on = ['economy','Year'])
print(df_merge.iloc[:15,:])

# plt.plot(df, usa_pop, label='USA Population', marker='o')
# plt.plot(years, usa_co2, label='USA CO₂ Emissions', marker='x')

# plt.title('USA Population vs CO₂ Emissions')
# plt.xlabel('Year')
# plt.legend()
# plt.show()