from structures import LinkedList, Stack, Queue, HashTable
from linked_list_palindrome import is_palindrome
from stack_valid_parentheses import test_problem_stack
from queue_order import test_problem_queue


""" Linked List """


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

assert is_palindrome(l1)
assert not is_palindrome(l2)


""" Stack """


def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()


test_stack()

assert test_problem_stack("()")
assert test_problem_stack("()[]{}")
assert test_problem_stack("({[][]})")
assert test_problem_stack("({[]})")
assert not test_problem_stack("(]")
assert not test_problem_stack("(()]")
assert not test_problem_stack("(((])")
assert not test_problem_stack("((())")
assert not test_problem_stack("((())))")


""" Queue """


def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()


test_queue()

assert test_problem_queue(2) == 2
assert test_problem_queue(3) == 2
assert test_problem_queue(4) == 4
assert test_problem_queue(5) == 2
assert test_problem_queue(6) == 4
assert test_problem_queue(7) == 6


""" Hash Table (Chaining) """


ht = HashTable()

ht.put(1, 1)
ht.put(2, 2)
assert ht.get(1) == 1
assert ht.get(2) == 2
assert ht.get(3) == -1

ht.put(12, 1)
ht.put(22, 2)
ht.put(32, 3)
assert ht.get(12) == 1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.remove(12)
assert ht.get(2) == 2
assert ht.get(12) == -1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.get(2)
