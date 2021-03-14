# 문자열의 join() 함수
# join() 함수는 다음과 같은 형태로 사용합니다.
# 문자열.join(문자열로 구성된 리스트)

number = int(input("정수 입력 > "))

if number % 2 == 0 :
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number,number))
else :
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number,number))