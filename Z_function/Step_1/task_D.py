def main():
    n, *a = open(0).read().split()
    
    for i in range(0, len(a), 2):
        s = a[i]
        t = a[i+1]
        
        print(len(s) - len(t) + 1)
        cnt = 0
        for i in range(len(s) - len(t) + 1):
            p = s[i:i+len(t)]
            print(p)
            """j = 0
            for a,b in zip(s, p):
                if a == b or b == "?":
                    j += 1
                else:
                    break
            if j == len(p):
                ar.append(i)
                cnt +=1"""          
    
main()



