# 리스트 []
# 순서를 가지는 객체 집합

#지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)
print()

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append : 맨 뒤에 추가
print(subway)

# 정형돈을 유재석과 조세호 사이에 태워봄
subway.insert(1, "정형돈") # insert( , ) : 삽입... 어디에, 무엇을.
print(subway)
print()

# 지하철에 있는 사람을 뒤에서부터 한 명씩 꺼냄
print(subway.pop()) # 어떤 사람이 꺼내졌는지 확인 가능 - 하하
print(subway) # 팝 이후의 결과
# print(subway.pop()) # 박명수
# print(subway)
# print(subway.pop()) # 조세호
# print(subway)
print()

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print()

#정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort() # .sort : 리스트 정렬(기본 - 오름차순)
print(num_list)

num_list.reverse() # .reverse : 내림차순 정렬
print(num_list)

#모두 지우기
num_list.clear()
print(num_list) # []
print()


# 다양한 자료형 함께 사용
num_list = [5, 4, 3, 2, 1]
mix_list = ["조세호", 20, True]
#print(mix_list)

#리스트 확장
num_list.extend(mix_list) # .extend : 확장, 리스트 합치기
print(num_list)