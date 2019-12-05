import requests
import json
import pytest

url = "https://swapi.co/api/people/"

payload = ""
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "6e290516-c612-41a5-8574-147998735d24,f0936e07-07a8-4cc9-b4f7-b88b63800614",
    'Host': "swapi.co",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "__cfduid=d219445e6c2d500ebd4b26ef499b7f10a1573830513",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)


data = response.json()
data_heroes = data["results"]
heroes = []
for i in range(len(data_heroes)):
    heroes.append(data_heroes[i]["name"])
for i in heroes:
    print(i)