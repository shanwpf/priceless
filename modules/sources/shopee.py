from bs4 import BeautifulSoup
import requests
import json

SEARCH_API_URL = "https://shopee.sg/api/v1/search_items"
ITEMS_API_URL = "https://shopee.sg/api/v1/items"

def create_item_list(json_obj):
	print(json_obj)
	item_list = []
	for card in json_obj:
		item = {}
		item['product_name'] = card["name"]
		item['price'] = card["price"]/100000.0
		item['url'] = card["name"].replace(" ", "-") + "-i." + card["shopid"] + "." + card["itemid"]
		item_list.append(item)

	print(json.dumps(item_list, indent=2, sort_keys=True)) # Pretty prints

def get_item_list(search_str):
	# First API Call to obtain list of IDs
	headers = { "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36", \
	'origin': 'https://shopee.sg', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en;q=0.9,zh;q=0.8', \
		'x-requested-with': 'XMLHttpRequest', 'content-type': 'application/json', 'accept': 'application/json', \
		'referer': 'https://shopee.sg/search/?keyword=something+something', 'authority': 'shopee.sg', 'x-api-source': 'pc', 'dnt': '1'}
	params = {"by":"pop", "order":"desc", "keyword":search_str, "newest":"0", "limit":"50" }
	idData = requests.get(SEARCH_API_URL, headers=headers, params=params)
	#print(idData.text)
	itemIDs = json.loads(idData.text)["items"]
	payload = {}
	payload["item_shop_ids"] = itemIDs
	f = open("shopee.json", "w")
	f.write(json.dumps(payload))
	#print(payload)

	# Second API Call to obtain list of search results
	data = json.dumps(payload)
	response = requests.post(ITEMS_API_URL, headers=headers, data=open("shopee.json","rb"))
	return create_item_list(response.json())

get_item_list("something something")