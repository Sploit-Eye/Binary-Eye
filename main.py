import os

# Text to Binary
# Convert your text into binary format.

version = "be-1.1-se"

def greencolor(skk): print("\033[92m {}\033[00m" .format(skk))
def redcolor(skk): print("\033[91m {}\033[00m" .format(skk))

greencolor("""
█▄▄ █ █▄░█ ▄▀█ █▀█ █▄█   █▀▀ █▄█ █▀▀
█▄█ █ █░▀█ █▀█ █▀▄ ░█░   ██▄ ░█░ ██▄
""")
print("[0] Install required tools")
print("[1] Start Binary Eye")
print("[2] About")
print("[3] Exit")
print("")

uanswer = input("Choose: ")

if (uanswer == "0"):
    os.system("bash requirements.sh")
elif(uanswer == "1"):
    print("")
    ntext = input("Type your text: ")
    print("")
    bformat = "".join(format(ord(i), "08b")for i in ntext)
    print("Binary code:", bformat)
elif(uanswer == "2"):
    greencolor("Binary Eye is created by Sploit Eye.")
    greencolor("This tool converts your text into binary format, this tool")
    greencolor("is open source. Source code is available on GitHub.")
    print("")
    greencolor("Source code - https://github.com/Sploit-Eye/binary-eye")
elif(uanswer == "3"):
    exit()
else:
    print("")
    redcolor("Please type the given numbers.")
