# finally 구문 사용해 파일 닫기
try:
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    예외.발생()
    file.closed()
except Exception as e:
    print(e)
finally:
    file.close()
    
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 예외가 발생할 경우 파일을 닫지 않고 프로그램이 끝나기 마련이다.
# 따라서 finally 구문을 사용하여 무조건 파일을 닫게끔 코딩해야한다.