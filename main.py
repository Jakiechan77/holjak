print("오징어게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

import random
a = random.randint(1,10)
print(a)

my = "짝" 
print(my)

dab = ""
if a % 2 == 0:
    print("짝")
    dab = "짝"
else:
    print("홀")
    dab = "홀"

if my == dab:
    print("맞다 통과")

else:
    print("빵!!")