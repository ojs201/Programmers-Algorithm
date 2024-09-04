import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]  # 각 작업의 남은 일수를 계산
    answer = []
    
    current_deployment = days[0]  # 첫 번째 배포 기준
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current_deployment:
            count += 1  # 현재 배포 그룹에 포함
        else:
            answer.append(count)  # 현재 배포 그룹의 작업 개수 저장
            current_deployment = days[i]  # 새로운 배포 기준 설정
            count = 1  # 새 배포 그룹 초기화
    
    answer.append(count)  # 마지막 배포 그룹 추가
    
    return answer