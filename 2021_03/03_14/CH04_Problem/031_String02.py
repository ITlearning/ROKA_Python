# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)

number = int(input("정수 입력 > "))

if number % 2 == 0 :
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number,number))
else :
     print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number,number))