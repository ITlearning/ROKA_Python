# 딕셔너리 요소에 접근하기
# C++에 map과 비슷하지만, 더 많은 기능. 약간 클래스와 map이 합쳐진 것 같은??

# 딕셔너리를 선언합니다
dic = { 
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}


# 출력합니다
print("name : ", dic["name"])
print("type : ", dic["type"])
print("ingredient : ", dic["ingredient"])
print("origin : ", dic["origin"])

# 값을 변경합니다
dic["name"] = "8D 망고 건조"
print("name : ", dic["name"])

dic["ingredient"][1] = "소금"
print("ingredient : ", dic["ingredient"])