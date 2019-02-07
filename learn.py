
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

#Loop Method

for each_items in movies:
	if isinstance(each_items,list):
		for nested_items in each_items:
			if isinstance(nested_items,list):
				for nest_item in nested_items:
					print(nest_item)
			else:
				print(nested_items)
	else:
		print(each_items)

#Function Method

def print_list(the_list):
	for each_items in the_list:
		if isinstance(each_items,list):
			print_list(each_items)
		else:
			print(each_items)

print_list(movies)

