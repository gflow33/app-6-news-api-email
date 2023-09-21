import requests

api_key = "8f59d8ae7cd7496898ab680297fa6f0e"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-21&sortBy=publishedAt&apiKey=8f59d8ae7cd7496898ab680297fa6f0e"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
