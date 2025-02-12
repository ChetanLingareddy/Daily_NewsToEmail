import requests
import os
from Send_email import info

# url and api key from newsapi.org
topic = "tesla"
api_key = os.getenv ( "API_KEY" ) # key  value stored locally
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-01-12&"
       "sortBy=publishedAt&apiKey=03e88b7b46114e15902f9e22433977f4&"
       "language=en")

# sends a request to the given url and waits for the response and stores its value in request variable.
request = requests.get ( url )
# Stores the content of the data from the link
content = request.json ()

message = ""

# Retrieves its data(title,description,link) and stores its values
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

#converts strings to bytes to safely send to email or http protocols
message = message.encode ( "utf-8" )
# send data to below line where it is utilized for email function
info ( message )
