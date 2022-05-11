import json
f=open("file4.json","r")
y=f.read()
h=json.loads(y)
for i in h:
    x=input("enter..")
    y=int(input("enter.."))
    for p,q in h[i].items():
        if x==p:
            h[i][p]=str(int(q)-y )
with open("file4.json","w") as f:
    json.dump(h,f,indent=4)    