n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    print(input_data)
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))
    print(array)

# 키(key)를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')