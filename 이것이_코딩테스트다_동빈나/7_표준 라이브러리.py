# 내장 함수
    # print(), input(), sorted() ...
# itertools
    # 순열과 조합 제공
# heapq
    # 힙 기능 제공, 그래프 알고리즘 때 사용할 것
# bisect
    # 이진탐색(binary search) 기능을 제공, 특정 리스트가 정렬되어 있을 때, 그 리스트에서 어떤 값들을 빠르게 찾고자할 때 사용, 코테에서 이진탐색 문제에서 잘 쓰임
# collections
    # 덱(deque)이나 카운터(counter) 같이 유용한 자료구조 알고리즘에 사용





# sum()
# min(), max()

# eval() - 중위표기법 시 사용
result = eval("(3+7+4)*3")
print(result)

# sorted()
# sorted() with key


# 순열, 조합
# 순열 : nPr = n * (n-1) * (n-2) ... * (n-r+1) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합 : nCr = n * (n-1) * (n-2) ... * (n-r+1) / r! ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2)) # 2개를 뽑는 조합
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]


# 중복 순열
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)