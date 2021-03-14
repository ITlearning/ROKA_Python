# 이 문제를 해결하려면 다음과 같이 코딩한다.

# if 조건문과 여러 줄 문자열(3)
number = int(input("정수 입력 > "))

if number % 2 == 0 :
    print("""입력한 문자열은 {}입니다.\n{}는 짝수입니다.""".format(number,number))
else :
    print("""입력한 문자열은 {}입니다.\n{}는 홀수입니다.""".format(number,number))
    
    # 이렇게 하면 코드가 다행히 잘 보이긴 하는데, 길게 적음으로 인해 다소 복잡해보일수가 있다.
    
    