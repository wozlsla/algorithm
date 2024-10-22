from collections import deque

word = "python"
word = "radar"
word = "eye"

""" deque
맨 앞과 맨 뒤에서 원소를 O(1)의 상수시간으로 꺼내는 자료형
"""


# O(n)
def is_palindrome(word):
    word = deque(word)
    for _ in range(len(word) // 2):
        if word.popleft() != word.pop():
            return False
    return True


print(is_palindrome(word))


# pop 하면 어차피 길이 줄어든다..
def is_palindrome(word):
    word = deque(word)
    if word.popleft() != word.pop():
        return False
    return True


""" list
list에서 pop(0)을 할 경우 맨 앞의 요소를 꺼내고 뒤의 요소들을 모두 한칸씩 앞으로 옯겨주어야 하므로 n만큼의 시간복잡도를 가짐.
"""


# O(n^2)
def is_palindrome(word):
    word = list(word)
    while len(word) > 1:  # O(n)
        if word.pop(0) != word.pop():  # O(n)
            return False
    return True


""" slicing **
내부적으로 C로 구현되어있기 때문에 덱으로 구현한 것 보다 2배 정도 빠르다 ...
"""


def is_palindrome(word):
    return word != word[::-1]
