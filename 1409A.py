# Ещё одна задача о двух числах

def main():        
    
    for s in [*open(0)][1:]:        
        a=[*map(int,s.split())]
        b = abs(a[0] - a[1])
        if b % 10:
            print(b//10 + 1)
        else:
            print(b//10)
        
main()

"""for s in[*open(0)][1:]:
    print(0-abs(eval(s.replace(' ','-')))//-10)"""