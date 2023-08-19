

#  ▄▄▄       ██░ ██  ███▄ ▄███▓▓█████ ▓█████▄     ███▄    █  ▄▄▄      ▓█████▄▓██   ██▓
# ▒████▄    ▓██░ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▒██▀ ██▌    ██ ▀█   █ ▒████▄    ▒██▀ ██▌▒██  ██▒
# ▒██  ▀█▄  ▒██▀▀██░▓██    ▓██░▒███   ░██   █▌   ▓██  ▀█ ██▒▒██  ▀█▄  ░██   █▌ ▒██ ██░
# ░██▄▄▄▄██ ░▓█ ░██ ▒██    ▒██ ▒▓█  ▄ ░▓█▄   ▌   ▓██▒  ▐▌██▒░██▄▄▄▄██ ░▓█▄   ▌ ░ ▐██▓░
#  ▓█   ▓██▒░▓█▒░██▓▒██▒   ░██▒░▒████▒░▒████▓    ▒██░   ▓██░ ▓█   ▓██▒░▒████▓  ░ ██▒▓░
#  ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░   ░  ░░░ ▒░ ░ ▒▒▓  ▒    ░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒   ██▒▒▒
#   ▒   ▒▒ ░ ▒ ░▒░ ░░  ░      ░ ░ ░  ░ ░ ▒  ▒    ░ ░░   ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒ ▓██ ░▒░
#   ░   ▒    ░  ░░ ░░      ░      ░    ░ ░  ░       ░   ░ ░   ░   ▒    ░ ░  ░ ▒ ▒ ░░
#       ░  ░ ░  ░  ░       ░      ░  ░   ░                ░       ░  ░   ░    ░ ░
#                                      ░                               ░      ░ ░
import math
 
number_1,number_2,number_3=input().split()
number_1=int(number_1)
number_2=int(number_2)
number_3=int(number_3)
# floorRes=math.floor(float(number_1/number_2))
# ceilRes=math.ceil(float(number_1/number_2))
# roundRes=round(float(number_1/number_2))
# print("floor",number_1,"/",number_2,"=",floorRes)
# print("ceil",number_1,"/",number_2,"=",ceilRes)
if (number_1>=number_2 and number_1>=number_3):
    if(number_2>=number_3):
        x=number_3
        y=number_1
    else:
        x=number_2
        y=number_1
if (number_2>=number_1 and number_2>=number_3):
    if(number_1>=number_3):
        x=number_3
        y=number_2
    else:
        x=number_1
        y=number_2
if (number_3>=number_1 and number_3>=number_2):
    if(number_1>=number_2):
        x=number_2
        y=number_3
    else:
        x=number_1
        y=number_3
print(x,y)
# ,number_2,number_3,number_4=input().split()
# number_1_plus=int(number_1+1)
 
# number_4=int(number_4)
 
# number_1=number_1%10
# number_2=number_2%10
 