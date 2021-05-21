import random
r = random.randint(1, 10)

mine = input("홀/짝을 선택하세요")
print(mine)

if r%2 == 0:
    a = "짝"
else:
    a = "홀"

if mine == a:
    print("유저 우승!")
else:
    print("컴퓨터 우승!")