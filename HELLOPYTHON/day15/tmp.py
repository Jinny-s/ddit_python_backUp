arrs = [0,1,2,3,4,5,6,7,8,9]
arrs2 = [0,1,2,3,2,5,6,4,8,9]

for i, arr in enumerate(arrs):
    if arrs[i] == arrs2[i]:
        print(arrs[i], arrs2[i],'일치')
    else:
        print(arrs[i], arrs2[i],'불일치')
        
for i in arrs:
    if arrs[i] == arrs2[i]:
        print(arrs[i], arrs2[i],'일치')
    else:
        print(arrs[i], arrs2[i],'불일치')