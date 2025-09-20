text = input("Enter some text: ")

char_count = len(text)
word_count = len(text.split())
digit_count = sum(char.isdigit() for char in text)
letter_count = sum(char.isalpha() for char in text)

print(f"Character count: {char_count}")
print(f"Word count: {word_count}")
print(f"Digit count: {digit_count}")
print(f"letter count: {letter_count}")

name = "omkar"
print(type(name))