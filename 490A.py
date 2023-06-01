# Командная олимпиада

def main():
    n, *a = map(int, open(0).read().split())
    s = min(a.count(1), a.count(2), a.count(3))
    print(s)
    d = {1:[], 2:[], 3:[]}
    for k, v in enumerate(a):
        d[v].append(k+1)
    for i in range(s):
        print(d[1][i], d[2][i], d[3][i])

main()

"""input()
n=[[],[],[]]
for i,j in enumerate(input().split(),1):
    n[int(j)-1]+=[i]
print(min(map(len,n)))
for j in zip(*n):
    print(*j)"""
