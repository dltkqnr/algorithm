# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):

    answer = len(s)
    print(s, '압축')
    # 1개 step부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        print(step, '단계 : ', prev)

        # step의 크기 만큼 증가시키며 이전 문자열과 비교
        for j in range(step,len(s), step):
            print(prev, '/', s[j:j+step] ,  '같은지 확인')

            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왓다면 ( 더 이상 압축 x )
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1

        print('압축 전:' , compressed)
        # 남아 있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        print('압축 후:', compressed)
        # 압축 문자열 중 가장 짧은 것
        answer = min(answer, len(compressed))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
