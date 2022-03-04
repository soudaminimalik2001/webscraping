import json
import requests
from bs4 import BeautifulStoneSoup
with open("task5.json","r+")as file:
    data2=json.load(file)
def analyse_movies_directors(data2):
    di1={}
    for i in data2:
        if "Director" in i:
            Director=i["Director"]
            for i in Director:
                if i not in di1:
                    di1[i]=1
                else:
                    di1[i]+=1
    print(di1)
    with open("task7.json","w+") as file1:
        json.dump(di1,file1,indent = 4)
analyse_movies_directors(data2)
                       