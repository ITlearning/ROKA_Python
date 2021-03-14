# while 반복문 :break 키워드/ continue 키워드

# break 키워드

# 변수를 선언합니다.
i = 0

while True :
    # 몇 번째 반복인지 출력합니다.
    print("{}번째 반복문입니다.".format(i))
    i = i + 1
    input_next = input("> 종료하시겠습니까?(y/n): ")
    if input_next in ["Y", "y"] :
        print("반복을 종료합니다.")
        break