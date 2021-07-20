import os

# Text to Binary
# Convert your text into binary format.

version = "be-1.0-se"

print("""
█▄▄ █ █▄░█ ▄▀█ █▀█ █▄█   █▀▀ █▄█ █▀▀
█▄█ █ █░▀█ █▀█ █▀▄ ░█░   ██▄ ░█░ ██▄
""")
print("---------------------")
print(" Version:", version   )
print("---------------------")
print("")

rtools = input("Python is Installed [Yes/No] : ")
print("")

if (rtools == "Yes"):
    text = input("Type your text: ") # Type your text
    print("")
    binary = "".join(format(ord(i), "08b") for i in text)
    print("Binary:", binary) # Prints text in binary format.
elif(rtools == "No"):
    os.system("bash requirements.sh")
else:
    print("Please type [Yes/No] only.")
