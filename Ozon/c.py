# C - Парное программирование

def fed(first, d):
    second = d[0]
    delta = abs(d[0][0]-first[0])
    for i in d:
        if i[0] == first[0]:
            return i
        elif abs(i[0]-first[0]) < delta:
            delta = abs(i[0]-first[0])
            second = i
    return second
 
def main():
    for s in[*open(0)][2::2]:
        d = []
        for count, value in enumerate(list(map(int, s.split())), start=1):
            d.append([value, count])
        for i in range(len(d)//2):
            first = d.pop(0)
            
            second = fed(first, d)
            d.remove(second)
            print(first[1], second[1])
        print()
 
main()