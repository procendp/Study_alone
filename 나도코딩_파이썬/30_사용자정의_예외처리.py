# 사용자 정의 예외처리
# 직접 class를 내장되어있는 에러 외에 표시하고 싶은대로 에러 표시하게끔 꾸미기.

# class 작성
# class BigNumberError(Exception): # Exception 상속받음
#     pass

### 어떤 값 받았는지도 표시해주기 위해선? <메세지 넣어주기>
class BigNumberError(Exception): 
    def __init__(self, msg):
        self.msg = msg
    
    def __str___(self): ### string 반환 위함
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >= 10 or num2 >= 10: 
        # raise BigNumberError # 이 부분을 class로 받기
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) ### 여기에 바로 msg 적어주기.
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# except BigNumberError:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err: ### msg 확인.
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
# finally
# 예외처리 구문 중에서 정상적으로 실행되 건, 실행되지 않 건 간에 무조건 실행해주는 구문