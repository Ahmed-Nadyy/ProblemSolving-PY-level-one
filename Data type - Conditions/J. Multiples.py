

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
 
number_1,number_2=input().split()
number_1=int(number_1)
number_2=int(number_2)
 
# floorRes=math.floor(float(number_1/number_2))
# ceilRes=math.ceil(float(number_1/number_2))
# roundRes=round(float(number_1/number_2))
# print("floor",number_1,"/",number_2,"=",floorRes)
# print("ceil",number_1,"/",number_2,"=",ceilRes)
if (number_1%number_2==0):
    print("Multiples")
elif (number_2%number_1==0):
    print("Multiples")
else :
    print("No Multiples")
# ,number_2,number_3,number_4=input().split()
# number_1_plus=int(number_1+1)
# number_3=int(number_3)
# number_4=int(number_4)
 
# number_1=number_1%10
# number_2=number_2%10
 