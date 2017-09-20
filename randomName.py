from bs4 import BeautifulSoup
import requests

data =  requests.get("https://randomuser.me/api/").json()
result = data["results"]

for i in result:
	for d in i:
		print 