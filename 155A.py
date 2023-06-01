# I_love_\%username\%

def main():    
    n, *a = map(int, open(0).read().split())
    cnt = 0
    for i in range(1, len(a)):
        if a[i] > max(a[:i]) or a[i] < min(a[:i]):
        
            cnt += 1
    print(cnt)    

main()


n,*a=map(int,open(0).read().split())
b=a[:1]
for x in a:
	n-=min(b)<=x<=max(b)
	b+=x,
print(n)