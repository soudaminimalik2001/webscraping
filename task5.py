import json
from task1 import movie_data
from task4 import scrape_movie_details
with open("task1.json","r")as file:
    data=json.load(file)
def get_movie_details_list():
    list1=[]
    for i in data:
        k=i["moviceurl"]
        a=scrape_movie_details(k)
        list1.append(a)
    with open("task5.json","w+") as file:
        json.dump(list1,file,indent = 4)
    return list1
get_movie_details_list()