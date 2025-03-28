sel = int(input('1.입력한 수식 계산 2. 두 수 사이의 합계: '))
if sel == 1:
    num = input("수식을 입력하세요: ")
    result = eval(num)
    print(f"{num} 결과는 {result}입니다.")

else:
    num1 = input("첫 번쨰 숫자를 입력하세요:")
    num2 = input("두 번쨰 숫자를 입력하세요:")
    result = sum(range(int(num1), int(num2)+1))
    print(f"{num1}+...+{num2}는 {result}입니다.")