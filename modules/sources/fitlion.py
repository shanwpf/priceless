from bs4 import BeautifulSoup
import requests

URL_PREFIX = "https://sg.fitlion.com/catalogsearch/result/?q="
REPLACE_SPACE_STRING = "+"

def generate_url(search_str):
	return URL_PREFIX + search_str.replace(" ", REPLACE_SPACE_STRING)

# Fitlion puts S$ infront of their pricing
# This function removes the characters and turns it into a float
def format_price(price_str):
	return price_str[2:]

def create_item_list(html_doc):
	item_list = []

	soup = BeautifulSoup(html_doc.text, 'html.parser')

	# Logic for processing the prices of the product
	# Handled regular prices that is discounted on sale
	price_box_raw = soup.find_all("div", "price-box")

	for element in price_box_raw:
		item = {}
		
		# If the item is on discount
		if(element.find("span").find("span") == None and element.find("span").text == "Regular Price:"):
			item['price'] = format_price(element.find(attrs={"class" : "special-price"}).find(attrs={"class":"price"}).text.split()[0])
			

		elif(element.find("span").find("span") == None):
			item['price'] = format_price(element.find("span").text)

		else:
			item['price'] = format_price(element.find("span").find("span").text)

		print(item['price'])

		item_list.append(item)

	product_name_raw = soup.find_all("h2", "product-name")
	for element in product_name_raw:

		item = {}
		item['product_name'] = element.find("a")['title']
		item['url'] = element.find("a")['href']
		item_list.append(item)

	return item_list

def get_item_list(search_str):
	html_doc = requests.get(generate_url(search_str))
	return create_item_list(html_doc)