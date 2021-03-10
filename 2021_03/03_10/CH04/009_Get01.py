# 키가 존재하지 않을 때 None을 출력하는지 확인하기
dic = { 
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근해 봅니다.
value = dic.get("존재하지 않는 키")
print("값 : ", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")