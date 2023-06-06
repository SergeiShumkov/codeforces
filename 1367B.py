# Четный массив


def main():
    
    
    for s in[*open(0)][2::2]:
        a =list(map(int, s.split()))
        even, odd = 0, 0
        for i in range(len(a)):
    
            if a[i] % 2 == i % 2:
                continue
            else:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        if even == odd:
            print(even)
        else:
            print(-1)
    
 
main()


"""for s in [*open(0)][2::2]:
    a=[int(x)%2 for x in s.split()]
    print((sum(i%2^x for i,x in enumerate(a))//2,-1)[sum(a)!=len(a)//2])"""