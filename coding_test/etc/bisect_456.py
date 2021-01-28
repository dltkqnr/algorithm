from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value , right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

b = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(b,4,4))
print(count_by_range(b,-1,3))