#QUIZ3
# 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"(!) 로 구성
# 예) 생성된 비밀번호 : nav51!

domain  = "http://naver.com"
# domain  = "http://google.com"
# domain  = "http://daum.net"
# domain  = "http://youtube.com"
rule1 = domain.replace("http://", "") # 규칙1 ...자르는 방법
#print(rule1)
rule2 = rule1[:rule1.index(".")] # 규칙2
#print(rule2)
rule3 = rule2[:3] + str(len(rule2)) + str(domain.count("e")) + "!" # 규칙3
print("url : {}의 의해 생성된 비밀번호 : {}" .format(domain, rule3))
