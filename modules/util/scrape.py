from modules.sources import carousell, lazada
from modules.util import janitor

def get_item_lists(search_str):
	item_lists = []
	item_lists.append(janitor.get_cleaned_list(carousell.get_item_list(search_str)))
	item_lists.append(lazada.get_item_list(search_str))
	return item_lists