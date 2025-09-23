import sys as sys

try:
	# This could throw an AssertionError
	assert len(sys.argv) < 3, "more than one argument is provided"
	if len(sys.argv) == 2:
		try:
			# This could throw an ValueError
			num = int(sys.argv[1]) # convert arg to int
			if num % 2 != 0:
				print("I'm Odd.")
			else:
				print("I'm Even.")
		# Catch ValueError and transform it to AssertionError
		except ValueError:
			raise AssertionError("argument is not an integer")
except AssertionError as error:
	print(f"AssertionError: {error}")
