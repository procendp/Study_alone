# 튜플
# 리스트와는 다르게 내용 변경, 추가 안됨
# 리스트보다 속도 빠름
# 변경 사항 없을 때, 쓰기 좋음.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
print()
#menu.add("생선까스") .. error

#다른 변수, 함께 나열 가능.
# name = "kim"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

(name, age, hobby) = ("kim", 20, "coding")
print(name, age, hobby)

############################################################################
# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3} .. 중복 허용 x
print()

java = {"you", "kim", "yang"}
python = set(["you", "park"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # {'you'}
print(java.intersection(python)) # {'you'}
print()

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python) # {'kim', 'park', 'you', 'yang'}
print(java.union(python)) # {'kim', 'park', 'you', 'yang'} .. 순서는 보장되지 않는다.
print()

# 차집합 (java는 할 수 있지만, python은 할 줄 모르는 개발자)
print(java - python) # {'yang', 'kim'}
print(java.difference(python)) # {'yang', 'kim'}
# 이 때, python 교육으로 할 줄 아는 사람이 늘어남
python.add("kim")
print(python) # {'kim', 'you', 'park'}
# java 까먹은 kim
java.remove("kim")
print(java) # {'yang', 'you'}