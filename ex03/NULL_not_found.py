def NULL_not_found(object: any) -> int:
	Nothing = None
	# if isinstance(object, None):
	# if object == Nothing:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
		return 0
	# Here I need to check for NaN. NaN is not equal to itself, and it's a "Number"
	elif isinstance(object, float):
		# if object == float("NaN"):
		if object != object:
			print(f"Cheese: {object} {type(object)}")
			return 0
	elif isinstance(object,str):
		if len(object) == 0:
			print(f"Empty:{object} {type(object)}")
			return 0
	elif isinstance(object,bool):
		# Can I do this? Or I need to do object == False
		if not object:
			print(f"Fake: {object} {type(object)}")
			return 0
	elif isinstance(object,int):
		if object == 0:
			print(f"Zero: {object} {type(object)}")
			return 0
	# else:
	print("Type not Found")
	return 1
