from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb") # 바이너리 형식으로 쓴다.
file.write(output)
file.close()