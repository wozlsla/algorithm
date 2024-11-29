# https://www.acmicpc.net/problem/1755 - 숫자놀이

alphabet = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

N, M = map(int, input().split())
nums = []

for i in range(N, M + 1):
    num = str(i)
    s = ""
    for n in num:
        s += alphabet[n] + " "
    nums.append(s)

nums.sort()

reverse_alphabet = {v: k for k, v in alphabet.items()}
res = []
for num in nums:
    j = ""
    for n in num.split():
        j += reverse_alphabet[n].strip()
    res.append(j)

res = [int(i) for i in res]

for i in range(0, len(res), 10):
    print(*res[i : i + 10])


#  다른 사람 풀이 (list)
d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
alphabet = {}

for i in range(N, M + 1):
    if i > 9:
        alphabet[i] = d[int(str(i)[0])] + d[int(str(i)[1])]
    else:
        alphabet[i] = d[i]

result = [i[0] for i in sorted(alphabet.items(), key=lambda x: x[1])]

while True:
    if len(result) > 10:
        print(*result[:10])
        result = result[10:]
    if len(result) <= 10:
        print(*result)
        break


# 2
res = []
for i in range(N, M + 1):
    a = " ".join([alphabet[j] for j in str(i)])
    res.append([i, a])
print(res)

res.sort(key=lambda x: x[1])

for i in range(len(res)):
    if i % 10 == 0 and i != 0:
        print()
    print(res[i][0], end=" ")
