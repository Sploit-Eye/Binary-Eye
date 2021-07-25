import os

# Text to Binary
# Convert your text into binary format.

version = "be-1.4-se"

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
print("[2] Subscribe on YouTube")
print("[3] About")
print("[4] Exit")
print("")

uanswer = input("Choose: ")

if (uanswer == "0"):
    os.system("bash requirements.sh")
elif(uanswer == "1"):
    os.system("tput clear")
    greencolor("""
█▄▄ █ █▄░█ ▄▀█ █▀█ █▄█   █▀▀ █▄█ █▀▀
█▄█ █ █░▀█ █▀█ █▀▄ ░█░   ██▄ ░█░ ██▄
    """)
    print(version)
    print("")
    print("[0] Text to binary")
    print("[1] Binary to text")
    print("[2] Main menu")
    print("")
    sanswer = input("Choose: ")
    print("")
    if(sanswer == "0"):
        text = input("Type your text: ")
        btext = "".join(format(ord(i), "08b") for i in text)
        print("")
        print("Binary code:", btext)
    elif(sanswer == "1"):
        binary_int = input("Type binary code: ")
        binary_int = int(binary_int, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        print("")
        print("Text:", ascii_text)
    elif(sanswer == "2"):
        os.system("tput clear")
        os.system("python3 main.py")
    else:
        redcolor("Please type the given numbers.")
elif(uanswer == "2"):
    os.system("open https://www.youtube.com/channel/UCepn9DYAldPfXPARemNAuCQ")
elif(uanswer == "3"):
    greencolor("This tool was created by Sploit Eye.")
    greencolor("Tool is open-source, get source code")
    greencolor("on GitHub. Modify it & improve it.")
    print("")
    greencolor("Thanks for using Binary Eye.")
elif(uanswer == "4"):
    os.system("tput clear")
    exit()
else:
    print("")
    redcolor("Please type the given numbers only.")
