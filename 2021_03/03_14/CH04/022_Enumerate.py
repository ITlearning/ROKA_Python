# enumerate() 함수와 리스트
# 변수를 선언합니다.
example_list = ["요소A", "요소B", "요소C"]

# 그냥 출력
print("# 단순출력")
print(example_list)
print()

# enumerate() 함수를 적용해 출력
print("# enumerate() 함수를 적용해 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력
print("# list() 함수로 강제 변환해 출력")
print(list(enumerate(example_list)))
print()

# 곧바로 출력되지 않고, 이상한 문구로 나오는 결과를 볼수 있다.
# 이는 이터레이터 때문인데, 추후에 더 자세히 나온다.

# for 반복문과 enumerate() 함수 조합해서 사용하기
print("# for 반복문과 enumerate() 함수 조합해서 사용하기")
for i, value in enumerate(example_list) :
    print("{}번째 요소는 {}입니다.".format(i,value))