import json
import requests
from bs4 import BeautifulStoneSoup
with open("task5.json","r+")as file:
    data2=json.load(file)
def analyse_movies_gener(data2):
    gener_list={}
    for i in data2:
        if "Genre" in i:
            Genre=i["Genre"]
            for i in Genre:
                if i not in gener_list:
                    gener_list[i]=1
                else:
                    gener_list[i]+=1
    print(gener_list)
    with open("task11.json","w+") as file1:
        json.dump(gener_list,file1,indent = 4)
analyse_movies_gener(data2)

#task11