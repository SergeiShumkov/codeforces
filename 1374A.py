# Необходимый остаток

def main():
    
    
    for s in [*open(0)][1:]:
        a=[*map(int,s.split())]
        #print(a[2] % a[0])
        if a[2] % a[0] == a[1]:
            print(a[2])
        if a[2] % a[0] < a[1]:
            print(a[2] - (a[2] % a[0] + a[0] -a[1]))
        if a[2] % a[0] > a[1]:
            print(a[2] - (a[2] % a[0] -a[1]))
    
    

main()


"""for s in[*open(0)][1:]:
    x,y,n=map(int,s.split())
    print(n-(n-y)%x)"""