from bs4 import BeautifulSoup
import requests
import json

URL_PREFIX = "https://www.lazada.sg/catalog/?q="
REPLACE_SPACE_STRING = "+"

def generate_url(search_str):
	return URL_PREFIX + search_str.replace(" ", REPLACE_SPACE_STRING)

def create_item_list(html_doc):
	item_list = []
	soup = BeautifulSoup(html_doc.text, 'html.parser')
	cards = json.loads(soup.find_all("script", type="application/ld+json")[1].text)
	for card in cards["itemListElement"]:
		item = {}
		item['product_name'] = card['name']
		item['price'] = card['offers']['price']
		item['url'] = card['url']
		item_list.append(item)
	return item_list

def get_item_list(search_str):
	html_doc = requests.get(generate_url(search_str))
	return create_item_list(html_doc)
	