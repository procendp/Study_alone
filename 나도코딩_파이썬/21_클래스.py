# # 스타크래프트
# # 마린
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 실제 게임에서 유닛은 수백개 만들어질 수 있는데 매번 tank3_ ..처럼 만들 수 없잖아. 그래서 class 가 필요.


# 클래스
class Unit:
    def __init__(self, name, hp, damage): # __init__ : 객체 생성할 때 꼭 필요한 생성자.
        self.name = name # .name, .hp, .damage .. 이런 것들이 멤버변수, 즉, 클래스 내에서 활용 가능한 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) # marine, tank 는 class Unit의 instance
# marine3 = Unit("마린")
# marine4 = Unit("마린", 40) # 이렇게 함수 내 정의된 변수에 맞게 사용하지 않으면 error.

# 멤버변수
wraith1 = Unit("레이스", 80, 5) # wraith1의 변수를 class Unit을 이용하여 만듬
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버 변수를 외부에서 쓰기

# 마인드 컨트롤로 빼앗은 레이스
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 빼앗은 레이스에 한해 클로킹 개발

if wraith2.clocking == True: # if wraith1.clocking == True: 이라면 에러. wraith1이 걸린 Unit 클래스엔 클로킹 없어.
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
