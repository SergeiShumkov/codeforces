# Короткие подстроки

def main(): 
    
    input = open(0).read().split()
    for i in input[1:]:
        print(i[0]+i[1:-1:2]+ i[-1])
        
main()


"""for s in[*open(0)][1:]:
    print(s[0]+s[1::2])"""