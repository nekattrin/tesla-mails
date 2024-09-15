import requests
from new_send_emails import send_email

topic = 'tesla'
api_key = "APIKEY"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-08-05" \
      "&sortBy=publishedAt&" \
      "apiKey=APIKEY" \
      "language=en&" \
      "pageSize=5"

request = requests.get(url)
content = request.json()
message = """\
Subject: Tesla News

"""
for article in content['articles']:
        message = message + str(article['title']) \
                  + '\n' + article['description'] \
                  + '\n' + article['url'] + '\n\n'

message = message.encode('utf-8')
send_email(message)
