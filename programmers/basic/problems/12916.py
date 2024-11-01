def solution(s):

    if len(s) < 1:
        return True

    s = s.lower()
    is_p = s.count("p")
    is_y = s.count("y")

    if is_p != is_y:
        return False

    return True


def solution(s):
    """
    - 빈 문자열("")에도 lower()와 count() 적용 가능
    - s.lower()의 결과를 s에 다시 할당 : 메모리에 새로운 객체를 생성하는 추가 작업 발생

    s.lower()를 자주 사용해야 할 경우, 미리 변환된 값을 s에 할당해두면, 매번 lower()를 호출하지 않아 효율적일 수 있으나 이 문제에서는 변환된 문자열이 오직 count() 호출에만 사용되므로, 굳이 s.lower() 값을 별도로 할당할 필요가 없다. 메모리 사용 면에서 비효율적.
    """

    s = s.lower()
    if s.count("p") != s.count("y"):
        return False

    return True


def solution(s):
    return s.lower().count("p") == s.lower().count("y")


s = "pPoooy"
s = "Pyy"
s = ""

print(solution(s))
