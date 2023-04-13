import pandas as pd

official_chart = pd.DataFrame(columns=['POS', 'title', 'artist', 'year', 'HIGH POSN'])

# URL of the website containing the table
url = 'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/'

tables = pd.read_html(url)

album_table = tables[0]
for index, row in album_table.iterrows():
    pos = row['POS']
    title = row['TITLE']
    artist = row['ARTIST']
    year = row['YEAR']
    high_posn = row['HIGH POSN']
    official_chart = official_chart.append({'POS': pos, 'title': title, 'artist': artist, 'year': year, 'HIGH POSN': high_posn}, ignore_index=True)

# display the DataFrame
print(official_chart)


# rename the column names for pl
official_chart = official_chart.rename(columns={'title': 'TYTUŁ', 'artist': 'ARTYSTA', 'year': 'ROK', 'HIGH POSN': 'MAX POZ'})

# script to count single artists

artist_counts = official_chart['ARTYSTA'].value_counts()
unique_artists = artist_counts[artist_counts == 1].index.tolist()

print(f'The following artists appear only once in the table: {unique_artists}')

#script to find most common artist
most_common_artist = official_chart['ARTYSTA'].mode()[0]'

#change column headers to have capital letter
def rename_columns(dataframe):
    # create a dictionary to map the old column names to the new column names
    column_mapping = {col: col.capitalize() for col in dataframe.columns}
    # rename the columns in the DataFrame using the mapping dictionary
    dataframe = dataframe.rename(columns=column_mapping)
    return dataframe

#removing column
# remove the "Max Poz" column from the DataFrame
official_chart = official_chart.drop(columns=['Max Poz'])

# which year is most frequent?
year_counts = official_chart['Year'].value_counts()

most_common_year = year_counts.index[0]

print("The year that appears most frequently on the list is:", most_common_year)

#count albums between 1960 and 1990

# select the rows with years between 1960 and 1990 (inclusive)
year_range = official_chart.loc[(official_chart['Year'] >= 1960) & (official_chart['Year'] <= 1990)]
num_positions = len(year_range)
print("The number of positions between 1960 and 1990 is:", num_positions)

#najmlodzsy album
# find the record with the most recent year to date
most_recent_record = official_chart.loc[official_chart['Year'].idxmax()]
print("The record with the most recent year to date is:")
print(most_recent_record)

#najstarszy album per artysta


# create a new DataFrame to store the oldest albums
oldest_albums = pd.DataFrame(columns=official_chart.columns)

# group the records by artist and find the oldest album for each artist and csv export
for artist, group in official_chart.groupby('Artist'):
    oldest_album = group.loc[group['Year'].idxmin()]
    oldest_albums = oldest_albums.append(oldest_album)

# display the result
print("The oldest album of each artist is:")
print(oldest_albums)

# export the result to a CSV file
oldest_albums.to_csv('oldest_albums.csv')