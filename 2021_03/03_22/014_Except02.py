# 여러 가지 예외가 발생할 수 있는 코드
list_number = [52,273,32,72,100]

try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)