

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