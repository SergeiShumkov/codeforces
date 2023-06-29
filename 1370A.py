# Максимальный НОД

def main():

    m, *a = map(int, open(0).read().split())
    for i in a:
        print(i//2)

main()

"""for s in[*open(0)][1:]:
    print(int(s)//2)"""


"""def main():

    a, b = *map(int, [*open(0)][0].split()),
    c = max(a, b)
    d = min(a,b)

    while c % d != 0:
        c, d = d, c%d
    print(d)

main()"""