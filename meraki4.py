import json
x={'4': 5, '6': 7, '1': 3, '2': 4}
z=[]
b=[]
for i,j in x.items():
    z.append(i)
    b.append(j)
z.sort()
dic={}
for p in z:
    for q in b:
        dic[p]=q
        b.remove(q)
        break
m=dic


f=open("file1.json","w")
file=json.dump(m,f,indent=2)
f.close()