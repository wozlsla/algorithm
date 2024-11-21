from dp import fibo, fibo_dp, cal_seat

# Recursive (fibo)
assert fibo(10) == 55
# assert fibo(100) == 354224848179261915075


# DP (fibo)
assert fibo_dp(10) == 55
assert fibo_dp(100) == 354224848179261915075


# 극장 좌석 자리 구하기
assert cal_seat(9, [4, 7]) == 12
assert cal_seat(9, [2, 4, 7]) == 4
assert cal_seat(11, [2, 5]) == 26
assert cal_seat(10, [2, 6, 9]) == 6
