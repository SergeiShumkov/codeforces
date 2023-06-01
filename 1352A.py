# Сумма круглых чисел

def main():    
    
    for i in [*open(0)][1:]:
        a = [c+'0'*i  for i,c in enumerate(i[-2::-1]) if c != '0']
        print(len(a))
        print(*a)

main()

"""def main():    
    for i in[*open(0)][1:]:
        b = []
        for j in range(1, len(i)+1):
            if i[j-1] == '0':
                continue
            else:
                b.append(i[j-1]+'0'*(len(i)-j))
        print(len(b))
        print(*b)

main()"""


"""for s in[*open(0)][1:]:
    a=[c+i*'0'for i,c in enumerate(s[-2::-1])if'0'<c]
print(len(a),*a)"""