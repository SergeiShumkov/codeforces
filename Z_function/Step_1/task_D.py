import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():

    n = int(input().decode().rstrip("\r\n"))
     
    for i in range(n):
        s = input().decode().rstrip("\r\n")
        t = input().decode().rstrip("\r\n")

        cnt = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                # print(i, j)
                # print(s[i:j])
                if t not in s[i:j]:
                    cnt += 1
        print(cnt)        
main()


"""def main():    
    n, *a = open(0).read().split()
    
    for i in range(0, len(a), 2):
        s = a[i]
        t = a[i+1]
        
        
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                # print(i, j)
                # print(s[i:j])
                if t not in s[i:j]:
                    cnt += 1
        print(cnt)        
main()"""



