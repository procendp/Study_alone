# Python에서 파일 열기

# 쓰기
# score_file = open("20_score.txt", "w", encoding="utf8") # w : 쓰기목적, utf8 : 한글 정보 위해 웬만하면 써주자.
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 닫아주기까지 해줘야함. //score 파일 생김.

# 추가 및 수정하기
# score_file = open("20_score.txt", "a", encoding="utf8") # a : append_추가하기.
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 읽기
# score_file = open("20_score.txt", "r", encoding="utf8")
# print(score_file.read())    # 한 번에 다 불러오기.
# score_file.close()

score_file = open("20_score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동(공백).. 붙이고 싶다면 end=""
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 파일에 4줄이 기입되어 있는 걸 아니까 4줄로 쓸 수 있지만 모른다면?

# while
# while True:
#     line = score_file.readline() # 무한 while 돌리고,  line 아닌 경우 ,break. line이면 프린트.
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# for
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

#############################################################################
# pickle
# 프로그램 상에서 우리가 사용하고 있는 데이터를 파일형태로 저장해주는 것

import pickle
# 쓰기
# profile_file = open("20_profile.pickle", "wb") # wb : write + binary, pickle에서는 2진으로 표시해줘야함.
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장, pickle 사용 시 꼭 해줘야 함.
# profile_file.close()

# 읽기
profile_file = open("20_profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with
# 읽기
with open("20_profile.pickle", "rb") as profile_file: # 연 파일 정보를 profile_file에 저장
    print(pickle.load(profile_file))
    #close 필요 없음.

# 쓰기
with open("20_study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부중")                                   # 단 2줄로 끝남.