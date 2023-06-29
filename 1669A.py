# Дивизон?

def main():
    for s in[*open(0)][1:]:
        a = int(s)
        if a <= 1399:
            print("Division 4")
        elif 1400 <= a <= 1599:
            print("Division 3")
        elif 1600 <= a <= 1899:
            print("Division 2")
        else:
            print("Division 1")  
   

main()

"""for n in[*open(0)][1:]:
    r=int(n)/100
    print('Division',1+(r<19)+(r<16)+(r<14))"""