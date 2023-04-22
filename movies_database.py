

import pandas as pd

# create an empty dataframe with column names
tmdb_genres = pd.DataFrame(columns=['genre_id', 'genres'])

# create a new dataframe with the specified columns and name it tmdb_movies
tmdb_movies = pd.DataFrame(columns=['order', 'budget', 'homepage', 'id', 'original_language', 'original_title', 'overview', 'popularity', 'release_date', 'revenue', 'runtime', 'status', 'tagline', 'title', 'vote_average', 'vote_count', 'genre_id'])

# read the CSV file into a new dataframe
new_data = pd.read_csv('/content/tmdb_genres.csv')

# append the new data to the existing dataframe
tmdb_genres = tmdb_genres.append(new_data, ignore_index=True)

# read the CSV file into a new dataframe
new_data2 = pd.read_csv('/content/tmdb_movies.csv')

# append the new data to the existing dataframe
tmdb_movies = tmdb_movies.append(new_data2, ignore_index=True)

# print the first 5 rows of the dataframe
print(tmdb_genres.head())
print(tmdb_movies.head())

#TASK 1

# calculate the 3rd quartile of vote_count
vote_count_3rd_quartile = tmdb_movies['vote_count'].quantile(0.75)

# filter the movies with vote_count greater than the 3rd quartile
filtered_movies = tmdb_movies[tmdb_movies['vote_count'] > vote_count_3rd_quartile]

# sort the filtered movies by vote_average in descending order and select the top 10
top_10_movies = filtered_movies.sort_values('vote_average', ascending=False).head(10)

# print the top 10 movies
print('Top 10 movies with vote count > 3rd quartile:')
print(top_10_movies[['title', 'vote_count', 'vote_average']])

#Task 2

# convert release_date column to datetime format
tmdb_movies['release_date'] = pd.to_datetime(tmdb_movies['release_date'])

# filter the movies released from 2010 to 2016
filtered_movies = tmdb_movies[(tmdb_movies['release_date'].dt.year >= 2010) & (tmdb_movies['release_date'].dt.year <= 2016)]

# group the filtered movies by year and calculate the average revenue and budget
grouped_movies = filtered_movies.groupby(filtered_movies['release_date'].dt.year)[['revenue', 'budget']].mean()

# print the grouped movies
print(grouped_movies)

import pandas as pd

# create an empty dataframe with column names
tmdb_genres = pd.DataFrame(columns=['genre_id', 'genres'])

# create a new dataframe with the specified columns and name it tmdb_movies
tmdb_movies = pd.DataFrame(columns=['order', 'budget', 'homepage', 'id', 'original_language', 'original_title', 'overview', 'popularity', 'release_date', 'revenue', 'runtime', 'status', 'tagline', 'title', 'vote_average', 'vote_count', 'genre_id'])

# read the CSV file into a new dataframe
new_data = pd.read_csv('/content/tmdb_genres.csv')

# append the new data to the existing dataframe
tmdb_genres = tmdb_genres.append(new_data, ignore_index=True)

# read the CSV file into a new dataframe
new_data2 = pd.read_csv('/content/tmdb_movies.csv')

# append the new data to the existing dataframe
tmdb_movies = tmdb_movies.append(new_data2, ignore_index=True)

# print the first 5 rows of the dataframe
print(tmdb_genres.head())
print(tmdb_movies.head())

# calculate the 3rd quartile of vote_count
vote_count_3rd_quartile = tmdb_movies['vote_count'].quantile(0.75)

# filter the movies with vote_count greater than the 3rd quartile
filtered_movies = tmdb_movies[tmdb_movies['vote_count'] > vote_count_3rd_quartile]

# sort the filtered movies by vote_average in descending order and select the top 10
top_10_movies = filtered_movies.sort_values('vote_average', ascending=False).head(10)

# print the top 10 movies
print('Top 10 movies with vote count > 3rd quartile:')
print(top_10_movies[['title', 'vote_count', 'vote_average']])

# convert release_date column to datetime format
tmdb_movies['release_date'] = pd.to_datetime(tmdb_movies['release_date'])

# filter the movies released from 2010 to 2016
filtered_movies = tmdb_movies[(tmdb_movies['release_date'].dt.year >= 2010) & (tmdb_movies['release_date'].dt.year <= 2016)]

# group the filtered movies by year and calculate the average revenue and budget
grouped_movies = filtered_movies.groupby(filtered_movies['release_date'].dt.year)[['revenue', 'budget']].mean()

# print the grouped movies
print(grouped_movies)

import matplotlib.pyplot as plt

# convert release_date column to datetime format
tmdb_movies['release_date'] = pd.to_datetime(tmdb_movies['release_date'])

# filter the movies released from 2010 to 2016
filtered_movies = tmdb_movies[(tmdb_movies['release_date'].dt.year >= 2010) & (tmdb_movies['release_date'].dt.year <= 2016)]

# group the filtered movies by year and calculate the average revenue and budget
grouped_movies = filtered_movies.groupby(filtered_movies['release_date'].dt.year)[['revenue', 'budget']].mean()

# create a figure and axis object
fig, ax = plt.subplots()

# plot the average revenue as a column chart
ax.bar(grouped_movies.index, grouped_movies['revenue'], color='b', alpha=0.5, label='Average Revenue')

# plot the average budget as a line chart
ax.plot(grouped_movies.index, grouped_movies['budget'], color='r', alpha=0.7, label='Average Budget')

# set the x-axis label and tick labels
ax.set_xlabel('Year')
ax.set_xticks(grouped_movies.index)
ax.set_xticklabels(grouped_movies.index)

# set the y-axis label and tick labels
ax.set_ylabel('Amount in USD (Millions)')
ax.set_yticklabels(['{:,.0f}'.format(x/1000000) for x in ax.get_yticks()])

# set the chart title
ax.set_title('Average Revenue and Budget per Year (2010 - 2016)')

# add a legend to the upper right corner of the canvas, outside the axis area
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

# display the chart
plt.show()
