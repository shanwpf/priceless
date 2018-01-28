from modules.util import scraper, curator, fileio
import time

print("Search: ", end = "")
search_str = input()
print("How much are you willing to pay? ", end = "")
willing_to_pay = input().strip()

while True:
	item_lists = scraper.get_item_lists(search_str)
	curated_list = curator.get_curated_item_list(item_lists, willing_to_pay, search_str)
	print(fileio.update_results_file(curated_list))
	time.sleep(10)
