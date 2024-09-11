def solution(answers):
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == supo_1[i % len(supo_1)]:
            scores[0] += 1
        if answers[i] == supo_2[i % len(supo_2)]:
            scores[1] += 1
        if answers[i] == supo_3[i % len(supo_3)]:
            scores[2] += 1

    max_score = max(scores)
    result = [i + 1 for i in range(3) if scores[i] == max_score]

    return result
