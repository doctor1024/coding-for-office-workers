#구구단 표를 만들어 봅시다!

#Jinhyung's solution
# dan = 출력을 요청한 단
# a = 1 부터 9까지 곱하는 수
# res = 곱한 결과 값

dan = input("몇 단을 출력 하시겠습니까? ")
a = 1

while a < 10:
    res = int(dan) * a
    print ("{} X {} = {}".format(int(dan), a, res))
    a = a + 1

# marco's solution
# 1) 사용자로부터 몇 단을 출력할지 받을 것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1:10)
    print ("{} * {} = {}".format(dan, num, dan * num)

# review
# 1) dan의 int 미처리
# 2) format 사용법 몰랐음
