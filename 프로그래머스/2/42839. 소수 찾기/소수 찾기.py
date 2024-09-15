from itertools import permutations

def is_prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False
    return True

def solution(numbers):
    possible_numbers = set() 
    
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int(''.join(p)) 
            possible_numbers.add(num)
    
    prime_count = 0
    for num in possible_numbers:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
