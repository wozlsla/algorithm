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
    answer = s  # 불변성 문제로 입력받은걸 수정하지 않는걸 권장
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
            if tmp in nums:  #
                result += str(nums.get(tmp))
                # list의 경우 인덱스를 반환할 수도 있다 ["zero", "one", ...]
                tmp = ""

    return result


# if s[i:i+len(word)] == word:


def solution(s):
    answer = ""
    dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    i = 0
    while i < len(s):
        if s[i].isdigit():  # 숫자인 경우 바로 추가
            answer += s[i]
            i += 1
        else:  # 영단어를 숫자로 변환
            for word, num in dic.items():
                if (
                    s[i : i + len(word)] == word
                ):  # 영단어가 일치하면 # 이 부분 슬라이싱 구성
                    answer += num
                    i += len(word)
                    break

    return int(answer)  # 마지막에 한번더 Int 형으로 전환


s = "one4seveneight"
print(solution(s))

# print("o".isdigit())

# num = "one"
# items = "onetwo"
# items.replace(num, "")
# print(items)
