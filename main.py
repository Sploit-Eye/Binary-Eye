# Text to Binary
# Convert your text into binary format.

version = "ttb-1.0-se"

print("""
▀█▀ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █▀█   █▄▄ █ █▄░█ ▄▀█ █▀█ █▄█
░█░ ██▄ █░█ ░█░   ░█░ █▄█   █▄█ █ █░▀█ █▀█ █▀▄ ░█░
""")
print("---------------------")
print(" Version:", version   )
print("---------------------")
print("")

text = input("Type your text: ") # Type your text
print("")

binary = "".join(format(ord(i), "08b") for i in text)

print("Binary:", binary) # Prints text in binary format.
