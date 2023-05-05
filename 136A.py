# Подарки

"""def main():    
    n,*a=map(int, open(0).read().split())
    arr = [0]*n
    for i in range(n):
        x = a[i] - 1
        arr[x] = i + 1
    print(*arr)
main()"""

def main():    
    input = open(0).read().split()    
    print(*[input[1:].index(str(i+1))+1 for i in range(int(input[0]))])
    
main()

"""n=int(input())
s=input().split()
print(*[s.index(str(i+1))+1 for i in range(n)])"""