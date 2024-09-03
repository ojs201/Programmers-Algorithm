def solution(participant, completion):
    participant_count = {}
    
    for name in participant:
        if name in participant_count:
            participant_count[name] += 1
        else:
            participant_count[name] = 1
    
    # 완주자 수를 줄이기
    for name in completion:
        participant_count[name] -= 1
    
    # 완주하지 못한 선수 찾기
    for name in participant_count:
        if participant_count[name] > 0:
            return name