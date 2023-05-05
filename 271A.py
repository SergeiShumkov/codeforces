# Красивый год

def main():    
    y=open(0).read()
    y = str(int(y) + 1)
    while len(y) != len(set(y)):
        y = str(int(y) + 1)
     
    print(y) 

main()

"""def main():    
    y=open(0).read()
    y = int(y) + 1
    while len(set(str(y)))-4:
        y += 1     
    print(y) 

main()"""

"""n=int(input())+1
while len(set(str(n)))-4:n+=1
print(n)"""