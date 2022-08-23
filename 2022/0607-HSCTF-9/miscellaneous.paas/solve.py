# text = input("enter a string to convert into ascii values:")
text = "AAA = 123"
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
# print(ascii_values)
for i in ascii_values:
    print("chr(", end="")
    print(i, end="")
    print(")+", end="")

print("done")