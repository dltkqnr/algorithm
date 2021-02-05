def is_prime_number(x):
    for i in range(2,x):
        if x % i == 0 :
            return False
    return True

x = int(input())

if is_prime_number(x) == True:
    print('prime')
else:
    print('not prime')