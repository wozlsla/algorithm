a = [1, 2, 3]
b = a

if a == b:
    print("a와 b 는 값이 같다")

if a is b:
    print("a와 b 는 정체성이 같다")

c = [1, 2, 3]
if a == c:
    print("a와 b 는 값이 같다")
if a is c:
    print("a와 b 는 정체성이 같다")
