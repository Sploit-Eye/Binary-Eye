import os

# Text to Binary
# Convert your text into binary format.

version = "be-1.2-se"

def greencolor(skk): print("\033[92m {}\033[00m" .format(skk))
def redcolor(skk): print("\033[91m {}\033[00m" .format(skk))

os.system("tput clear")

greencolor("""
█▄▄ █ █▄░█ ▄▀█ █▀█ █▄█   █▀▀ █▄█ █▀▀
█▄█ █ █░▀█ █▀█ █▀▄ ░█░   ██▄ ░█░ ██▄
""")
print(version)
print("")
print("[0] Install required tools")
print("[1] Start Binary Eye")
print("[2] Source Code")
print("[3] About")
print("[4] Exit")
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
    os.system("open https://github.com/Sploit-Eye/binary-eye")
elif(uanswer == "3"):
    greencolor("This tool was created by Sploit Eye.")
    greencolor("Tool is open-source, get source code")
    greencolor("on GitHub.")
    print("")
    greencolor("Thanks for using Binary Eye.")
elif(uanswer == "4"):
    exit()
else:
    print("")
    redcolor("Please type the given numbers only.")
