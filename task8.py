from task1 import movie_data
import json
import os
import requests
# t1=movie_data()
with open("task1.json","r+")as file:
    a=json.load(file)
def text(detail):
    for i in detail:
        path="/home/dell32/Desktop/task8/task88"+i["movieName"]+".text"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w")as f:
                url=requests.get(i["moviceurl"])
                f.write(url.text)
text(a)

#task8