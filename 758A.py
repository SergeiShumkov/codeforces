# Праздник равенства

def main():
    n, *a = map(int, open(0).read().split())
    m = max(a)
    print(sum([m-x for x in a]))

main()

"""n=int(input())
*l,=map(int,input().split())
print(n*max(l)-sum(l))"""