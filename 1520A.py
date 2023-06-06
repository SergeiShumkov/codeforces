# Не отвлекайся!

def main():
    
    
    for s in[*open(0)][2::2]:
        s = s.rstrip()
        if len(s) == 1:
            dd = True
        set1 = {s[0]}
        dd = True
        for i in range(1, len(s)):
            if s[i-1] != s[i] and s[i] not in set1:
                 set1.add(s[i])
                 
            elif s[i-1] != s[i] and s[i] in set1:
                dd = False
                break
        print(["NO", "YES"][dd])

main()

"""from itertools import* 
for s in[*open(0)][2::2]:
    print('YNEOS'[len([*groupby(s)])>len({*s})::2])

from itertools import* 

s = "DDBBCCCBBEZ"
print([*groupby(s)])
print({*s})"""