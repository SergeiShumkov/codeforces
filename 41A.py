# Перевод

"""import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    s = input().decode().rstrip("\r\n")
    t = input().decode().rstrip("\r\n")
    if s == t[::-1]:
        print("YES")
    else:
        print("NO")

main()"""

import os, io
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def main():    
    s = input().decode().rstrip("\r\n")
    t = input().decode().rstrip("\r\n")    
    print('YNEOS'[s!=t[::-1]::2])

main()

"""print('YNEOS'[input()!=input()[::-1]::2])"""