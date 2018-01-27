from modules.util import scrape, curator

print("Search: ", end = "")
search_str = input()

item_lists = scrape.get_item_lists(search_str)
print(curator.get_curated_item_list(item_lists))