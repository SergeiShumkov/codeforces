# Газировкопитие

def main():    
    n, k, l, c, d, p, nl, np = map(int, open(0).read().split())
    print((min(k*l//nl, c*d, p//np))//n)
    
main()