# Ваня и забор

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    n, h = map(int, input().decode().rstrip("\r\n").split())
    
    a = list(map(int, input().decode().rstrip("\r\n").split()))
    s = [1 if x <= h else 2 for x in a] 
    print(sum(s))
 
main()"""


 
def main():    
    N,h,*a=map(int, open(0).read().split())
    print(N+sum([n>h for n in a])) 

main()

"""N,h,*a=map(int, open(0).read().split())
print(N+sum(n>h for n in a))"""