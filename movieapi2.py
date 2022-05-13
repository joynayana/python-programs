from omdbapi.movie_search import GetMovie as g
m=g(api_key='6c09a907')

print('----MOVIE DETAILS-----')
name=input("enter a movie name you want:")
a=m.get_movie(title=name,plot='full')
print(a)

b=m.get_data('actors')
print('\n Actors Details')
print('\n',b)
    

c=m.get_data('plot')
print('\n complete story')
print('\n',c)

