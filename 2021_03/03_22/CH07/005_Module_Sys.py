# sys 모듈
# 시스템과 관련된 정보를 가지고 있는 모듈이다.
# 근데 구름 IDE 는 리눅스 기반이라 돌아가지 않는다... 추후 찾아봄.
import sys

print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion():", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)


# 프로그램을 강제로 종료합니다.
sys.exit()