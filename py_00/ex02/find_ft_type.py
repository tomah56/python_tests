def all_thing_is_obj(object: any) -> int:

# this is really dump... no idea why but lets print what they want....
# what the costumer wants the costumer gets.

# try catch may mean nothing here but we comming from c so lets be safe.
	try:
		# if isinstance(object, int):
		# 	print("Type not found 5")
		if type(object) is int:
			print("Type not found")
		elif type(object) is str:
			print(f"{object} is in the kitchen : {type(object)}")
		else:
			print(f"{type(object).__name__ } : {type(object)}")
	except NameError as e:
		print("Type not found" , e)
		return 1
	return 0
# pass if no return ?