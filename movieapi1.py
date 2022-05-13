import omdbapi
from omdbapi.movie_search import GetMovie
#key for omdbapi
m=GetMovie(api_key='6c09a907')
#get movie data as json format
a=m.get_movie(title='hridayam')
print(a)
b=m.get_data('actors','year')
print(b)
