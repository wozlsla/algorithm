# https://school.programmers.co.kr/learn/courses/30/lessons/81301 - 숫자 문자열과 영단어

numbers = {
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
print(numbers.items())
print(type(numbers.items()))


def solution(s):

    result = []
    tmp = ""

    for char in s:
        if char.isdigit():
            result.append(char)
        else:
            tmp += char
            if tmp in numbers:
                result.append(str(numbers[tmp]))
                tmp = ""

    return int("".join(result))


s = "one4seveneight"
s = "23four5six7"
print(solution(s))
