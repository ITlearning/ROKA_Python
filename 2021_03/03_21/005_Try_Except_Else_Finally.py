# finally 구문
try:
    number_input_a = int(input("정수입력 > "))
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 : {}".format(2*3.14*number_input_a))
    print("원의 넓이 :", 3.14 * number_input_a * number_input_a)
except:
     print("정수를 입력하지 않았습니다. 제대로 입력좀 해보세요.")
else:
     print("예외가 발생하지 않았습니다.")
finally:
    print("예..뭐..어떻게든 프로그램이 끝났습니다.")