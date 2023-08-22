# B - Сумма к оплате

from collections import Counter
 
def main():
    for s in[*open(0)][2::2]:
        cnt = 0
        d = dict(Counter(map(int, s.split())))
        for j in d:
            cnt += j * (d[j]-d[j]//3)
        print(cnt)
 
 
main()