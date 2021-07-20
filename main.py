# Text to Binary
# Convert your text into binary format.

print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄

""")

text = input("Type your text: ") # Type your text
print("")

binary = "".join(format(ord(i), "08b") for i in text)

print("Binary:", binary) # Prints text in binary format.
