# Полицейские-рекруты


def main():    
    input = open(0).read().split() 
    cnt1 = 0
    cnt2 = 0
    for i in input[1:]:
        if i == '-1' and cnt2 == 0:
            cnt1 += 1
            continue
        elif i == '-1' and cnt2 != 0:
            cnt2 -= 1
        else:
            cnt2 += int(i)
    print(cnt1)
    
main()

"""
input()
k=0
for i in list(map(int,input().split()[::-1])):
  print(i, "=====")
  k=min(0,k+i)
  print(k)
print(-k)
"""