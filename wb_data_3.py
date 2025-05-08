import plotly.express as px
import wbgapi as wb
import difflib
import pandas as pd
# Ask the user for a keyword to search for indicators
search_keyword = str(input('What keyword are you interested in looking for in indicators?: '))
search_keyword_2 = str(input('What keyword are you interested in looking for in the second indicators?: '))

# List all available indicators
indicators_list = []
indicators_list_2 = []
df = []
df_2 = []
chosen_indicator = ' '
chosen_indicator_2 = ' '

def indicators(x,y):
    global chosen_indicator
    global chosen_indicator_2
    choice = 1
    choice_2 = 1
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

    # Loop and print second indicators matching the keyword
    for y in wb.series.list():
        id_title_2 = y['id']
        indicator_name_2 = y['value'] 

        if search_keyword_2.lower() in indicator_name_2.lower():
            print(f"{choice_2}: {id_title_2} - {indicator_name_2}")
            choice_2 += 1
            indicators_list_2.append(y)
    selection_2 = int(input('\nEnter the number of the second indicator you want to use: ')) - 1
    chosen_indicator_2 = indicators_list_2[selection_2]['id']


indicators(search_keyword,search_keyword_2)

df = wb.data.DataFrame(chosen_indicator)
df_2 = wb.data.DataFrame(chosen_indicator_2)

print(df.head())
print(df_2.head())

