import requests
import os

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=03e88b7b46114e15902f9e22433977f4"

request = requests.get(url)
content= request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])
