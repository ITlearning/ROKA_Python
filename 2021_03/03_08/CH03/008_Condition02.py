# in 문자열 연산자를 활용해서 짝수와 홀수 구분

number = input("정수 입력 > ")
last_number = number[-1]

if last_number in "02468" :
    print("짝수입니다")

if last_number in "13579" :
    print("홀수입니다")