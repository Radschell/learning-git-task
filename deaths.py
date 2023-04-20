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
