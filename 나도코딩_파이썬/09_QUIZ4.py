# #QUIZ4
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
lst = range(1, 21) # 1 ~ 20까지 숫자 생성 ..but, range type임. list로 쓸거니까 바꿔줘야함.
lst = list(lst) # type을 list로 변경

shuffle(lst) # 무작위로 섞음

winners = sample(lst, 4) # sample : 추출.. 4명 <1명은 치킨, 3명은 커피>

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # 편의상 0번째 사람을 치킨 당첨자로 하자. 어차피 shuffle 해서 랜덤
print("커피 당첨자 : {0}".format(winners[1:])) # 4명 중 0번째 제외, 1번째부터 끝까지.. 총 3명 추출
print("-- 축하합니다 --")