from modules.util import fileio, scraper, curator

current_search_str = ""
current_willing_price = 0

# Returns a boolean indicating if updated data is available
def is_update_available():
	return fileio.has_update()

# Returns a dict obj of the updated item_list
def update():
	item_lists = scraper.get_item_lists(current_search_str)
	curated_list = curator.get_curated_item_list(item_lists, current_willing_price, current_search_str)
	fileio.update_results_file(curated_list)
	return fileio.get_item_list_from_file()

# def get_update():
# 	fileio.set_update_status(False)
# 	return fileio.get_item_list_from_file()

def process_input(input_str):
	last_space = input_str.rfind(" ")
	current_search_str = input_str[:last_space - 1]
	current_willing_price = input_str[last_space + 1:]

# Starts a new search
def search(input_str):
	process_input(input_str)
	return update()
