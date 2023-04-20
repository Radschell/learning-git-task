import pandas as pd

data = {
    'id': pd.Int64Dtype(), # integer values
    'name': 'string', # string values
    'date': 'string', # string values
    'manner_of_death': 'string', # string values
    'armed': 'string', # string values
    'age': pd.Int64Dtype(), # integer values
    'gender': 'string', # string values
    'race': 'string', # string values
    'city': 'string', # string values
    'state': 'string', # string values
    'signs_of_mental_illness': 'boolean', # boolean values
    'threat_level': 'string', # string values
    'flee': 'string', # string values
    'body_camera': 'boolean' # boolean values
}

df = pd.DataFrame(columns=data.keys()).astype(data)

import pandas as pd


csv_path = 'C:/Users/HOME/Desktop/Kodilla/learning-git-task/fatal-police-shootings-data.csv'

# create an empty DataFrame with column names and data types specified
data = {
    'id': pd.Int64Dtype(), # integer values
    'name': 'string', # string values
    'date': 'string', # string values
    'manner_of_death': 'string', # string values
    'armed': 'string', # string values
    'age': pd.Int64Dtype(), # integer values
    'gender': 'string', # string values
    'race': 'string', # string values
    'city': 'string', # string values
    'state': 'string', # string values
    'signs_of_mental_illness': 'boolean', # boolean values
    'threat_level': 'string', # string values
    'flee': 'string', # string values
    'body_camera': 'boolean' # boolean values
}
df = pd.DataFrame(columns=data.keys()).astype(data)

# use read_csv function to import data from CSV file to DataFrame
df = pd.read_csv(csv_path, dtype=data)

# display the DataFrame
print(df.head())

# TASK 2. Adding function to count number of incidents per race
df = pd.read_csv(csv_path, dtype=data)

# group the records by race and count the number of records per race
race_counts = df.groupby('race').size().reset_index(name='counts')

# display the race counts DataFrame
print(race_counts)

# group the records by race and mental illness status and count the number of records in each group
race_and_mental_illness_counts = df.groupby(['race', 'signs_of_mental_illness']).size().reset_index(name='counts')

# display the race and mental illness counts DataFrame
print(race_and_mental_illness_counts)

# TASK 3. Adding function to count which race has highest number of mental illnes incidents 
# filter the DataFrame to include only records where signs_of_mental_illness is True
mental_illness_records = race_and_mental_illness_counts[race_and_mental_illness_counts['signs_of_mental_illness'] == True]

# get the race with the highest number of records where signs_of_mental_illness is True
race_with_most_mental_illness_records = mental_illness_records.loc[mental_illness_records['counts'].idxmax()]['race']

# print the race with the highest number of records where signs_of_mental_illness is True
print("The race with the highest number of records where signs_of_mental_illness is True is:", race_with_most_mental_illness_records)

#TASK4 adding column with days of the week

# use read_csv function to import data from CSV file to DataFrame
df = pd.read_csv(csv_path, dtype=data)

# convert the date column to a pandas datetime object
df['date'] = pd.to_datetime(df['date'])

# create a new column with the day of the week corresponding to the date column
df['day_of_week'] = df['date'].dt.day_name()

# print the first few rows of the updated DataFrame
print(df.head())

# group the DataFrame by day of the week and count the number of records in each group
records_per_day = df.groupby('day_of_week').size()

# print the resulting Series object containing the counts per day of the week
print(records_per_day)

import matplotlib.pyplot as plt

# create a bar chart with the counts per day of the week
records_per_day = records_per_day.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
records_per_day.plot(kind='bar')

# set the chart title and axes labels
plt.title('Number of Records per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Records')

# display the chart
plt.show()

#TASK 5 adding other databases

import pandas as pd

# replace the URLs with the actual URLs you want to scrape
url_population = 'https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population'
url_abbreviations = 'https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations'

# read HTML tables from the URLs
dfs_population = pd.read_html(url_population)
dfs_abbreviations = pd.read_html(url_abbreviations)

# extract the first table from the list of DataFrames
df_population = dfs_population[0]

# drop unnecessary columns
df_population.drop(['Rank', 'Percentage', 'Population density'], axis=1, inplace=True)

# rename columns to match the column names in your original DataFrame
df_population.rename(columns={'State': 'state', 'Population': 'population'}, inplace=True)

# convert the population column to integers
df_population['population'] = df_population['population'].str.replace(',', '').astype(int)

# set the state column as the index
df_population.set_index('state', inplace=True)

# extract the necessary columns from the abbreviations DataFrame
df_abbreviations = dfs_abbreviations[0][['United States postal abbreviations', 'ANSI']]

# rename columns to match the column names in your original DataFrame
df_abbreviations.rename(columns={'United States postal abbreviations': 'state'}, inplace=True)

# set the state column as the index
df_abbreviations.set_index('state', inplace=True)

# merge the two DataFrames based on the state column
df_merged = pd.merge(df_population, df_abbreviations, on='state')

# add the ANSI column to the original DataFrame
df_population['ANSI'] = df_merged['ANSI']

# display the resulting DataFrame
print(df_population.head())


import pandas as pd

# Load the HTML table from the URL into a list of DataFrames
dfs = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')

# Select the first DataFrame from the list, which contains the population data
df_population = dfs[0]

# Drop the unnecessary columns
df_population = df_population.drop(['Rank', '% of US', '−'], axis=1)

# Rename the columns to match the existing DataFrame
df_population = df_population.rename(columns={'State/Territory': 'state', 'Population estimate': 'population'})

# Merge the population data into the original DataFrame
df_merged = pd.merge(df_original, df_population, on='state', how='left')
