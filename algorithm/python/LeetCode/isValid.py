s = "([}}])"

stack = []

if len(s) % 2 == 1:
    print(False)
    exit()

for i in s:
    if i == "(":
        stack.append("(")
    elif i == "[":
        stack.append("[")
    elif i == "{":
        stack.append("{")
    elif i == ")":
        if len(stack) < 1:
            print(False)
            exit()
        if stack[-1] == "(":
            stack.pop()
        else:
            print(False)
            exit()
    elif i == "]":
        if len(stack) < 1:
            print(False)
            exit()
        if stack[-1] == "[":
            stack.pop()
        else:
            print(False)
            exit()
    elif i == "}":
        if len(stack) < 1:
            print(False)
            exit()
        if stack[-1] == "{":
            stack.pop()
        else:
            print(False)
            exit()

if len(stack) == 0:
    print(True)
else:
    print(False)
