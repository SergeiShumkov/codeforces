# Куплю лопату

def main():    
    
    
    k, r = map(int, open(0).read().split())
    for i in range(1, 11):
        if str(k * i)[-1] in ['0', str(r)]:
            break
    print(i)

main()