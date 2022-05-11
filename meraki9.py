# import json
# dic={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}}
# for i in dic:
#     x=input("enter..")
#     y=int(input("enter.."))
#     for p,q in dic[i].items():
#         if x==p:
#             dic[i][p]=str(int(q)-y )         
# with open("file4.json","w") as f:
#     json.dump(dic,f,indent=4)

import json
dic={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}}      
with open("file4.json","w") as f:
    json.dump(dic,f,indent=4)