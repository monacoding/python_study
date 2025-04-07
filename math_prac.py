import math 

#제곱근
print("제곱근 \u221A16:",math.sqrt(16))

#로그 
print("자연로그log(e):",math.log(math.e))

#로그 (밑 10)
print("로그 log10(1000):",math.log10(1000))

#삼각함수 
print("사인 sin(\u03c0/2):",math.sin(math.pi/2))
print("코사인 cos(0):", math.cos(0))

#올림/ 내림/ 반올림
print("올림 ceil(2.3):",math.ceil(2.3))
print("내림 floor(2.7)",math.floor(2.7))
print("절대값 fabs(-5):",math.fabs(-5))

#팩토리얼 
print("팩토리얼 5!",math.factorial(5))

#무한대 
print("무한대:",math.inf)

#라디안 <-> 도 단위 변환
print("90도 -> 라디안:",math.radians(90))
print("\u03c0 라디안 ->도",math.degrees(math.pi))

#빗변 구하기(피타고라스 정리 )
print("빗변 길이 (3,4) :",math.hypot(3,4))

# 소수부와 정수부 분리
x = 5.678
frac, whole = math.modf(x)
print(f"{x}의 정수부:{whole},소수부:{frac}")