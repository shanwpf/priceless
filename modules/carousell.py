from bs4 import BeautifulSoup
import requests

# TODO: Get url from main
html_doc = requests.get(input())
soup = BeautifulSoup(html_doc.text, 'html.parser')
item_list = []
for card in soup.find_all("figure", "card"):
	item = {}
	item['username'] = card.find("h3", "media-heading").text
	item['product_name'] = card.find("h4").text
	item['date'] = card.find("time").find("span").text
	item['price'] = card.find("dl").find("dd").text
	item['desc'] = card.select_one("dl dd:nth-of-type(2)").text
	item_list.append(item)
