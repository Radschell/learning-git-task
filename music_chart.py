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
