# 지역변수
# 함수 내에서만 쓰여지고 소멸되는

# 전역변수
# 프로그램 어느 곳에서나 사용 가능한

gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    # global gun # 전역 공간에 있는 gun 사용하고 싶다면 이렇게.
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 10, 전역변수 gun 값이 들어갈거고

checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 18, checkpoint 함수 내 지역변수 gun 값이 들어가서 결과값 다름.