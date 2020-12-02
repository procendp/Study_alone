# 함수 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 특정 작업 단위로 묶어 놓는 것
# 코드를 줄일 수 있음
# 내장 함수 : 표준 라이브러리에 포함되어 기본적으로 제공하는 것
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 매개변수 : 함수 내부에서 사용할 변수
# 반환 값 : 함수에서 처리 된 결과를 반환  .. 꼭 있어야하는 건 아냐

def add(a, b): # a, b가 매개변수

    return a + b

# global 키워드
# 함수 밖에 선언된 변수를 참조함

c = 8
def func():
    global c # 이거 없이 밑줄처럼 c += 1 하면 오류남. 매개변수 없기 때문에 c가 정의되어있지 않음.           #%%%% 전역변수가 리스트라면 글로벌 리스트값 없어도 됨. 주소값 이용하니까 함수 안에 c[2] = 7 해도 알아들음
    c += 1

for i in range(10):
    func()

print(c) # 18


# 패킹 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def operator(a, b):
    return a + b, a - b, a * b, a / b

a, b, c, d = operator(3, 7) # a, b, c, d에 operator 함수 리턴 값이 패킹되어 매칭되어 있는 것. 파이썬은 이렇게 여러가지도 가능
print(a, b ,c, d) # 10 -4 21 0.42857142857142855



# 람다 표현식 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 함수를 매우 간단하게 작성
# 정렬에도 잘 쓰임

print((lambda a, b: a + b)(3, 5)) # 8   .. a와 b를 매개변수로 받아서 a + b로 리턴하는 함수를 손쉽게 만듦 

