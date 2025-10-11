import sys as sys

def plural(word, count):
	return word + ('s' if count != 1 else '')
plural.__doc__ = "Helper function that returns singular or plural word depending on the count"

def get_stats(txt):
	stats = {
				"character": 0,
				"upper": 0,
				"lower": 0,
				"punctuation": 0,
				"space": 0,
				"digit": 0
			}
	stats["character"] = len(txt)
	for char in txt:
		if char.isupper(): stats["upper"] += 1
		elif char.islower(): stats["lower"] += 1
		elif char.isspace(): stats["space"] += 1
		elif char.isdigit(): stats["digit"] += 1
		elif char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~": stats["punctuation"] += 1
	print(f"The text contains {stats['character']} {plural('character', stats['character'])}:")
	print(f"{stats['upper']} {plural('upper letter', stats['upper'])}")
	print(f"{stats['lower']} {plural('lower letter', stats['lower'])}")
	# print(f"{stats['punctuation']} {plural('punctuation mark', stats['punctuation'])}")
	print(f"{stats['punctuation']} punctuation marks")
	print(f"{stats['space']} {plural('space', stats['space'])}")
	print(f"{stats['digit']} {plural('digit', stats['digit'])}")
get_stats.__doc__ = "Helper function to process text and count chars, upper letters, lower, spaces, digits and punctuation marks"

def main():
	try:
		assert len(sys.argv) < 3, "more than one argument is provided"
		if len(sys.argv) == 2 and sys.argv[1] != "":
			txt = sys.argv[1]
		else:
			# txt = input("What is the text to count?\n")
			print("What is the text to count?")
			txt = sys.stdin.readline()
			while len(txt) == 0 or txt == '\n':
				# txt = input("What is the text to count?\n")
				print("What is the text to count?")
				txt = sys.stdin.readline()
		get_stats(txt)

	except AssertionError as error:
		print(F"AssertionError: {error}")
	except Exception as e:
		print(f"Error: {type(e).__name__}: {e}")
main.__doc__ = "main function that reads text from args or stdin and process it with helper function get_stats()"

if __name__ == "__main__":
	main()
