import json
import requests
from bs4 import BeautifulSoup
from task4 import scrape_movie_details
from task12 import movie_actor_details 
Url = "https://www.rottentomatoes.com/m/coco_2017"
def final_movie(url1):
    list=[]
    task4= scrape_movie_details(url1)
    task12= movie_actor_details(url1)
    task4["cast"]=task12
    list.append(task4)
    with open("task13.json","w+") as file1:
        json.dump(list,file1,indent = 4)
        print(list)
final_movie(Url)

#task13