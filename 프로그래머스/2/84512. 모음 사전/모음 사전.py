def solution(word):
    factors = [781, 156, 31, 6, 1]
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    result = 0
    
    for i, char in enumerate(word):
        index = vowels.index(char) 
        result += index * factors[i] + 1  
    
    return result