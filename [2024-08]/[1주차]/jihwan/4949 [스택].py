while True:
    s = input() # 개행문자로 끝나는 것이 아닌 '.' 으로 구분하기 때문에 input 으로 받아야 함
    if s == '.':
        break
    stack = []
    balance = True

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                balance = False
                break
            last = stack.pop(-1)
            if last != '(':
                balance = False
                break
        if i == ']':
            if len(stack) == 0:
                balance = False
                break
            last = stack.pop(-1)
            if last != '[':
                balance = False
                break

    if len(stack) != 0:
        balance = False

    if balance:
        print("yes")
    else:
        print("no")