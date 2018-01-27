from bs4 import BeautifulSoup
import requests

URL_PREFIX = "https://sg.gymshack.com/search?q="
URL_PRODUCT_PREFIX = "https://sg.gymshack.com"
REPLACE_SPACE_STRING = "+"

def generate_url(search_str):
	return URL_PREFIX + search_str.replace(" ", REPLACE_SPACE_STRING)

# The website uses a postfix to lead to their catalouge
# This function is to concatenate the website with it's product detail postfix
def generate_product_detail(str):
	return URL_PRODUCT_PREFIX + str

# The website uses $11.00 SGD as their price format
# This function is to remove the prefix and postfix of the format
def format_price(str):
	return str[1:-4]

def create_item_list(html_doc):
	item_list = []

	soup = BeautifulSoup(html_doc.text, 'html.parser')
	product_box_raw = soup.find_all("div", "block-inner")
	for element in product_box_raw:
		item = {}

		item['product_name'] = element.find("div", "title").text
		
		item['url'] = generate_product_detail(element.find("a")['href'])

		# Checks if the item is in discount, if it is, then take the lesser value
		if(element.find("div", "reducedfrom") == None):
			item['price'] = format_price(element.find("span", "money").text)
		else:
			item['price'] = format_price(element.find("span", "price").find("span", "money").text)



		item_list.append(item)

		
	print(item_list)

def get_item_list(search_str):
	html_doc = requests.get(generate_url(search_str))
	return create_item_list(html_doc)

get_item_list("creatine")