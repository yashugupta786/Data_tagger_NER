from nltk import word_tokenize
from collections import OrderedDict
od = OrderedDict()
od1 = OrderedDict()
user_str="digital expert marketing"
roles=["digital marketing expert", "expert"]
skills=["digital marketing", "marketing"]
location=["noida","delhi"]
roles_list=[]


for i in roles:
    if i in user_str:
        user_str=(user_str.replace(i,"_".join(i.split())))


for j in skills:
    if j in user_str:
        user_str=(user_str.replace(j,"-def-".join(j.split())))


user_str=word_tokenize(user_str)
print(user_str)


for i,user_str in enumerate(user_str):
    if "-def-" in user_str :
        for k,p in enumerate(user_str.split("-def-")):
            if k==0:
                print(p+ "  "+"B-SKILL")
            else:
                print(p+ "  "+"I-SKILL")
    elif "_"in user_str:
        for c,d in enumerate(user_str.split("_")):

            if c==0:
                print(d+ "  "+"B-ROLE")
            elif c!=0:
                print(d+"   "+"I-ROLE")

    elif user_str in location:
        print(user_str+"    "+"B-LOC")
    elif user_str in skills:
        print(user_str+"    "+"B-SKILL")
    elif user_str in roles:
        print(user_str+"    "+"B-ROLE")
    else:
        print(user_str + "    " + "O")
