# Два массива и обмены

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        a = sorted(list(map(int, input().split())))
        b = sorted(list(map(int, input().split())), reverse=True)
        ab = list(zip(a,b))
        
        
        for d in range(k):
            
            if ab[d][0] >= ab[d][1]:
                break
            else:
                a[d] = ab[d][1]
        print(sum(a))

main()





"""R=lambda:map(int,input().split())
t,=R()
for _ in[0]*t:
    n,k=R()
print(sum(map(max,sorted(R()),sorted(R())[:-1-k:-1]+[0]*n)))"""