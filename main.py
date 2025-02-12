import requests
import os
from Send_email import info
topic = "tesla"
api_key = os.getenv ( "API_KEY" )
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-01-12&"
       "sortBy=publishedAt&apiKey=03e88b7b46114e15902f9e22433977f4&"
       "language=en")

request = requests.get ( url )
content = request.json ()
message = ""
for article in content["articles"][:20] :
    title = article["title"]
    description = article["description"]
    link = article["url"]
    message += f"""
TITLE:  {title}
DESCRIPTION:  {description}
URL LINK: {link}\n\n"""
message=f"""Subject: Daily News
{message}"""
message = message.encode ( "utf-8" )
info ( message )
