def is_valid_parathesis(s):
    mapping = {}
    stack = []

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack or mapping[ch] != stack.pop():
                return False
    
    return not stack

if __name__ == "__main__":
    print(is_valid_parathesis("()[]{}"))
    print(is_valid_parathesis("([)]"))
    print(is_valid_parathesis("()"))
    print(is_valid_parathesis("()[]{}"))
    print(is_valid_parathesis("([{}])"))

    #output
    #True
    #False
    #True
    #True
    #True
