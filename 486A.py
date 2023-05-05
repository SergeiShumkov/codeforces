# Подсчёт функции

"""def main():    
    k = int(open(0).read())
    
    if k % 2 == 0:
        print(k//2)
    else:
        print(k//2 - k)
    
main()"""

def main():    
    k = int(open(0).read())
    
    print(k//2 - k%2*k)
    
main()

# n=int(input());print(n//2-n%2*n)