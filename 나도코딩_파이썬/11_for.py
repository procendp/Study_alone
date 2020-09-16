# for 반복문

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# 특별한 값을 순서 정해서 넣었을 때.
for waiting in [0, 1, 2, 3, 4] : 
    print("대기번호 : {0}".format(waiting)) # 0부터 4까지 하나씩 waiting에 넣어 돌리고, 프린트.

# 순차적으로 1 증가 <range 활용>
for waiting in range(5) :
    print("대기번호 : {0}".format(waiting)) # 위와 같은 문장.. range(5).. 0부터 5미만까지.. or range(0,5)


##예제
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks :
    print("{0}님, 커피 준비되었습니다.".format(customer))




# 한 줄 for문
# 출석번호가 1, 2, 3, 4 .. 앞에 100을 붙이기로 함. -> 101, 102, 103, 104...
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students] # students에 있는 i를 하나씩 불러오면서 그 값에 100을 더한 값을 리스트로 불러서 students에 넣어라.
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [len(i) for i in students] # students에 있는 i를 하나씩 불러오면서 그 값을 길이(len)로 변환하여 넣어라.
print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
print(students)
