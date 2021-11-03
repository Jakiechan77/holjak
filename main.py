print("오징어게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

import random
a = random.randint(1,10)
b =input("짝 또는 홀을 입력하세요")
print("입력된 값은")
print(b)

c = ""
if a % 2 == 0:
    print("결과는 짝")
    c = "짝"
else:
    print("결과는 홀")
    c = "홀"

if b == c:
    print("맞다 통과")

else:
    print("틀림 탈락")