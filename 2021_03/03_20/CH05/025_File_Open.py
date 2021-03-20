# 파일 열고 닫기
# 파일에 텍스트를 씁니다.
with open("basic.txt", "w") as file :
    file.write(input())
# 파일을 닫습니다.
# file.close()

# 이렇게 코드를 작성하면 with 구문이 종료될 때 자동으로 파일이 닫힌다.