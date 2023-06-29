# Честный тренер

def main():

    for s in [*open(0)][2::2]:
        a=list(map(int,s.split()),)
        a.sort()
        print(min([a[i+1] - a[i] for i in range(len(a)-1)]))
        
main()

"""def main():

    for s in [*open(0)][2::2]:
        a=sorted(map(int,s.split()))
        print(min([a[i+1] - a[i] for i in range(len(a)-1)]))
        
main()



for s in [*open(0)][2::2]:
    a=sorted(map(int,s.split()))
    print(min([j-i for i, j in zip(a,a[1:])]))"""