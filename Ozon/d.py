# D - Электронная таблица

def main():
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
    
    
main()