import os, io, time

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        
        n = int(input().decode().rstrip("\r\n"))
        
        temp = [0]*n        
        ss = True
        for j in range(n):
            try:
                a = list(map(lambda x: int(time.mktime(time.strptime('10/10/2020 '+x, '%d/%m/%Y %H:%M:%S'))), input().decode().rstrip("\r\n").split("-")))
                if a[1] >= a[0]:
                    temp[j] = a
                else:
                    ss = False
                    
            except:
                ss = False
                
        # print(temp)
        if ss:
            for i in range(len(temp)):
                for j in range(len(temp)):
                    if i != j:
                        if not len(list(range(max(temp[i][0],temp[j][0]), min(temp[i][1],temp[j][1])+1, 1))):
                            continue
                        else:
                            ss = False
                            
                            break

        
        print(["NO", "YES"][ss])
        
main()




# import time
# a = []
# srrr = "23:59:58-23:59:59 00:00:00-23:59:58".split()
# for i in srrr:
#     # d = i.split("-")
#     # s.append(d)

#     s = list(map(lambda x: int(time.mktime(time.strptime('10/10/2020 '+x, '%d/%m/%Y %H:%M:%S'))), i.split("-")))
#     a.append(s)

# #print(a)
# # a = [[1602363499, 1602363699],[1602277200, 1602363598]]
# b = [1602277200, 1602363598]

# print(list(range(max(a[0][0],a[1][0]), min(a[0][1],a[1][1])+1, 1)))
# # print(list(range (9, 8, 1)))




"""
import os, io, time

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    t = int(input().decode().rstrip("\r\n"))
    for i in range(t):
        n = int(input().decode().rstrip("\r\n"))
        
        temp = [0]*n
        
        ss = "YES"
        for j in range(n):
            try:
                a = list(map(lambda x: time.mktime(time.strptime('10/10/2020 '+x, '%d/%m/%Y %H:%M:%S')), input().decode().rstrip("\r\n").split("-")))
                if a[1] >= a[0]:
                    temp[j] = a
                else:
                    ss = "NO"
            except:
                ss = "NO"
        
        if ss == "YES":
            temp = sorted(temp, key=lambda i: (i[1]))
            c = 0
            for j in temp:
                if j[0] > c:
                    c = j[1]
                else:
                    ss = "NO"
        print(ss)
        
main()"""

# struct_time = time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=2, tm_min=46, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
# print(time.mktime(struct_time))

# struct_time = time.strptime('10/10/2020 10:15', '%d/%m/%Y %H:%M')
# print()