import json, os

FILE_PATH = './out/results.json'

def file_exists():
	return os.path.isfile(FILE_PATH)

def file_differs(item_list):
	with open(FILE_PATH) as existing_file:
		existing_data = json.load(existing_file)
		return existing_data == item_list

def overwrite_file(item_list):
	with open(FILE_PATH, 'w') as outfile:
		json.dump(item_list, outfile)

def update_results_file(item_list):
	if not file_exists() or file_differs(item_list):
		overwrite_file(item_list)
		return True
	else:
		return False
