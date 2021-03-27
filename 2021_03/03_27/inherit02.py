# 사용제 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        
raise CustomException