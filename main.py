from modules.sources import carousell, lazada, qoo10, fitlion
from modules.util import filterItems

print("Search: ", end = "")
search_str = input()

carousell_item_list = filterItems.get_filtered_list(carousell.get_item_list(search_str))
lazada_item_list = lazada.get_item_list(search_str)
qoo10_item_list = qoo10.get_item_list(search_str)
fitlion_item_list = fitlion.get_item_list(search_str)
print(fitlion_item_list)
print('\n')
print(carousell_item_list)