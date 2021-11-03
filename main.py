print("오징어게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")
import random
a = random.randint(1,10)

for i in range(2):
    my =input("짝 또는 홀 입력 잘못쓰면 빵이지만 한번은 기회줄게 ")
    print("입력된 값은")
    print(my)
    if my == "홀" or my == "짝":
        dab = ""
        if a % 2 == 0:
            print("결과는 짝")
            dab = "짝"
        else:
            print("결과는 홀")
            dab = "홀"
        if my == dab:
            print("맞음 통과")
        else:
            print("틀림 빵!")
    else:
        print("잘못 입력 다시 입력해라")