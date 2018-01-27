from bs4 import BeautifulSoup
import requests

SEARCH_URL_PREFIX = "https://www.qoo10.sg/s/"
SEARCH_URL_MID = "?keyword="
SEARCH_URL_POSTFIX = "&keyword_auto_change="

def generate_url(search_str):
	return SEARCH_URL_PREFIX + search_str + SEARCH_URL_MID + search_str  + SEARCH_URL_POSTFIX

def format_price(price_str):
	return price_str[1:]

def create_item_list(html_doc):
    item_list = []
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    for items in soup.find_all("tr", {"list_type": "search_new_list_type"}):
        item = {}
        item['product_name'] = items.find(attrs={"class": "sbj"}).text
        item['price'] = format_price(items.select_one("div.prc").find("strong").text)
        item['url'] = items.find(attrs={"data-type": "goods_url"})["href"]
        item_list.append(item)
    return item_list

def get_item_list(search_str):
	html_doc = requests.get(generate_url(search_str))
	return create_item_list(html_doc);


