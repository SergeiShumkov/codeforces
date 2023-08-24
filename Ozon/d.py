# D - Электронная таблица

"""def main():
    t = int(input())
    for i in range(t):
        input()
        
        n, m = *map(int, input().split()),
        
        b = [[int(j) for j in input().split()] for i in range(n)]
        k = int(input())
        c = list(map(int, input().split()))
        
        for click in c:
            b = sorted(b, key=lambda i: (i[click - 1]))
        for z in b:
            print(*z)
        print()
    
    
main()"""
import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        input().decode().rstrip("\r\n")
        
        n, m = *map(int, input().split()),
        
        b = [[int(j) for j in input().decode().rstrip("\r\n").split()] for i in range(n)]
        k = int(input())
        c = list(map(int, input().decode().rstrip("\r\n").split()))
        
        for click in c:
            b = sorted(b, key=lambda i: (i[click - 1]))
        for z in b:
            print(*z)
        print()
    
    
main()




