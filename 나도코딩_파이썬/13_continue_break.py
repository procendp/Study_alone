# continue
absent = [2, 5] # 2, 5번 결석일 때, 제외하고 출석 부르게 하는.
nobook = [7]
for student in range(1, 11) : # 1 ~ 10번까지 출석번호 있음
    if student in absent : # student가 absent에 포함됐다면, 즉, 결석했다면 continue.
        continue # continue 만나면 내려가지 않고 다음 반복으로.
    elif student in nobook:
        print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
        break # break을 해줌으로써, 더 돌아가지 않고, 7번 마친 후 끝낸다.
    print("{0}, 책을 읽어봐".format(student)) # 그렇지 않으면 프린트.. 1, 책을 읽어봐.. 3, 책을 읽어봐 .....
