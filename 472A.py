# Уроки дизайна задач: учимся у математики

from math import sqrt
 
 
def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return True
        i += 1
    if n > 1:
        return False


def main(): 
    
    a = int(open(0).read())
    b = a // 2

    while b >= 4:    
        if is_prime(b) and is_prime(a - b):
            print(b, a -b)
            break
        b -= 1

main()

"""_=int(input())
print(Z:=8+_%2,_-Z)"""