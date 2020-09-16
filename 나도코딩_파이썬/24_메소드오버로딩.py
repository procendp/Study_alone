# 연산자 오버로딩
# 자식 class에서 메소드를 쓰고 싶을 때, 메소드를 새롭게 정의해서 쓰는 법.


# 일반 유닛
class Unit: 
    def __init__(self, name, hp, speed): # 지상유닛에 대한 speed 정보가 없어서 넣어줌
        self.name = name 
        self.hp = hp
        self.speed = speed  # speed 추가하는 순간, 상속 받은 자식들에게도 오류 나니 다 수정해줘야해.
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 드랍쉽 : 공격 기능은 없지
class Flyable: # 날 수 있는 기능을 가진 class
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed): 
        AttackUnit.__init__(self, name, hp, 0, damage) # 0 넣는 이유 : 위 Unit에서 지상유닛관련 speed 추가했고, 공중유닛 speed는 밑에 해줬으므로 의미 없으니 0으로 초기화 
        Flyable.__init__(self, flying_speed) # 공중 유닛 class
        # 이렇게 초기화 하게 되면, 두 class에 있는 걸 합치게 되고, 두 class를 안쓰고 이 class만 써도 돼.
    
    # @@@아래부분.
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 문제는 이렇게 쓰면, 지상유닛인지, 공중유닛인지 매번 확인해서 함수써야해..불편
# 따라서 연산자 오버로딩을 통해 똑같이 move함수를 쓰면 지상, 공중 유닛 이동 가능하게 하자.
# @@@바로 FlyableAttackUnit 함수에 move함수를 새롭게 정의하는 것. <재정의>
vulture.move("11시")
battlecruiser.move("9시")