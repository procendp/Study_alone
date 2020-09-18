#########문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요."
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)
print()

#슬라이싱
##문자열 중 필요부분만 가져오기
jumin = "990120-1234567"

print("성별 : " + jumin[7]) #뒷자리 1 가져오기 위한 7... index는 마찬가지로 0부터.
print("연 : " + jumin[0] + jumin[1]) #맨앞 두자리
print("연 : " + jumin[0:2]) #index 0이상 2미만까지.. 위랑 같음
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) 
#print("생년월일 : " + jumin[0:6]) 둘 다 같다. 맨 앞 0은 생략가능.
print("뒤 7자리 : " + jumin[7:])
#print("뒤 7자리 : " + jumin[7:14]) 이것 또한 위와 같다. 맨 뒤는 생략가능.
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) #맨 뒷자리는 -1번째이다. 따라서 -7번째는 1이고, -7 -6 -5... -1 출력