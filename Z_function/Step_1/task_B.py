"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
 
    n = int(input().decode().rstrip("\r\n"))
    
     
    for i in range(n):
        st = input().decode().rstrip("\r\n")    
        lst = [1 if (st[i:j] == st[:i] or st[i:j] == st[j:len(st)]) and st[:i] != st[j:len(st)] else 0 for i in range(1, len(st)) for j in range(i+1, len(st))]
        print(lst.count(1))

                
main()"""


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

st = "222222"

lst = [1 if (st[i:j] == st[:i] or st[i:j] == st[j:len(st)]) and st[:i] != st[j:len(st)] else 0 for i in range(1, len(st)) for j in range(i+1, len(st))]
print(lst.count(1))
# lst = [[st[:i], st[i:j], st[j:len(st)]] for i in range(1, len(st)) for j in range(i+1, len(st))]

print(lst)

# lst = [f'{st[:i]} {st[i:j]} {st[j:len(st)]}' for i in range(1, len(st)) for j in range(i+1, len(st))]

# lst = [j if st[i:j] == st[:i] or st[i:j] == st[j:len(st)] else None for i in range(1, len(st)) for j in range(i+1, len(st))]
# print('\n'.join(lst))
for i in range(1, len(st)):
    for j in range (i+1, len(st)):
        a = st[:i]
        b = st[i:j]
        c = st[j:len(st)]
        
        print(a, " --- ", b, " --- ", c)