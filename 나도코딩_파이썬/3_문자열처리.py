#########문자열 처리 함수
python = "Python is Amazingn"
print(python.lower()) # 다 소문자
print(python.upper()) # 다 대문자
print(python[0].isupper()) # True, index 0번째가 대문자인지? isupper로 확인. 맞으면 T, 틀리면 F
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) #문자열 내 앞 문자를 뒷 문자로 바꿔줌.
print()

#문자열 속 문자 찾기
index = python.index("n") # 문자열 내 n의 위치 확인, 하지만 첫번째 것만 찾고 만다.
print(index) 
index = python.index("n", index + 1) #앞에서 찾은 위치, 그 다음부터 찾기.
print(index)
index = python.index("n", index + 2) #그 다음부터 찾기.
print(index)
print()

print(python.find("n")) # 첫번째 n 찾음
print(python.find("Java")) # -1, 없는 거 찾으면 반환.
#print(python.index("Java")) #오류남..
#print("hi") #오류난 시점부터는 출력 아예 안됨.
print()

print(python.count("n")) # 3, 문자열 내 n이 몇번 나왔는지 세기.