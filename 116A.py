# Трамвай

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    n = int(input().decode().rstrip("\r\n"))
    summa = 0
    capacity = 0
    for _ in range(n):
        a, b = map(int, input().decode().rstrip("\r\n").split())
        summa = summa - a + b
        if summa > capacity:
            capacity = summa
    print(capacity)

main()"""

import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    n = int(input().decode().rstrip("\r\n"))
    summa = capacity = 0
    
    for _ in range(n):        
        summa = summa - eval(input().decode().rstrip("\r\n").replace(' ','-'))
        capacity = max(summa, capacity)
    print(capacity)

main()


"""a=p=0
for x in[0]*int(input()):
    p-=eval(input().replace(' ','-'));a=max(a,p)
print(a)"""