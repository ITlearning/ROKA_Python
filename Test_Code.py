# 테스트 페이지입니다.
# 약간의 실습이나 문제가 생겼을 경우 사용합니다.

output = [num for num in range(1,101) if "{:b}".format(num).count('0') == 1 ]

for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: ",sum(output))