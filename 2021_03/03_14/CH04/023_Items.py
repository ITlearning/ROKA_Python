# 딕셔너리의 items() 함수와 반복문

example_dic = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

# 딕셔너리의 items() 함수 결과
print("# 딕셔너리의 items() 함수 결과")
print("items() : ", example_dic.items())
print()

# for 반복문과 items() 함수 조합해서 사용
print("# for 반복문과 items() 함수 조합해서 사용")

for key, element in example_dic.items() :
    print("dic[{}] = {}".format(key,element))