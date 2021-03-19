n = int(input())

A = []
for i in range(n) :
    A.append(input().split(' '))
    
a = int(input())
B = []
for i in range(n) :
    B.append(input().split(' '))
    
for i in range(n) :
    if B[i] in A :
        print("1")
    else :
        print("0")