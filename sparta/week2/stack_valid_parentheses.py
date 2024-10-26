""" Python List """


def test_problem_stack(s):
    stack = []  # python에서는 그냥 list로도 쓴다..
    pair = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        if char in "({[":
            # stack.push(char)
            stack.append(char)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()
            if pair[char] != top:
                return False

    # return stack.is_empty()
    return not stack


""" Stack """


def parentheses_stack(s):
    stack = Stack()
    pair = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        if char in "({[":
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return stack.is_empty()


from structures import Stack

assert parentheses_stack("()")
assert parentheses_stack("()[]{}")
assert parentheses_stack("({[][]})")
assert parentheses_stack("({[]})")
assert not parentheses_stack("(]")
assert not parentheses_stack("(()]")
assert not parentheses_stack("(((])")
assert not parentheses_stack("((())")
assert not parentheses_stack("((())))")
