import requests
from send_email import send_email


topic = "tesla"
api_key = "8f59d8ae7cd7496898ab680297fa6f0e"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-21&sortBy=publishedAt&apiKey=8f59d8ae7cd7496898ab680297fa6f0e&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the articles titles and description
for article in content["articles"][:20]:
    body = "Subject: Today's news" \
            + "\n" + body + article["title"] + "\n" \
            + article["description"] \
            + "\n" + article["url"] + 2*"\n"


body = body.encode('utf-8')
send_email(body)
