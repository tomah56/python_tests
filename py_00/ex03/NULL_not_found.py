def NULL_not_found(object: any) -> int:
	# So some majic with pythoon nan not defined or undefined values are not equel to themself.
	if object is None:
		print(f"Nothing: None : {type(object)}")
	elif type(object) is int and object == 0:
		print(f"Zero: 0 : {type(object)}")
	elif type(object) is float and object != object:
		print(f"Cheese: nan : {type(object)}")
	elif type(object) is str:
		if not len(object):
			print(f"Empty : {type(object)}")
		else:
			print("Type not found")
			return 1 
	elif type(object) is bool:
		print(f"Fake: {object} : {type(object)}")
		return 1
	else:
		print(f"Not Null: {object} : {type(object)}")
		return 1
	return 0
#your code