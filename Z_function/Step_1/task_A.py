import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():

    n = int(input().decode().rstrip("\r\n"))
    
     
    for i in range(n):
        st = input().decode().rstrip("\r\n")
        for j in range(len(st), 0, -1):
            temp_st = st[:j]
            if temp_st == temp_st[::-1]:
                print(len(temp_st))
                break
     
main()


"""
import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
    n = int(input().decode().rstrip("\r\n"))
    a = [int(i) for i in input().split()]
    b = [0]*(n+1)
    temp = 0
 
    for i in range(1, len(a)+1):
        temp += a[i-1]
        b[i] = temp
 
    print(*b)
     
main()"""

"""n = int(input())

 
for i in range(n):
    st = input()
    for j in range(len(st), 0, -1):
        temp_st = st[:j]
        if temp_st == temp_st[::-1]:
            print(len(temp_st))
            break"""
        # print("===", st[:j])
 
    # print("======", st)