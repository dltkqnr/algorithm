# codeup basic1025
"""
a = input()
b = 10000

for i in range(len(a)):
    if b != 0:
        print("[" + str(int(int(a[i]) * b ))+"]")
        b/=10
"""

a = input()
for i in range(5):
    number = int(a[i])
    print("[%d]" % (number*10000/(10**i)))