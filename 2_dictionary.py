# Create an empty dictionary
_dict = {}

# using foor loop arrange dictionary with alphabet keys and corresponding ASCII values
for letter in range(ord('a'), ord('z') + 1):
    _dict[chr(letter)] = letter

# Print the dictionary
print(_dict)
