def solution(code):
    mode = 0
    lst = []
    for i in range(len(code)):
        if mode == 0:
            if code[i] != "1":
                if i % 2 == 0:
                    lst.append(code[i])
            elif code[i] == "1":
                mode += 1
        elif mode == 1:
            if code[i] != "1":
                if i % 2 == 1:
                    lst.append(code[i])
            elif code[i] == "1":
                mode -= 1

    if len(lst) == 0:
        return "EMPTY"
    return "".join(lst)