# Проверка Codeforces

def main():

    for s in[*open(0)][1:]:
        
        if s[:-1] in "codeforces":
            print("YES")
        else:
            print("NO")
main()



"""for c,_ in[*open(0)][1:]:
    print('NYOE S'[c in'cdfores'::2])"""