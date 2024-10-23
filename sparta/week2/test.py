from structures import LinkedList
from palindrome import is_palindrome


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)


assert is_palindrome(l1)
assert not is_palindrome(l2)
