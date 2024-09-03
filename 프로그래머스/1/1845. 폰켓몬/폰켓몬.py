def solution(nums):
    norep = set(nums)
    n = len(nums) // 2
    
    if len(norep) >= n:
        return n
    else:
        return len(norep)