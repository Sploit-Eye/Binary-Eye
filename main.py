text = input("Type your text: ")

binary = "".join(format(ord(i), "08b") for i in text)

print("Binary:", binary)