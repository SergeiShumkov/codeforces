# Магниты

def main():    
    n,*a=map(int, open(0).read().split())
    count = 1
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            count += 1
    print(count)
    
main()

"""p=f=-1
for s in open(0):
    f+=p!=s
    p=s
print(f)"""