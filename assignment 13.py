'''              ASSIGNMENT- WEB API'S USING PYTHON               '''

# Q.1 Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.

import requests
import json
resp = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=435251")
data = json.loads(resp.text)
print(data["quoteText"])
