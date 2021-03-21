# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    # 여러 가지 처리를 수행한다.
    예외.발생해라ㅋㅋ()
    # 파일을 닫습니다
    file.close()
except Exception as e:
    print(e)
    
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 예외가 발생할경우 파일을 제대로 닫지 못하고 예외가 출력이 된다.