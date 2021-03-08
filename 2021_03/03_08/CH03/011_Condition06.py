# 유머를 조건문으로 구현하기(1)

secore = float(input("학점 입력 > "))

if secore == 4.5 : 
    print("신")
elif 4.2 <= secore :
    print("교수님의 사랑")
elif 3.5 <= secore :
    print("현 체제의 수호자")
elif 2.8 <= secore :
    print("일반인")
elif 2.3 <= secore :
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= secore :
    print("오락문화의 선구자")
elif 1.0 <= secore :
    print("불가촉천민")
elif 0.5 <= secore :
    print("자벌레")
elif 0 <= secore :
    print("플랑크톤")
else :
    print("시대를 앞서가는 혁명의 씨앗")