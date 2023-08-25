# H. Валидация карты

import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    
    
    for _ in range(int(input().decode().rstrip("\r\n"))):
        n, m = *map(int, input().split()),
        for i in range(n):
            print(input().decode().rstrip("\r\n").split("."))
            
# R, G, V, Y , B            
main()