def solution(sizes):
    width = 0
    height = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        
    for i in range(len(sizes)):
        if sizes[i][0] > width:
            width = sizes[i][0]
        
    for i in range(len(sizes)):
        if sizes[i][1] > height:
            height = sizes[i][1]
            
    answer = width * height
    
    return answer