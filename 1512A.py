# Шпион обнаружен!

def main():
    for s in[*open(0)][2::2]:
        t = s.split()
        for i  in set(t):
            if t.count(i) == 1:
                print(t.index(i)+1)
                break

main()

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():

    t = int(input().decode().rstrip("\r\n"))
     
    for i in range(t):
        n = input().decode().rstrip("\r\n")
        t = list(map(int, input().decode().rstrip("\r\n").split()))
        for i  in set(t):
            if t.count(i) == 1:
                print(t.index(i)+1)
                break
main()"""



"""for s in[*open(0)][2::2]:
    a=s.split()
    print(a.index(min(a,key=a.count))+1)"""