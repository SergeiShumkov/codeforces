# E - Отчет

"""from collections import Counter
 
def main():
    for s in[*open(0)][2::2]:
        arr = list(map(int, s.split()))
        d = dict(Counter(arr))
        t = "YES"
        for (k, v) in d.items():
            if len(set(arr[arr.index(k): arr.index(k)+v])) > 1:
                t = "NO"
                break
        print(t)
        
main()"""

"""import os, io
from collections import Counter

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        input().decode().rstrip("\r\n")
        arr = list(map(int, input().decode().rstrip("\r\n").split()))
        d = dict(Counter(arr))
        t = "YES"
        for (k, v) in d.items():
            if len(set(arr[arr.index(k): arr.index(k)+v])) > 1:
                t = "NO"
                break
        print(t)

main()"""

"""def main():
    for s in[*open(0)][2::2]:
        s = s.replace(" ", "").strip()
        t = "YES"
        for i in set(s):
            if len(set(s[s.find(i): s.rfind(i)+1])) > 1:
                t = "NO"
                break
        
        print(t)    
        
main()"""

"""def main():
    for s in[*open(0)][2::2]:
        s = s.split()
        ss = list(reversed(s))
        t = "YES"
        for i in set(s):
            if len(set(s[s.index(i): len(s) - ss.index(i)])) > 1:
                t = "NO"
                break        
        print(t)
        
main()"""


import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        input().decode().rstrip("\r\n")
        s = input().decode().rstrip("\r\n").split()
        ss = s[::-1]
        ls = len(s)
        t = "YES"
        for i in set(s):
            if  ls - ss.index(i) - s.index(i) > s.count(i):
                t = "NO"
                break        
        print(t)
        
main()


"""def main():
    for s in[*open(0)][2::2]:
        s = s.split()
        ss = s[::-1]
        ls = len(s)
        t = "YES"
        for i in set(s):
            if  ls - ss.index(i) - s.index(i) > s.count(i):
                t = "NO"
                break        
        print(t)
        
main()"""

"""def main():
    for s in[*open(0)][2::2]:
        s = s.split()
        ss = s[::-1]
        ls = len(s)
        t = "YES"
        for i in set(s):
            if len(s[s.index(i): ls - ss.index(i)]) > s.count(i):
                t = "NO"
                break        
        print(t)
        
main()"""


"""def main():
    for s in[*open(0)][2::2]:
        s = s.split()
        t = "YES"
        for i in set(s):
            if len(set(s[s.index(i): s.reverse().index(i)])) > 1:
                t = "NO"
                break
        
        print(t)    
        
main()"""