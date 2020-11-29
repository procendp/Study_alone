# 50 지출-> 10 할인
# 클래스 문법 확인
# 마지막 테케 확인

class Solution:
    def solution(self, goods):
        self.goods = goods

    def calculate(self):
        over = []   # 50 이상
        under = []  # 50 미만
        cnt = 0

        for i in range(len(self.goods)):
            if self.goods[i] >= 50:
                over.append(self.goods[i] - 10)
                cnt += 1
            else:
                under.append(self.goods[i])
                if sum(under) >= 50:
                    cnt += 1

        return sum(self.goods) - (cnt * 10)



    print(calculate([46,62,9])) # 97
    print(calculate([50,62,93])) # 175
    print(calculate([5,31,15])) # 41
    print(calculate([5,3,15])) # 23








# 50 이상이면 10 할인

# def solution(goods):
#     over = []   # 50 이상
#     under = []  # 50 미만
#     cnt = 0

#     for i in range(len(goods)):
#         if goods[i] >= 50:
#             over.append(goods[i] - 10)
#             cnt += 1
#         else:
#             under.append(goods[i])
#             if sum(under) >= 50:
#                 cnt += 1

#     return sum(goods) - (cnt * 10)

# print(solution([46,62,9])) # 97
# print(solution([50,62,93])) # 175
# print(solution([5,31,15])) # 41
# print(solution([5,3,15])) # 23
# print(solution([49,49,49])) # 127.. 137이어야 하는데..