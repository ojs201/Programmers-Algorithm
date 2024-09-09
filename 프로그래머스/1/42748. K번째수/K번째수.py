def solution(array, commands):
    result = []
    
    for command in commands:
        i, j, k = command
        sliced_array = sorted(array[i-1:j])
        result.append(sliced_array[k-1])
    
    return result
