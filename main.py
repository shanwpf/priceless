from modules.util import scraper, curator

print("Search: ", end = "")
search_str = input()

item_lists = scraper.get_item_lists(search_str)
print(curator.get_curated_item_list(item_lists))
