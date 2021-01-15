# input() 대신 sys 라이브러리 사용
import sys
# readlint() : enter 줄바꿈 기호 자동 사용 , rstrip()으로 제거
input_data = sys.stdin.readline().rstrip()

print(input_data)