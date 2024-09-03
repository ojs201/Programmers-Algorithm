def solution(arr):
    answer = []
    answer.append(arr.pop())

    for i in range(0, (len(arr))):
        if arr[-1] == answer[-1]:
            arr.pop()
        else:
            answer.append(arr.pop())

    answer.reverse()
    return answer
