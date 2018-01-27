from modules.util import scraper, curator

print("Search: ", end = "")
search_str = input()
print("How much are you willing to pay? ", end = "")
willing_to_pay = input().strip()

item_lists = scraper.get_item_lists(search_str)
print(curator.get_curated_item_list(item_lists, willing_to_pay, search_str))
