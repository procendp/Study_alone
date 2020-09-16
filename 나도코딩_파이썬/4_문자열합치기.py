#########문자열 합치기

#기본
print("a" + "b")
print("a", "b") # 콤마하면 공백1

#다른 방법 1
print("나는 20살입니다.")
print("나는 %d살입니다." % 20) #c처럼 콤마찍지 마!!!!
print("나는 %s을 좋아해요." % "파이썬") # %s는 문자도 정수도 다 받는다.
print("Apple 은 %c로 시작해요." % "A") # %c는 한글자만 받는다.
print("나는 %s색과 %s색을 좋아해요." % ("파란", "노란")) #둘 이상
print()

#다른 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "노란")) # 0번째, 1번째로 자리지정 가능
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "노란")) # 순서 교차 가능
print()

#다른 방법 3
print("나는 {age}살이며 {color}색을 좋아해요." .format(age = 20, color = "노란"))
print("나는 {age}살이며 {color}색을 좋아해요." .format(color = "노란", age = 20)) # 상관없지만 이렇게도 표현 가능
print()

#다른 방법 3
age = 20
color = "노란"
print(f"나는 {age}살이며 {color}색을 좋아해요.") # f를 앞에 씀으로써 앞서 선언한 변수들 입력 가능..f하고 공백 no!