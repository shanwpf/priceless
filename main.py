from modules.sources import carousell, lazada, qoo10
from modules.util import filterItems

print("Search: ", end = "")
search_str = input()

carousell_item_list = filterItems.get_filtered_list(carousell.get_item_list(search_str))
lazada_item_list = lazada.get_item_list(search_str)
qoo10_item_list = qoo10.get_item_list(search_str)
print(qoo10_item_list)