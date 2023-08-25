# G - Возможные друзья

from collections import Counter
 
def main():
    n, m, *a = map(int, open(0).read().split())
    """for s in[*open(0)]:
        n, x = *map(int, s.split()),
        print(n, x)"""
    d = {x: [] for x in range(1, n+1)}
    
    for i in range(0, len(a), 2):
        d[a[i]] = d[a[i]]+[a[i+1]]
        d[a[i+1]] = d[a[i+1]]+[a[i]]
    #print(d)
    for i in range(1, n+1):
        arr = []
        for j in d[i]:
            arr += d[j]
        #print(arr)
        if len(arr) < 2:
            print(0)
        else:
            start_dict = dict(Counter(list(filter(lambda s: s not in d[i]+ [i], arr))))
            #print(start_dict)
            if start_dict == {}:
                print(0)
            else:
                
                arr2 = list({x: y for x, y in filter(lambda x: start_dict[x[0]] == max(start_dict.values()), start_dict.items())}.keys())
                arr2.sort()
                print(*arr2)
        
 
 
main()