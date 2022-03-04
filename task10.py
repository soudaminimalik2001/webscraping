from bs4 import BeautifulSoup
import requests
import json
from task1 import movie_data
from task4 import scrape_movie_details
from task5 import get_movie_details_list
from task8 import text
from task9 import get_movie_list_details

def analyse_language_and_directors(movies_list):
    directors_dic={}
    for movie in movies_list:
        for director in movie['director']:
            directors_dic[director]={}
    for i in range(len(movies_list)):
        for director in directors_dic:
            if director in movies_list[i]['director']:
                for language in movies_list[i]['language']:
                    directors_dic[director][language]=0
    for i in range(len(movies_list)):
        for director in directors_dic:
            if director in movies_list[i]['director']:
                for language in movies_list[i]['language']:
                    directors_dic[director][language]+=1
    # print(directors_dic)
    with open("task10.json","w+") as f:
        json.dump(directors_dic,f,indent = 4)
        return directors_dic
analyse_language_and_directors(get_movie_details_list)
                
                        
#task10

    