ITEM_NAME_FILTER_LIST = ['buying', 'wtb', 'buy', 'looking for']
PRICE_THRESHOLD_RATIO = 0.7

def is_bad_price(item, willing_price):
	item_price_float = float(item['price'])
	if item_price_float < float(willing_price):
		return True
	else:
		return False

def is_bad_name(item):
	item_name = item['product_name']
	for phrase in ITEM_NAME_FILTER_LIST:
		if phrase in item_name:
			return True
	return False

def is_bad_item(item):
	if is_bad_price(item) or is_bad_name(item):
		return True
	else:
		return False

def clean_bad_price(item_list, willing_price):
	item_list = list(filter(lambda item: 
		float(item['price']) <= float(willing_price) and
		float(item['price']) >= float(willing_price) * PRICE_THRESHOLD_RATIO,
		item_list))
	return item_list

def clean_bad_name(item_list):
	for item in item_list:
		if is_bad_name(item):
			item_list.remove(item)
	return item_list

def get_cleaned_list(item_list, willing_price):
	item_list = clean_bad_name(item_list)
	item_list = clean_bad_price(item_list, willing_price)
	return item_list
