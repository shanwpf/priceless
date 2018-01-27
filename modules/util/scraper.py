from modules.sources import carousell, lazada, qoo10, fitlion, gymshack, ezbuy

def get_item_lists(search_str):
	item_lists = []

	#Add new source modules here
	item_lists.append(carousell.get_item_list(search_str))
	item_lists.append(lazada.get_item_list(search_str))
	item_lists.append(qoo10.get_item_list(search_str))
	item_lists.append(gymshack.get_item_list(search_str))
	item_lists.append(ezbuy.get_item_list(search_str))
	item_lists.append(fitlion.get_item_list(search_str))
	return item_lists
