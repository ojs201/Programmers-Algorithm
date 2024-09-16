from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for perm in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for min_fatigue, use_fatigue in perm:
            if current_fatigue >= min_fatigue:
                current_fatigue -= use_fatigue
                count += 1
            else:
                break
        
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons
