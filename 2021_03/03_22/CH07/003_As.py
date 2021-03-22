# as 구문
# 모듈을 가져올 때 이름 충돌이 발생하는 경우가 있을 수 있다.
# 추가로 모듈의 이름이 너무 길어서 짧게 줄여 사용하고 싶을 때도 있을 것이다.
# 이럴때 as 구문을 사용한다.
import math as m
print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))