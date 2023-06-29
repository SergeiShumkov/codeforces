# Честное разделение

def main():

    for s in [*open(0)][2::2]:
        # print(s.count("1"),s.count("2"))
        if s.count("1") == 0 and s.count("2") % 2 == 0:
            print("YES")
        elif s.count("1") % 2 == 0 and s.count("1") != 0:
            print("YES")
        
        else:
            print("NO")

main()

"""def main():

    for s in [*open(0)][2::2]:        
        if s.count("1") % 2 or s.count("1")<len(s)%4:
            print("NO")        
        else:
            print("YES")

main()



for s in[*open(0)][2::2]:
    a=s.count('1')
    print('YNEOS'[a%2 or a<len(s)%4::2])"""