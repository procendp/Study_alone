# while 반복문

customer = "토르"
index = 5
while index >= 1 :
    print("{0}님, 커피 나왔습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1 # index = index - 1
    if index == 0 :
        print("커피는 폐기처분 되었습니다.")

# 무한 루프
# while True :
#     print(" ")


# 토르 올 때까지 부르기
customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}님, 커피 나왔습니다.".format(customer))
    person = input("성함이 어떻게 되세요? ")