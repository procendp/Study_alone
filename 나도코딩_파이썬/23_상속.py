# 상속
# 물려받음.. Unit과 AttackUnit이 겹치는 부분이 있지. 이걸 상속으로 묶자

# 일반 유닛
class Unit: # 부모
    def __init__(self, name, hp): 
        self.name = name 
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 자식 : (Unit) 해줌으로써 상속받음.. self.name, self.hp
    def __init__(self, name, hp, damage): 
        # self.name = name 
        # self.hp = hp
        Unit.__init__(self, name, hp) # Unit에서 name, hp 상속받음.
        self.damage = damage # 거기에 추가로 damage도 적어줄 수 있겠지.
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self.name, self.damage : AttackUnit __init__ 내 변수 출력
                                                       # location : attack 내 변수 출력
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


#############################################################
# 다중 상속
# 여러 부모한테서 받는다, 즉 부모가 여럿

# 드랍쉽 : 공격 기능은 없지
class Flyable: # 날 수 있는 기능을 가진 class
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 애가 하는 일은 딱히 없어. 단지, AttackUnit과 Flyable class를 상속받아서 초기화 해줬을 뿐
    def __init__(self, name, hp, damage, flying_speed): # attack : name, hp, damage .. flyable : flying_speed
        AttackUnit.__init__(self, name, hp, damage) # 공격 가능한 class
        Flyable.__init__(self, flying_speed) # 공중 유닛 class
        # 이렇게 초기화 하게 되면, 두 class에 있는 걸 합치게 되고, 두 class를 안쓰고 이 class만 써도 돼.

# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")