# 랜덤하게 abs()명의 키와 몸무게 만들기
# 랜덤한 숫자를 만들기 위해 가져온다.
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file :
    for i in range(10) :
        name = random.choice(hanguls) + random.choice(hanguls)
        weigth = random.randrange(40, 100)
        heigth = random.randrange(140, 200)
        
        # 텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weigth, heigth))