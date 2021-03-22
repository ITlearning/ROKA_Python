# 예외 구문과 예외 객체
list_number = [52,273,32,72,100]

try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)