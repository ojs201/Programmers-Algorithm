def solution(brown, yellow):
    def divisor_pairs(n):
        pairs = []
        for i in range (1, n + 1):
            if n % i == 0 and i >= n // i:
                pair = (i, n //i)
                pairs.append(pair)
        return pairs
    
    square_count = brown + yellow
    divisor_list = []
    w = 0
    h = 0
    
    divisor_list = divisor_pairs(square_count)

    for i in range(len(divisor_list)):
        if (divisor_list[i][0] - 2) * (divisor_list[i][1] - 2) == yellow:
            w = divisor_list[i][0]
            h = divisor_list[i][1]

    answer = [w, h]
    
    return answer