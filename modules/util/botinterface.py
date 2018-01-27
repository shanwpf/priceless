from modules.util import fileio, scraper, curator

current_search_str = ""

# Returns a boolean indicating if updated data is available
def is_update_available():
	return fileio.has_update()

# Returns a dict obj of the updated item_list
def update():
	item_lists = scraper.get_item_lists(search_str)
	curated_list = curator.get_curated_item_list(item_lists, willing_to_pay, search_str)
	fileio.update_results_file(curated_list)
	return fileio.get_item_list_from_file()

# def get_update():
# 	fileio.set_update_status(False)
# 	return fileio.get_item_list_from_file()

# Starts a new search
def search(search_str):
	current_search_str = search_str
	return update()
	