import json
x='{"a": 1,"a": 2,"a": 3, "a": 4,"b":1,"b": 2}'
y=json.loads(x)

f=open("file2.json","w")
file=json.dump(y,f)
f.close()
