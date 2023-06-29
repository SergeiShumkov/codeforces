# Квадратная строка?

def main():
    for s in[*open(0)][1:]:
        a = len(s[:-1])
        if a % 2 == 0 and s[:a//2] == s[a//2:-1]:
            print("YES")
        else:
            print("NO")
        
main()


"""for s in[*open(0)][1:]:
    n=len(s)//2
    print('YNEOS'[s[:n]!=s[n:-1]::2])"""