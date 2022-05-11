import json

a=[["neelam","programer","24","2400"],["komal","trainer","24","20000"],["anuradha","hr","25","40000"],["abhishek","manager","29","63000"]]
e=["name","Designation","age","salary"]
dic={}
z=[]
for i in a:
    x=dict(zip(e,i))
    z.append(x)
j=1
for i in z:
    dic["emp"+str(j)]=i
    j=j+1
f=open("file3.json","w")
file=json.dump(dic,f,indent=2)
f.close()