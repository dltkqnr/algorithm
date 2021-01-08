# codeup basic1085
h,b,c,s = map(int, input().split())

bt = (h*b*c*s)/8
kb = bt/1024
print("%.1f MB" %(kb/1024))