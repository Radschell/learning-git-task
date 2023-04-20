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