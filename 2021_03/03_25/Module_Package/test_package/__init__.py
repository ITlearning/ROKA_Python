# "from test_package import *"로
# 모듈을 읽어 들일 때 가져올 모듈
__all__ = ["module_a", "module_b"] # 사용시 읽어들일 모듈의 목록

print("test_package를 읽어 들였습니다.")