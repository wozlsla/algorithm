from collections import deque


def calc(s):
    """
    eval : 주어진 문자열을 코드로 실행
    - 외부 입력을 그대로 실행 가능하기 때문에 보안 위험 !!
    - 파싱 과정 추가 비용 - 문자열을 토큰으로 분리하고 구문 분석
    """

    s = s.replace(" ", "")

    items = deque()
    nums = deque()

    for i in s:
        if i in ["+", "-", "/", "*"]:
            items.append(i)
        else:
            nums.append(i)

    result = nums.popleft()  # 이건 큐..잖아..
    while nums:
        result = eval(str(result) + items.popleft() + nums.popleft())

    return result


def calc(s):

    s = s.split()
    stack = deque()

    for item in s:
        if item.isdigit():
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()
            if item == "+":
                stack.append(a + b)
            if item == "-":
                stack.append(a - b)
            if item == "*":
                stack.append(a * b)
            if item == "/":
                stack.append(a // b)

    return stack.pop()


def calc(s):
    import operator

    """ Operator """

    stack = deque()
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        # "/": operator.truediv,
        "/": operator.floordiv,
    }

    for item in s.split():
        if item.isdigit():
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[item](a, b))  # operator.add(a, b)
    return stack.pop()


s = "2 3 + 5 *"
s = "4 2 / 3 - 2 *"
print(calc(s))


# print("2".isdigit())  # isdigit은 string 클래스에 있는 메서드

# print([1, 2].popleft()) X
# print(eval("1 * 2"))
# # print(eval("1", "*", "2")) X
# print(eval("1" + "*" + "2"))
