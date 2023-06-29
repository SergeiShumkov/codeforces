# Поликарп и монеты

def main():

    m, *a = map(int, open(0).read().split())
    for i in a:
        c = d = i//3
        if i % 3 == 1:
            c += 1
        if i % 3 == 2:
            d += 1
        print(c, d)

main()

"""for s in[*open(0)][1:]:
    n=int(s)
    print(c:=n//3+n%3%2, n-c>>1)"""