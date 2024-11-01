nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution(s):
    if len(s) < 1 or len(s) > 50:
        return

    for num in nums:
        if num in s:
            s = s.replace(num, str(nums.get(num)))

    return s


def solution(s):
    answer = s
    for key, value in nums.items():
        answer = answer.replace(key, value)
    return int(answer)


def solution(s):
    """
    1. 숫자면 넘어가고 문자열이라면 다음 숫자가 나올때까지 단어를 보관(save)
    2. 문자열이 딕셔너리의 키와 같은지 확인
    3. 있으면 result에 추가하고 save 초기화
    """
    if s.isdigit():
        return int(s)

    nums = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    tmp = ""
    result = ""

    # 숫자만 남을 때까지

    for i in s:
        if i.isdigit():
            result += i
        else:
            tmp += i
            if tmp in nums:
                result += str(nums.get(tmp))
                # list의 경우 인덱스를 반환할 수도 있다 ["zero", "one", ...]
                tmp = ""

    return result


s = "one4seveneight"
print(solution(s))

# print("o".isdigit())

# num = "one"
# items = "onetwo"
# items.replace(num, "")
# print(items)
