from bs4 import BeautifulSoup
import requests

URL_PREFIX = "https://carousell.com/search/products/?query="
REPLACE_SPACE_STRING = "%20"

def generate_url(search_str):
	return URL_PREFIX + search_str.replace(" ", REPLACE_SPACE_STRING)

def create_item_list(html_doc):
	item_list = []
	soup = BeautifulSoup(html_doc.text, 'html.parser')
	for card in soup.find_all("figure", "card"):
		item = {}
		item['username'] = card.find("h3", "media-heading").text
		item['product_name'] = card.find("h4").text
		item['date'] = card.find("time").find("span").text
		item['price'] = card.find("dl").find("dd").text
		item['desc'] = card.select_one("dl dd:nth-of-type(2)").text
		item_list.append(item)
	return item_list

def get_item_list(search_str):
	html_doc = requests.get(generate_url(search_str))
	return create_item_list(html_doc);
