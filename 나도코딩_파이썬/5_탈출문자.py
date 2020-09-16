#########탈출 문자

# print("백문이 불여일견 
# 백견이 불여일타")         ...이렇게 하면 오류 남. \n 사용해
print("백문이 불여일견\n백견이 불여일타")
print()

# \" \' : 문장 내에서 따옴표
#저는 "정무현"입니다.
print("저는 '정무현'입니다.") # 해도 되지만, 원하는 값은 아니지.
print('저는 "정무현"입니다.') # 이렇게 하면 원하는 값을 출력할 순 있어.
print("저는 \"정무현\"입니다.") # 하던 대로 큰따옴표로 이루어지면, 좌우 단어들이 잡혀서 문젠데, 역슬래시 해주면 괜찮다.
print()

# \\ : 문장 내에서 \
#print("C:\Users\jlppo\Desktop\VS CODE\Coding_Study_Project\PythonWorkspace") ...이러면 에러나지.
print("C:\\Users\\jlppo\\Desktop\\VS CODE\\Coding_Study_Project\\PythonWorkspace") # 쓰고프면 두개씩 넣자.
print()

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 이렇게 하면 Red Apple 읽고, \r 만나서 커서가 맨 앞으로 감
                         # 맨 앞에서 Pine이 Red를 덮어써서 결과적으로 ----> PineApple 출력.
print()

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple
print()

# \t : 탭 역할
print("Red\tApple") # Red   Apple
print()