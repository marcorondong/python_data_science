import sys as sys

def plural(word, count):
	return word + ('s' if count != 1 else '')

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

def main():
	try:
		assert len(sys.argv) < 3, "more than one argument is provided"
		if len(sys.argv) == 2 and sys.argv[1] != "":
			txt = sys.argv[1]
		else:
			txt = input("What is the text to count?\n")
			while len(txt) == 0:
				txt = input("What is the text to count?\n")
		get_stats(txt)

	except AssertionError as error:
		print(F"AssertionError: {error}")

if __name__ == "__main__":
	main()