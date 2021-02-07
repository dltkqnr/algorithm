# https://programmers.co.kr/learn/courses/30/lessons/42889

    
def solution(n,stages):

    answer = []

    count = [0] * (max(stages)+1)

    for i in range(len(stages)):
        count[stages[i]] += 1

    data = []
    for i in range(1, n+1):
        data.append(count[i]/sum(count[i:]))


solution(5, [2,1,2,6,2,4,3,3])

