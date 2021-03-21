# 파일이 제대로 닫혔는지 확인하기
try:
    file = open("info.txt", "w")
    # 여러 가지 처리를 수행합니다.
    file.write("Hello")
    file.close()
except Exception as e:
    print(e)
    

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed)