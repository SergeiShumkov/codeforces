# Удалить наименьшее


def main():
    
    
    for s in [*open(0)][2::2]:
        a={*map(int,s.split())}
        if len(a)> max(a)-min(a):
            print("YES")
        else:
            print("NO")

main()


"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    
    
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        n = int(input().decode().rstrip("\r\n"))
        a = sorted(list(set(map(int, input().decode().rstrip("\r\n").split()))))
        
        if len(a) == 1:
            print("YES")
            continue
        r = True
        for i in range(len(a)-1):
            if a[i+1] == a[i] + 1:
                continue
            else:
                print("NO")
                r = False
                break
        if r == True:
            print("YES")
 
main()"""

"""for s in[*open(0)][2::2]:
    a={*map(int,s.split())}
print('YNEOS'[len(a)<=max(a)-min(a)::2])"""