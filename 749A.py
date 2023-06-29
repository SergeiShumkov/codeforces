# Задача Бахгольда

def main():
    a = int(input())
    b = [2] * (a // 2)
    print(a // 2)
    if a % 2  != 0:
        b[-1] = 3
        

    print(*b)
        
main()

"""n=int(input())
print(n//2,"\n","2 "*(n//2-1),2+n%2)"""