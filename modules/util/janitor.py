ITEM_NAME_FILTER_LIST = ['buying', 'wtb', 'buy', 'looking for']

def is_bad_price(item):
	item_price_float = float(item['price'])
	if item_price_float < 1:
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

def get_cleaned_list(item_list):
	for item in item_list:
		if is_bad_item(item):
			item_list.remove(item)
	return item_list
