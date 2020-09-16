# super
# 다중 아닌 기본 1개짜리 상속의 초기화 시 간편한데, 그냥 다 초기화 해주자.
# 형태는 super().__init__(name, hp, 0) 형태.
# 원래는 Unit.__init__(self, name, hp, 0)이지.....   super()와 뒤에 self 빼주는 차이.
# 걍 초기화 다 해서 쓰자!

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__() # Unit 생성자

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         super().__init__() # Flyable 생성자   ... 이렇게 super()를 쓰면 다중상속 못하고 앞 것만 받아.
                                                    # 다중상속일 땐, super 쓰지마.

# 다중 상속엔 이렇게
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self) # super 쓰지말고 둘 다 초기화 해주자.
        
# 드랍쉽
dropship = FlyableUnit()