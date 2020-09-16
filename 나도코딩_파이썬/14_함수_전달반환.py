# 함수 정의 형태.
# def open_account():

def open_account(): # 전달값 없는 경우
    print("새로운 계좌가 생성되었습니다.") # 아무것도 출력 안됨. 함수는 정의만 해주는 것. 호출 전까지는 안됨.

open_account() # 이제서야 함수가 호출되어 출력된다.


# 전달값과 반환값
# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 두 개 값 리턴도 가능

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))