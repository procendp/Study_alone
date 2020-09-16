# 표준 입출력
print("1", "2", sep="vs") # 그 동안 ,를 하면 빈 공백이 나옴.

# sep = " "
# ,의 공백을 원하는 값으로 채움.
print("1", "2", sep="vs") # 1vs2
                          
# end = " "
# 개행없이 이어지게 쓰고, 공백 원하는 값으로 채우기.
print("1", "2", end="?" )
print("무엇이 더 큰가?")


#####
# import sys
import sys
print("1", "2", file = sys.stdout) # 1 2
print("1", "2", file = sys.stderr) # 1 2
# VScode 상에선 똑같아 보이지만, sys.stdout은 표준출력으로 나타내고, sys.stderr는 표준에러로 처리가 된다.
# 로그처리를 따로 할 때, 에러같은 경우엔 따로 처리할 수 있게 해주는.

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # items 하면 key(subject)값과 value(score)값을 둘 다 가져온다.
    # print(subject, score)
    """
    수학 0
    영어 50
    코딩 100          ..정렬하고 싶다면 ljust 같은 거 쓰자.
    """
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    """
    수학          0     ..subject에 8칸 확보하고 좌측정렬, score에 4칸 확보하고 우측정렬
    영어         50     ..score는 숫자니까 정렬 위해서 문자열 처리 str.
    코딩        100     ..sep=":" , 콤마 공백은 : 로.
    """

# 은행 대기순번표
# 001, 002 ... 010, 011 ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(3), 크기 3만큼의 공간을 확보하고 0을 넣어라. 


    ### 참고
    # input() 하면 scanf처럼 입력 받는데, 죄다 string으로 받음. 이 점 유의하자.