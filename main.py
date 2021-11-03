print("오징어게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

import random
a = random.randint(1,10)
my =input("짝 또는 홀을 입력하세요")
print(my)

b = ""
if a % 2 == 0:
    print("결과는 짝")
    b = "짝"
else:
    print("결과는 홀")
    b = "홀"

if my == b:
    print("맞다 통과")

else:
    print("틀림 탈락")