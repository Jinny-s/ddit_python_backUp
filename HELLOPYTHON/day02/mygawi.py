import random

mine = input("가위바위보!")
com = ""
reulst = ""

rand = random.random()

if rand > 0.66:
    com = "가위"
elif rand > 0.33:
    com = "바위"
else:
    com = "보"

if mine == com:
    result = "DRAW!"
elif (mine == "가위" and com == "보") or (mine=="바위" and com =="가위") or (mine=="보" and com =="바위"):
    result = "USER WIN!"
else:
    result = ("COM WIN!")

print("com:",com)
print("mine:",mine)
print("result:",result)

# if mine == com:
#     result = "DRAW!"
# elif mine == "가위":
#     if com == "보":
#         result = "USER WIN!"
#     elif com == "바위":
#         result = "COM WIN!"
# elif mine == "바위":
#     if com == "가위":
#         result = "USER WIN!"
#     elif com == "보":
#         result = "COM WIN!"
# elif mine == "보":
#     if com == "바위":
#         result = "USER WIN!"
#     elif com == "가위":
#         result = "COM WIN!"