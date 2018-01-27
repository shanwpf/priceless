from modules.sources import carousell
from modules.util import filterItems

print("Search: ", end = "")
search_str = input()

carousell_item_list = filterItems.get_filtered_list(carousell.get_item_list(search_str))
print(carousell_item_list)