import random

class Movie:

   def __init__(self, title, year, genre, views):
       self.title = title
       self.year = year
       self.genre = genre
       self.views = views

   def __str__(self):
       return f'{self.title} {self.year} {self.genre} views:{self.views}'

   def play(self, step=1):
       self.views += step


class Series(Movie):
   def __init__(self, title, year, genre, views, episode_no, season_no):
       self.title = title
       self.year = year
       self.genre = genre
       self.views = views
       self.episode_no = episode_no
       self.season_no = season_no
     
   def play(self, step=1):
       self.views += step

movies_list = [
    Movie(title="avatar", year="2022", genre="sciencefiction", views=0),
    Movie(title="grantorino", year="2012", genre="drama", views=0),
    Movie(title="mustang", year="2002", genre="animation", views=0)
  
]

series1 = Series(title="Dexter", year="2022", genre="Thriller", views=0, episode_no=2, season_no=1)
series2 = Series(title="Witcher", year="2022", genre="Fantasy", views=0, episode_no=3, season_no=2)

movies_list.append(series1)
movies_list.append(series2)

print(movies_list[0])




def get_movies():
    for movie in movies_list:
        if isinstance(movie, Movie):
            print(movie)

def get_series():
    for series in movies_list:
        if isinstance(series, Series):
            print(series)

def search():
    title = input("Enter the title of the movie: ")
    for movie in movies_list:
        if movie.title == title:
            return movie
    return None


def generate_views():
    movie = random.choice(movies_list)
    random_views = random.randint(1,100)
    movie.views += random_views

def generate_views_ten_times():
    for i in range(10):
        generate_views()

def movie_views(movie):
    return movie.views

def top_titles():
    n = int(input("Enter the number of top movies to be returned: "))
    movies_list.sort(key=movie_views, reverse=True)
    for i in range(n):
        print(movies_list[i])


generate_views()
top_titles()

