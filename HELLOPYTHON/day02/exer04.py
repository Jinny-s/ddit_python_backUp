#Exer 04
#첫 숫자를 입력하시오 : 1
#끝 숫자를 입력하시오 : 4
#짝수의 합은 '6'입니다

a = int(input("첫 숫자를 입력하시오"))
b = int(input("끝 숫자를 입력하시오"))
c = 0

for i in range(a,b+1):
    if i % 2 == 0:
        c += i
print("짝수의 합은 {}입니다".format(c))            