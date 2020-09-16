try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    # 에러 발생시키기
    if num1 >= 10 or num2 >= 10: # 한 자리 숫자 나누기 전용 계산기를 만들 거니까, 어떤 수든 10이상이 입력되면 안되겠지.
        raise ValueError # 그 때 에러 발생(raise), 밑에 print로 안가고, 바로 except ValueError: 찾아감.
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")