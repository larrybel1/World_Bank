import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import wbgapi as wb
import difflib

# Function made to look for the country code
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
selection = int(input('\nEnter the number of the indicator you want to use: ')) - 1
chosen_indicator = indicators_list[selection]['id']
# print(chosen_indicator)
country_pick = input('Pick a country you would like to take a look at: ')
country_pick2 = input('Pick a second country you would like to take a look at: ')
country_code = get_country_code(country_pick)
country_code2 = get_country_code(country_pick2)
# print(country_code)

# This piece looks for the country to be spelt correctly 
if not country_code:
    print('Country could not be found, please try again with different spelling: ')
else:
    df = wb.data.DataFrame(chosen_indicator, economy= [country_code, country_code2])#.reset_index()#, time=range(2000, 2024))


# print(df)
flipped_df = df.transpose().reset_index()#.melt()
#nprint(flipped_df)
flipped_df.columns = ['Years', country_pick, country_pick2]
# print(flipped_df)
fig = px.line(
    flipped_df,
    x = 'Years',                  # x-axis: years
    y = [country_pick, country_pick2],           # y-axis: the indicator (3rd column = renamed indicator name)
    title = f"{search_keyword} in {country_pick.title()} and {country_pick2.title()} over the {flipped_df.columns[0]}s",
    markers = True,
    color_discrete_map = {country_pick: 'blue', country_pick2: 'green'},
     labels={
        'Year': 'Time (Years)',      # Custom x-axis label
        'value': f'{search_keyword}',       # y-axis label if you're using long-form data
        'variable': 'Countries'        # shown in legend for wide-form data
    }
)

fig.show()