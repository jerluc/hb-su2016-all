movies_list = []
from urllib2 import *
from json import *
def movies():
    global movies_list
    movie_list2 = []
    response = urlopen('https://data.sfgov.org/resource/wwmu-gmzc.json')                                     
    json_obj=load(response)
    for i in range(len(json_obj)):
        movie = json_obj[i]
        #Adds movie to movie_list2
        movie_list2.append(movie)
    #Set movies_list to movie_list2
    movies_list = movie_list2




movies_list3 = []
def find_movies():
    string = raw_input("What name do you want?: ")

    for i3 in range (len (movies_list )):
        name = movies_list[i3]['director']
        if (name == string ):
            if movies_list[i3]['title'] in movies_list3:
                continue
            else:
                #Adds movie to movies_list3
                movies_list3.append(movies_list[i3]['title'])
        else:
            if (name.lower() == string.lower()):
                if movies_list[i3]['title'] in movies_list3:
                    continue
                else:
                    #Adds movie to movies_list3
                    movies_list3.append(movies_list[i3]['title'])

    for i4 in range(len(movies_list3)):
        movie2 = movies_list3[i4]
        print(movie2)





