# if

# weather = "rain"
# weather = "dust"
# weather = "sunny"
# weather = input("오늘 날씨 어때?") # input은 scanf와 비슷한 역할. input 속을 프린트 후, 터미널에 기입 가능. 값에 따라 결과 다르게 출력.
# if weather == "rain" or "snow": # or weather == "snow"나, or "snow"나 같음. or로 해당하는 값을 더 넣어줄 수 있음.
#     print("우산 챙겨")
# elif weather == "dust" : # elif = else if
#     print("마스크 챙겨")
# else :
#     print("준비물 필요 없어")
# print()

temp = int(input("기온 어때?" )) # 기온은 정수형태니까 int 감싸자.
if 30 <= temp :
    print("hot")
elif 10 <= temp and temp < 30 :
    print("good")
elif 0 <= temp < 10 : # and와 같은 표현
    print("cold")
else :              # -20과 같이 음수도 가능.
    print("bad")