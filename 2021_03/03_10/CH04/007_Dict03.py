# 딕셔너리 요소 제거하기
dic = {
    "name": "7D 망고 건조",
    "type": "당절임"
}

print("요소 제거 이전 : ", dic)

# 딕셔너리 요소를 제거합니다
del dic["name"]
del dic["type"]

# 요소 제거 후에 내용을 출력해 봅니다
print("요소 제거 이후 : ", dic)