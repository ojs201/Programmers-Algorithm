def solution(name):
    def get_char_move(c):
        return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    total_moves = 0
    n = len(name)
    
    for char in name:
        total_moves += get_char_move(char)
    
    min_move = n - 1 
    
    for i in range(n):
        next_idx = i + 1
        
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        min_move = min(min_move, 2 * i + n - next_idx, i + 2 * (n - next_idx))
    
    total_moves += min_move
    return total_moves