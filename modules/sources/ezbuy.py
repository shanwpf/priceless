import requests
import json

SEARCH_API_URL = "https://sg-en-web-api.ezbuy.sg/api/EzCategory/ListProductsByCondition"

def generate_url(search_str):
	return URL_PREFIX + search_str.replace(" ", REPLACE_SPACE_STRING)

def create_item_list(cardList):
	item_list = []
	#print(cardList)
	for card in cardList["products"]:
		item = {}
		item['product_name'] = card['name']
		item['price'] = card['price']
		item['url'] = "https://ezbuy.sg/product/" + card['url'] + ".html" 
		item_list.append(item)

	# print(json.dumps(item_list, indent=2, sort_keys=True)) # Pretty prints
	return item_list

def get_item_list(search_str):
	headers = {'Origin': 'https://ezbuy.sg', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en;q=0.9,zh;q=0.8',\
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',\
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': 'application/json, text/javascript, */*; q=0.01',\
			'Connection': 'keep-alive', 'DNT': '1'}
	formData = '{"searchCondition":{"limit":56,"offset":0,"propValues":[],"filters":[],\
			"keyWords":"' + search_str + '","categoryId":0},"limit":56,"offset":0,"language":"en","dataType":"new"}'
	response = requests.post(SEARCH_API_URL, headers=headers, data=formData)
	return create_item_list(json.loads(response.text))
	
# get_item_list("something something")