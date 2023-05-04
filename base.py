import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
    
    n = input().decode().rstrip("\r\n")
    s = input().decode().rstrip("\r\n")
    if s.count("A") > s.count("D"):
        print("Anton")
    elif s.count("A") < s.count("D"):
        print("Danik")
    else:
        print("Friendship")
        

main()




"""t = input()
p = input()

print(t, p)

cnt = 0
ar = []
for i in range(len(t) - len(p) + 1):
    s = t[i:i+len(p)]
    j = 0
    for a,b in zip(s, p):
        if a == b or b == "?":
           j += 1
        else:
            break
    if j == len(p):
        ar.append(i)
        cnt +=1
    
print(cnt)
print(*ar)"""

"""5
abacaba
a?a
test
?????
abaabaaab
a??a
ok
?
test
me"""



"""def z(string, idx):
    if not idx : return 0
    i=0
    print(string, string[idx:])
    for a,b in zip(string, string[idx:]):
        if not a == b :
            break
        i+=1
    return i

for i in range(len('abacaba')) :
    print(z('abacaba', i))"""

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
    
    x = input().decode().rstrip("\r\n")
    a = [1 if i.isupper() else 0 for i in x]
    if a.count(1) > a.count(0):
        print(x.upper())
    else:
        print(x.lower())
        

main()"""


"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
 
    n, k = map(int, input().decode().rstrip("\r\n").split())
    
    lst = list(map(int, input().decode().rstrip("\r\n").split()))
    
    a = lst[:k]
    for i in lst[k:]:
        if i == a[-1]:
            a.append(i)
        else:
            break
        
    print(len(a) - a.count(0))

                
main()"""

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():
 
    n = int(input().decode().rstrip("\r\n"))
    
    count = 0
    for _ in range(n):
        st = input().decode().rstrip("\r\n")
        if st.count("1") > 1:
            count += 1

    print(count)    
 

                
main()"""


"""lst = [1 if ((st[i:j] in pre or st[i:j] in suf) and not(st[i:j] in pre and st[i:j] in suf))  else 0 for i in range(len(st)) for j in range(i+1, len(st)+1)  ]
        
        print (lst.count(1))
counter = 0
        
        for i in range(len(st)):
            for j in range(i+1, len(st)+1):
                item = st[i:j]
                
                if item in pre and item in suf:
                    continue
                if item in pre or item in suf:
                    counter += 1
                

        print(counter)"""


"""lst = [1 if (st[i:j] == st[:i] or st[i:j] == st[j:len(st)]) and st[:i] != st[j:len(st)] else 0 for i in range(1, len(st)) for j in range(i+1, len(st))]
        print(lst.count(1))"""
        
        
 # [st[:i], st[i:j],st[j:len(st)]]

"""
a = st[:i]
        b = st[i:j]
        c = st[j:len(st)]

4
abacaba
aaaa
barbarmiakirkudu
abaabaababaab"""


"""
    n = int(input().decode().rstrip("\r\n"))
    
     
    for i in range(n):
        st = input().decode().rstrip("\r\n")
        for j in range(len(st), 0, -1):
            temp_st = st[:j]
            if temp_st == temp_st[::-1]:
                print(len(temp_st))
                break"""