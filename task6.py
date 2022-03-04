import json
import requests
from bs4 import BeautifulStoneSoup
with open("task5.json","r+")as file:
    data1=json.load(file)
def analyse_movies_language(data1):
    di={}
    for i in data1:
        if "Language" in i:
            Language=i["Language"]
            for i in Language:
                if i not in di:
                    di[i]=1
                else:
                    di[i]+=1
    print(di)
    with open("task6.json","w+") as file1:
        json.dump(di,file1,indent = 4)
analyse_movies_language(data1)
                    
#task6          