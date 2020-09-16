# 사전
#캐비넷에 키 값과 함께 내용 저장

#key가 정수일 때
cabinet = {3:"유재석", 100:"김태호"} # 3번 key에 유재석 저장, 100번 key에 김태호 저장
print(cabinet[3]) #출력방법 1
print(cabinet[100]) 
print(cabinet.get(3)) # 출력방법 2
#print(cabinet[5]) # 에러남. KeyError : 5 // 키값 5가 없기 때문. 여기부터 뒤에 프로그램들도 다 안 돌아감.
print(cabinet.get(5)) # None ..얘는 오류 안 내고 다르게 출력함.
print(cabinet.get(5, "사용 가능")) # 사용 가능 .. 5번 키는 비어있으나 사용 가능으로 대체하여 출력됨.

print(3 in cabinet) # True .. 3이 캐비넷이 있는가?
print(5 in cabinet) # False
print()


#key가 문자일 때
cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print()
#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'c-20': '조세호'} .. 이렇게 추가, 삭제 된다.
print()
#떠난 손님
del cabinet["A-3"] # {'B-100': '김태호', 'c-20': '조세호'} ..A-3 삭제
print(cabinet)
print()
#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key, value 다 출력
print(cabinet.items())
print()

#캐비넷 비우기
cabinet.clear()
print()

