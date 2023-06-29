# Минимальный квадрат

def main():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        mi = min(a,b)*2
        ma = max(a,b)
        if mi >= ma:
            print(mi**2)
        else:
            print(ma**2)

main()


"""def main():
    
    for s in[*open(0)][1:]:
        a = *map(int, s.split()),
        print(max(*a,2*min(a))**2)        

main()"""



