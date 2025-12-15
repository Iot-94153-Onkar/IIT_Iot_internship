# String Slicing 

text = input("Enter a string: ")

print("\nOriginal String:", text)

# Basic slicing
print("First 5 characters:", text[:5])
print("From index 2 to 6:", text[2:7])
print("From index 3 to end:", text[3:])

# Negative slicing
print("Last 4 characters:", text[-4:])
print("From -6 to -1:", text[-6:-1])

# Step slicing
print("Every second character:", text[::2])
print("Every third character:", text[::3])

# Reverse string
print("Reversed string:", text[::-1])
