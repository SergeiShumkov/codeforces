# Счастливый?

def main():
    
    
    for s in[*open(0)][1:]:
        a = [int(c) for c in s.rstrip()]
        print(["NO", "YES"][sum(a[:3]) == sum(a[3:])])

main()

"""for s in[*open(0)][1:]:
    a,b,c,d,e,f,_=map(ord,s)
    print('YNEOS'[a+b+c!=d+e+f::2])"""