from modules.util import fileio, scraper, curator

# Returns a boolean indicating if updated data is available
def update_available():
	return fileio.has_update()

# Returns a dict obj of the updated item_list
def get_update():
	fileio.set_update_status(False)
	return fileio.get_item_list_from_file()

# Starts a new search
def search(search_str):
	