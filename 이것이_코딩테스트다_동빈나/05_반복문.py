# 반복문
# for
# while
# 코테에선 무한 루프 잘 안씀

# for문 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# in 뒤에 오는 자료형(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
# 차례대로 하나씩 말고 n칸 간격으로 방문하고 싶다면 3번째에 스택값 넣자 (ex) range(1, 100, 3) .. 1, 4 ,7 ...
# 주로 range() 사용
# range(시작 값, 끝 값)
# range(10)처럼 인자를 하나면 넣으면 자동으로 시작 값은 0부터


# 학생들의 합격 여부 판단2 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 특정 번호의 학생은 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4} # index 2, 4번 학생 제외

for i in range(5):
    if i + 1 in cheating_student_list: # i + 1 : index 01234 -> 12345
        continue
    if scores[i] >= 80: # 1_90, 2_85, 5_97 이지만 앞에서 2, 4번 제외했으니 1, 5번만 남는다.
        print(i + 1, "번 학생은 합격입니다.")

# 중첩 반복문 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 구구단
for i in range(2, 10): # 2 ~ 9단
    for j in range(1, 10): # 단마다 1 - 9 곱하기
        print(i, "x" ,j, '=', i * j)
    print()
