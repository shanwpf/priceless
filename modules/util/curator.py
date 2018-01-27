ITEM_NAME_FILTER_LIST = ['buying', 'wtb', 'buy', 'looking for']
PRICE_THRESHOLD_RATIO = 0.7

# def is_bad_price(item, willing_price):
# 	item_price_float = float(item['price'])
# 	if item_price_float < float(willing_price):
# 		return True
# 	else:
# 		return False

def name_contains_keyword(item, search_str):
	split_str = search_str.split(" ")
	for keyword in split_str:
		if keyword.lower() in item['product_name'].lower():
			return True
	return False

def name_contains_filtered_word(item):
	for phrase in ITEM_NAME_FILTER_LIST:
		if phrase in item['product_name'].lower():
			return True
	return False

# def is_bad_name(item, search_str):
# 	if name_contains_filtered_word(item):
# 		return True
# 	elif not name_contains_keyword(item, search_str):
# 		return True
# 	else:
# 		return False

# def is_bad_item(item):
# 	if is_bad_price(item) or is_bad_name(item):
# 		return True
# 	else:
# 		return False

def clean_bad_price(item_list, willing_price):
	item_list = list(filter(lambda item: 
		float(item['price']) <= float(willing_price) and
		float(item['price']) >= float(willing_price) * PRICE_THRESHOLD_RATIO,
		item_list))
	return item_list

def clean_bad_name(item_list, search_str):
	item_list = list(filter(lambda item:
		not name_contains_filtered_word(item) and
		name_contains_keyword(item, search_str),
		item_list))
	return item_list

def get_cleaned_list(item_list, willing_price, search_str):
	item_list = clean_bad_name(item_list, search_str)
	item_list = clean_bad_price(item_list, willing_price)
	return item_list

# Sorts an item list by price
def sort_list(item_list):
	item_list = sorted(item_list, key = lambda item: float(item['price']))
	return item_list

# def sort_all_lists(item_lists):
# 	for item_list in item_lists:
# 		sort_list(item_list)
# 	return item_lists

# Combines all item lists into a single item list
def join_all_lists(item_lists):
	joined_list = []
	for item_list in item_lists:
		joined_list += item_list
	return joined_list

def curate_list(item_list, willing_price, search_str):
	item_list = get_cleaned_list(item_list, willing_price, search_str)
	item_list = sort_list(item_list)
	return item_list

# Returns a curated item list from item lists
def get_curated_item_list(item_lists, willing_price, search_str):
	item_list = curate_list(join_all_lists(item_lists), willing_price, search_str)
	return item_list
