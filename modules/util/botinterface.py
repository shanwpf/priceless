from modules.util import fileio, scraper, curator

# Returns a boolean indicating if updated data is available
def is_update_available():
	return fileio.has_update()

# Returns a dict obj of the updated item_list
def update(search_str, willing_price):
	item_lists = scraper.get_item_lists(search_str)
	curated_list = curator.get_curated_item_list(item_lists, willing_price, search_str)
	fileio.update_results_file(curated_list)
	return fileio.get_item_list_from_file()

# def get_update():
# 	fileio.set_update_status(False)
# 	return fileio.get_item_list_from_file()

def process_input(input_str):
	last_space_idx = input_str.rfind(" ")
	current_search_str = input_str[:last_space_idx].strip()
	current_willing_price = float(input_str[last_space_idx + 1:].strip())
	return {'search_str': current_search_str, 'willing_price': current_willing_price}

# Starts a new search
def search(input_str):
	args = process_input(input_str)
	return update(args['search_str'], args['willing_price'])
