# 예외처리
# 어떤 에러가 발생했을 때, 처리해주는 방법
# !!!에러 나면 보통 프로그램 종료되는데, 그걸 막음으로써 프로그램의 완성도를 높일 수 있다.!!!

# print("나누기 전용 계산기")
# num1 = int(input("첫 번째 숫자를 입력하세요 : "))
# num2 = int(input("두 번째 숫자를 입력하세요 : "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) # 6, 삼 -> ValueError ..
#                          # 6/ 3 = 2는 되지만 6 / 삼 은 안됨. 이런 거 다 처리해주는 게 예외처리.

try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.") 
    # [try: .. except ValueError:] 사용함으로써 에러 발생 시 문구로 처리 가능.
    # try 실행 중에 문제 발생 시, except 부분 찾고 해당 에러가 있다면 그거 출력.
# 6 / 0 에러.
except ZeroDivisionError as err:
    print(err) # as err 사용함으로써 에러 문구 그대로 보여줌.

# 이 외의 오류 발생이면 여기 출력.
# except:
#     print("알 수 없는 오류가 발생했습니다.")

# 이 외 오류가 뭔지 보고프면
except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err)
