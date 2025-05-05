import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import wbgapi as wb
import difflib

# This part of the code looks for the 3 letter country code using the counrty name the user use 
def get_country_code(country_name):
    country_name = country_name.strip().lower()
    countries = {c['value'].lower(): c['id'] for c in wb.economy.list()}
    
    if country_name in countries:
        return countries[country_name]
    # Use closest match if no exact match
    closest = difflib.get_close_matches(country_name, countries.keys(), n=1)
    if closest:
        return countries[closest[0]]
    else:
        return None


# Ask the user for a keyword to search for indicators
search_keyword = str(input('What keyword are you interested in looking for in indicators?: '))

# List all available indicators
indicators_list = []
df = []

# Initialize counter
choice = 1
# Loop and print indicators matching the keyword
for indicator in wb.series.list():
    id_title = indicator['id']
    indicator_name = indicator['value']  # ← Fix is here!

    if search_keyword.lower() in indicator_name.lower():
        print(f"{choice}: {id_title} - {indicator_name}")
        choice += 1
        indicators_list.append(indicator)
        
# Allows the user to look at all the indicators that has their keyword and allows them to pick it via a number
selection = int(input('\nEnter the number of the indicator you want to use: ')) - 1
chosen_indicator = indicators_list[selection]['id']
# print(chosen_indicator)


# Asks the user to pick a country 
country_pick = input('Pick a country you would like to take a look at: ')
country_code = get_country_code(country_pick)
# print(country_code)

# If the user missspelled the name of a country or the system cant find it, 
# this allows them to type it in again without having to run the script again
if not country_code:
    print('Country could not be found, please try again with different spelling: ')
else:
    df = wb.data.DataFrame(chosen_indicator, economy=country_code)#, time=range(2000, 2024))
    
# print(df)
flipped_df = df.transpose().reset_index()
# print(flipped_df)
flipped_df.columns = ['Year', 'GDP']
# print(flipped_df)
fig = px.line(
    flipped_df,
    x ='Year',                  # x-axis: years
    y = flipped_df.columns[1],           # y-axis: the indicator (3rd column = renamed indicator name)
    title = f"{flipped_df.columns[1]} in {country_pick.title()} over the {flipped_df.columns[0]}s",
    markers = True
)

fig.show()