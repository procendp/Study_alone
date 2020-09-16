# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

#     profile("유재석", 20, "파이썬")
#     profile("김태호", 25, "자바")
    # 이렇게 다른 경우가 아닌 같은 경우는?
    
# 같은 학교 같은 학년 같은 반 같은 수업. 
# def profile(name, age = 17, main_lang = "파이썬"): # 이렇게 직접 넣어주면 그것만 나옴
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)
    
profile(main_lang = "파이썬", name = "유재석", age = 20) # 이렇게 순서 뒤바뀌어도 가능.

