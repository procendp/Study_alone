# 자료구조의 변경
#커피숍

menu = {"coffee", "milk", "juice"}
print(menu, type(menu)) # {'milk', 'coffee', 'juice'} <class 'set'> .. type_집합(set) {}

#type 변경
menu = list(menu) 
print(menu, type(menu)) # ['coffee', 'milk', 'juice'] <class 'list'> ..type 변경_리스트(list) []

menu = tuple(menu) 
print(menu, type(menu)) # ('juice', 'coffee', 'milk') <class 'tuple'> ..type 변경_튜플(tuple) ()

menu = set(menu)
print(menu, type(menu)) # # {'milk', 'coffee', 'juice'} <class 'set'> .. type 변경_집합(set) {}