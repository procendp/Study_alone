# # 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "해주면 개행없이 다음 프린트를 이어보여줌.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")
# # 이렇게 김태호가 2가지 언어밖에 못하면 번거롭게 나머지 ""로 채워줘야함
# # 유재석이 더 많은 언어를 구사하게 될 수도 있어. 함수 자체를 바꿔줘야하겠지.    => 따라서 가변 인자 활용

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "해주면 개행없이 다음 프린트를 이어보여줌.
    for lang in language:    #lang 변수 선언 후 language 안에 포함된거 하나씩 출력
        print(lang, end=" ") # Python, Java, C .. 나열
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

