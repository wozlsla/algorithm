def solution(t, p):
    """
    Slicing 반복 사용 (새 객체 생성 - 메모리 추가 할당)
    Python) list의 길이를 따로 저장. Slicing에서도 해당 객체의 len 속성으로 저장 됨.
    """

    cnt = 0
    st, ed = 0, len(p)

    while len(t[st:ed]) == len(p):
        if int(t[st:ed]) <= int(p):
            cnt += 1

        st += 1
        ed += 1

    return cnt


def solution(t, p):
    """
    Slicing Window
    불필요한 변환 작업들 줄이기
    """

    cnt = 0
    window = len(p)
    p = int(p)

    # idx 같이 사용. st, ed 선언 안 해도 됨
    for i in range(len(t) - window + 1):  # !!
        if int(t[i : i + window]) <= p:
            cnt += 1

    return cnt


t = "3141592"
p = "271"


print(solution(t, p))
