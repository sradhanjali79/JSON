import json
x={"name":"shraddhanjali","school":"k.p.u.v.p","college":"royal science and commerce institude"}


f=open("file.json","w")
y=json.dump(x,f,indent=2)
f.close()