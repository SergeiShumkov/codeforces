# Бросок кубика

def main():
    a = max(*map(int, [*open(0)][0].split()),)
     
    if a == 1:
        print("1/1")
    elif a == 2:
        print("5/6")
    elif a == 3:
        print("2/3")
    elif a == 4:
        print("1/2")
    elif a == 5:
        print("1/3")
    else:
        print("1/6")

main()

# print(['1/1','5/6','2/3','1/2','1/3','1/6'][int(max(input().split()))-1])