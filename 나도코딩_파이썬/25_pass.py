# pass
# 뭘 아직 적지 않아도 완성된 것처럼 행동하게 함. 오류 안나게.


# 일반 유닛
class Unit: 
    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp
        self.speed = speed  
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 건물
class BulidingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # init 함수에서 뭘 아직 하지 않았지만, pass를 적음으로써 오류 안나게 함(일단 완성된 것 처럼).

#서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
suppply_depot = BulidingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over() # pass 때문에 오류 x