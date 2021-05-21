#Exer 02
#첫 숫자를 입력하시오 : 1
#끝 숫자를 입력하시오 : 3
#모든 수의 합은 '6'입니다 (1~3 덧셈)

a = int(input("첫 숫자를 입력하시오"))
b = int(input("끝 숫자를 입력하시오"))
c = 0
for i in range(a, b+1):
    c += i
print("모든 수의 합은 {}입니다".format(c))