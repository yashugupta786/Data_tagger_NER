from nltk import word_tokenize
from collections import OrderedDict
od = OrderedDict()
od1 = OrderedDict()
user_str="looking for candidates for java developer,analyst java, java, python, software  for noida and delhi location"
roles=["java developer","analyst java","principal java consultant","python developer","software engineer"]
skills=['java','python','machine learning',"software"]
location=["noida","delhi"]
roles_list=[]
# for i in roles:
#     if i in user_str:
#         roles_list.append(i)
#         for k, l in enumerate(i.split(" ")):
#             if k == 0:
#                 # print(str(l) + "    " + "B-ROLE")
#                 od[l]="B-role"
#             else:
#                 # print(str(l) + "  " + "I-ROLE")
#                 od1[l]="I-role"
# print(roles_list)
# print(od)
# print(od1)


for i in roles:
    if i in user_str:
        user_str=(user_str.replace(i,"_".join(i.split())))

user_str=word_tokenize(user_str)
for i,user_str in enumerate(user_str):
    if user_str in skills:
        print(user_str+"    "+"B-SKILL")
    elif "_"in user_str:
        for c,d in enumerate(user_str.split("_")):

            if c==0:
                print(d+ "  "+"B-ROLE")
            else:
                print(d+"   "+"I-ROLE")
    elif user_str in location:
        print(user_str+"    "+"B-LOC")

    else:
        print(user_str + "    " + "O")
