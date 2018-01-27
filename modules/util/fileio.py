import json, os

FILE_PATH = './out/results.json'
update_available = False

def set_update_status(boolean):
	update_available = boolean

def file_exists():
	return os.path.isfile(FILE_PATH)

def file_differs(item_list):
	pairs = zip(get_item_list_from_file(), item_list)
	return any(x != y for x, y in pairs)

def get_item_list_from_file():
	with open(FILE_PATH) as existing_file:
		existing_data = json.load(existing_file)
		return existing_data

def overwrite_file(item_list):
	with open(FILE_PATH, 'w') as outfile:
		json.dump(item_list, outfile)

def has_update():
	return update_available

def update_results_file(item_list):
	if not file_exists() or (file_exists() and file_differs(item_list)):
		overwrite_file(item_list)
		update_available = True
		return True
	else:
		return False
