# Выбор команд

def main(): 
    
    n, k, *a = map(int, open(0).read().split())
    b = [x for x in a if x<=5-k]
    print(len(b) // 3)


main()


"""i=lambda:map(int,input().split())
n,k=i()
print(sum(x<=5-k for x in i())//3)"""