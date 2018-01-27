from modules import carousell

print("Search: ", end = "")
search_str = input()

carousell_item_list = carousell.get_item_list(search_str)
print(carousell_item_list)