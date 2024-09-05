def solution(s):
    s_list = list(s)
    cnt = 0

    for i in range(len(s_list)):
        if s_list[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
                break

    if cnt == 0:
        return True
    else:
        return False