# Предсказание Панорамикса

def simple():
    a = [2]
    
    for i in range(3, 51):
        t = True
        for j in a:
            if i % j == 0:
                t = False
                break
        if t:
            a.append(i)
    return(a)



def main():
    b, c = map(int, open(0).read().split())
    
    a = simple()
    
    if b not in a or c not in a:
        print("NO")
    elif a.index(b) == a.index(c) - 1:
        print("YES")
    else:
        print("NO")
    
        
main()