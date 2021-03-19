# 테스트 페이지입니다.
# 약간의 실습이나 문제가 생겼을 경우 사용합니다.

앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 100
memo = {}

def 문제(남은사람수, 앉힌사람수) :
    key = str([남은사람수, 앉힌사람수])
    
    #종료조건
    if key in memo :
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0 :
        return 1
    #재귀 처리
    for i in key :
        