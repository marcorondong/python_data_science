def NULL_not_found(object: any) -> int:
	if isinstance(object, None):
		print(f"Nothing : {object} {type(object)}")
	elif isinstance(object, float):
		print(f"Cheese : {object} {type(object)}")