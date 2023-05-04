# Очередь в школе

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    n, t = map(int, input().decode().rstrip("\r\n").split())
    s = input().decode().rstrip("\r\n")
    for _ in range(t):
        start = -1
        l = len(s) - 1
        index_arr = []
        while True:
            start = s.find("B", start+1)
            if start not in [-1, l]:
                index_arr.append(start)
            if start == -1:
                break
        if len(index_arr) == 0:
            break
        
        for i in index_arr:            
            li = list(s)        
            if li[i+1] == 'G':
                li[i] = 'G'
                li[i+1] = 'B'
            s = ''.join(li)
            
    print(s)
 
main()"""

import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    t = int(input().decode().rstrip("\r\n")[2:])
    s = input().decode().rstrip("\r\n")
    while t:
        s=s.replace('BG','GB')
        t -=1
            
    print(s)

main()

"""t=int(input()[2:]);s=input()
while t:
    s=s.replace('BG','GB')
    t-=1
print(s)"""



"""def main():
    n = 4
    s = "BGBBG"

    for _ in range(n):
        start = -1
        l = len(s) - 1
        index_arr = []
        while True:
            start = s.find("B", start+1)
            if start not in [-1, l]:
                index_arr.append(start)
            if start == -1:
                break
        if len(index_arr) == 0:
            print(s)
            break
        print(index_arr)
        for i in index_arr:
            print(s)
            li = list(s)        
            if li[i+1] == 'G':
                li[i] = 'G'
                li[i+1] = 'B'
            s = ''.join(li)
            
    print(s)


main()"""