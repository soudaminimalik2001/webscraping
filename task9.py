import os
import random
import time
import requests
import json
from task1 import movie_data
from task4 import scrape_movie_details

def get_movie_list_details(movie):
    movie_list=[]
    for i in movie[:10]:
        path="/home/dell32/Desktop/Task9/task99"+i["movieName"]+".json"
        random_sleep=random.randint(1,3)
        if os.path.exists("file.json"):
            pass
        else:
            with open(path,"w")as f1:
                url=requests.get(i["moviceurl"])
                f1.write(url.text)
                time.sleep(random_sleep)
get_movie_list_details( movie_data)

#task9