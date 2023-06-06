# Черный квадрат

def main():
    
    
    b = [0] + list(map(int, input().split()))
    sum = 0
    for i in input():
        sum += b[int(i)]
    
    print(sum)

main()


"""def main():
    
    a = [*open(0)]
    b = [0] + list(map(int, a[0].split()))
    sum = 0
    for i in a[1]:
        sum += b[int(i)]
    
    print(sum)

main()


def main():
    
    a = [*open(0)]
    b = [0] + list(map(int, a[0].split()))
    d = [int(c) for c in a[1]]
    sum = 0
    for i in d:
        sum += b[i]
    print(sum)

main()

def main():
    
    a = [*open(0)]
    b = [0] + list(map(int, a[0].split()))
    d = [int(c) for c in a[1]]
    sum = 0
    for i in range(1, 5):
        sum += b[i] * d.count(i)
    print(sum)

main()


def main():
    
    
    b = [0] + list(map(int, input().split()))
    d = [int(c) for c in input()]
    sum = 0
    for i in range(1, 5):
        sum += b[i] * d.count(i)
    print(sum)

main()

*a,=map(int,input().split())
print(sum(a[int(i)-1]for i in input()))"""