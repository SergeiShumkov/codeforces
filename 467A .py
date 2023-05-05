# Юра и заселение

"""def main():    
    n,*a=map(int, open(0).read().split())
    count = 0
    for i in range(len(a))[::2]:
        if a[i+1] - a[i] >= 2:
            count += 1
            
    print(count)
           
main()"""

import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():    
    n = int(input().decode().rstrip("\r\n"))
    c = 0
    for i in range(n):
        if eval(input().decode().rstrip("\r\n").replace(' ','-')) < -1:
            c += 1
    print(c)
           
main()


# print(sum(eval(input().replace(' ','-'))<-1for _ in ' '*int(input())))