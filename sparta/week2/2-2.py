def sol(s):

    table = {}  # 문자열의 가장 최근 위치 기록
    window = start = 0

    for idx, item in enumerate(s):

        # 중복된 문자가 현재 윈도우 내에 있는지를 확인
        if item in table and table[item] >= start:
            # 시작점 업데이트 (중복된 문자 다음 위치)
            start = table[item] + 1

        # 문자 위치 업데이트
        table[item] = idx

        # 부분 문자열의 (최대) 길이 업데이트
        window = max(window, idx - start + 1)
        # window = idx - start + 1

    return window


s = "abcdefabcbbabcabcbb"
print(sol(s))


# hash = {}
# s = "abcabcbbabcabcbb"
# for idx, i in enumerate(s):
#     hash[i] = idx
#     print(hash)
