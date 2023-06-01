# Сережа и Дима

def main():
    n, *a = map(int, open(0).read().split())
    sum_and = 0
    sum_dmi = 0
        
    for i in range(n):
        if a[0] > a[-1]:
            q = a[0]
        else: 
            q = a[-1]
        if i % 2:
            sum_dmi += a.pop(a.index(q))
        else:
            sum_and += a.pop(a.index(q))        
    print(sum_and, sum_dmi)
main()



"""i,x=input,[0,0]
n,m=int(i()),[*map(int,i().split())]
for i in range(n):
    b=max(m[0],m[-1])
    x[i%2]+=b
    m.remove(b)
print(*x)"""