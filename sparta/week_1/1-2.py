def sol(num):
    if num % 2 != 0:
        return "홀수입니다"
    return "짝수입니다"


while 1:
    num = int(input("Num: "))
    if num > 0:
        break
    else:
        print("정수를 입력해주세요")

print(sol(num))
