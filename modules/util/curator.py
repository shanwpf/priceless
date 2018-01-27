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

# Returns the curated item list one item list
def curate_item_list(item_list):
	return item_list[:10]

# Returns a curated item list from item lists
def get_curated_item_list(item_lists):
	item_lists = sort_list(join_all_lists(item_lists))
	return curate_item_list(item_lists)