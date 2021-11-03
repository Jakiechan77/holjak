print("오징어게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

import random
A = random.randint(1,10)
B =input("짝 또는 홀을 입력하세요")
print("입력된 값은")
print(B)

C = ""
if a % 2 == 0:
    print("결과는 짝")
    C = "짝"
else:
    print("결과는 홀")
    C = "홀"

if B == C:
    print("맞다 통과")

else:
    print("틀림 탈락")