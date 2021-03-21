# try except 구문 끝난 후 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생()
except Exception as e:
    print(e)
    
file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed :", file.closed)

# 사실 그냥 닫기만 하면 된다.
# finally 를 무조건 사용해야 된다는 건 말도 안되는 이야기였다.
