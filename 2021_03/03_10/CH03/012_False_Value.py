# False로 변환되는 값
# 대표적인 False 변환 값은 빈 컨테이너(0, "", 빈 리스트 등) 이다.

print('# if 조건문에 0넣기')
if 0 : 
    print('0은 True로 변환됩니다.')
else :
    print('0은 False로 변환됩니다.')
    
print('# if 조건문에 빈 문자열 넣기')
if "" :
    print('빈 문자열은 True로 변환됩니다.')
else :
    print('빈 문자열은 False로 변환됩니다.')
