from nltk import word_tokenize
from collections import OrderedDict
od = OrderedDict()
od1 = OrderedDict()



def readfile(filename):
    '''
    read file
    return format :
    '''
    f = open(filename)
    f=f.readlines()
    return f


import ast
Logs=[]
# open file and read the content in a list
with open('Data/Logs.txt', 'r') as filehandle:
    Logs = [current_place.replace("'","\'").strip() for current_place in (filehandle.readlines())]



skills=readfile("Data/Skills.txt")
roles=readfile("Data/roles.txt")
suffix=readfile("Data/suffix.txt")
Orgs=readfile("Data/company.txt")
Locations=readfile("Data/locations.txt")
#junk=readfile("Data/junk.txt")

roles=[ i.replace("\n","") for i in roles]
skills=[ i.replace("\n","") for i in skills]
suffix=[ i.replace("\n","") for i in suffix]
Orgs=[ i.replace("\n","") for i in Orgs]
Locations=[ i.replace("\n","") for i in Locations]
#junk=[ i.replace("\n","") for i in junk]
#
# Logs=Logs[:15]


trainingFileObj = open("Data/trainingFile_splitLines.txt", "w")
# #print(len(skills),skills[:10])
# #print(len(roles),roles[:10])
# #print(len(suffix),suffix[:10])
# #print(len(Orgs),Orgs[:10])
# #print(len(Locations),Locations[:10])
# #print(len(junk),junk[:10]
# Logs=Logs[:2]
# Logs=['ca, java developer requires','machine learning, sales, marketing']
count=0
for user_str in Logs:
    user_str=user_str.lower().replace("/"," ")
    print(count)
    trainingFileObj.write("\n")
    count+=1
    for i in roles:
        if i in user_str:
            user_str=(user_str.replace(i,"_ROLE_".join(i.split())))


    for j in skills:
        if j in user_str:
            user_str=(user_str.replace(j,"_SKILLS_".join(j.split())))

    for k in suffix:
        if k in user_str:
            user_str=(user_str.replace(k,"_SUFFIX_".join(k.split())))

    for l in Orgs:
        if l in user_str:
            user_str=(user_str.replace(l,"_ORGS_".join(l.split())))

    for m in Locations:
        if m in user_str:
            user_str=(user_str.replace(m,"_LOCATION_".join(m.split())))

    # for n in junk:
    #     if n in user_str:
    #         user_str=(user_str.replace(n,"_JUNK_".join(n.split())))

    user_str=word_tokenize(user_str)
    ##print(user_str)


    for i,user_str in enumerate(user_str):

        if "_SKILLS_" in user_str :
            for s,p in enumerate(user_str.split("_SKILLS_")):
                if s==0:
                    #print(p+ "  "+"B-SKILL")
                    tags=p+ "  "+"B-SKILL"
                    trainingFileObj.write((tags + "\n"))
                    #trainingFileObj.writable(str(tags))
                else:
                    #print(p+ "  "+"I-SKILL")
                    tags=p+ "  "+"I-SKILL"
                    trainingFileObj.write((tags + "\n"))
                    #trainingFileObj.writable(str(tags))

        elif "_ROLE_"in user_str:
            for r,d in enumerate(user_str.split("_ROLE_")):

                if r==0:
                    #print(d+ "  "+"B-ROLE")
                    tags=d+ "  "+"B-ROLE"
                    trainingFileObj.write((tags + "\n"))
                elif r!=0:
                    #print(d+"   "+"I-ROLE")
                    tags=d+"   "+"I-ROLE"
                    trainingFileObj.write((tags + "\n"))



        elif "_ORGS_" in user_str :
            for o,p in enumerate(user_str.split("_ORGS_")):
                if o==0:
                    #print(p+ "  "+"B-ORGS")
                    tags=p+ "  "+"B-ORGS"
                    trainingFileObj.write((tags + "\n"))
                else:
                    #print(p+ "  "+"I-ORGS")
                    tags=p+ "  "+"I-ORGS"
                    trainingFileObj.write((tags + "\n"))
        elif "_SUFFIX_"in user_str:
            for sf,d in enumerate(user_str.split("_SUFFIX_")):

                if sf==0:
                    #print(d+ "  "+"B-SUFFIX")
                    tags=d+ "  "+"B-SUFFIX"
                    trainingFileObj.write((tags + "\n"))
                elif sf!=0:
                    #print(d+"   "+"I-SUFFIX")
                    tags=d+"   "+"I-SUFFIX"
                    trainingFileObj.write((tags + "\n"))
        elif "_LOCATION_" in user_str :
            for loc,p in enumerate(user_str.split("_LOCATION_")):
                if loc==0:
                    #print(p+ "  "+"B-LOCATION")
                    tags=p+ "  "+"B-LOCATION"
                    trainingFileObj.write((tags + "\n"))
                else:
                    #print(p+ "  "+"I-LOCATION")
                    tags=p + "  " + "I-LOCATION"
                    trainingFileObj.write((tags + "\n"))
        # elif "_JUNK_"in user_str:
        #     for jnk,d in enumerate(user_str.split("_JUNK_")):
        #
        #         if jnk==0:
        #             #print(d+ "  "+"B-JUNK")
        #             tags=d+ "  "+"B-JUNK"
        #             trainingFileObj.write((tags + "\n"))
        #         elif jnk!=0:
        #             #print(d+"   "+"I-JUNK")
        #             tags=d+"   "+"I-JUNK"
        #             trainingFileObj.write((tags + "\n"))
        elif user_str in skills:
            #print(user_str + "    " + "B-SKILL")
            tags=user_str + "    " + "B-SKILL"
            trainingFileObj.write((tags + "\n"))
        elif user_str in roles:
            #print(user_str + "    " + "B-ROLE")
            tags=user_str + "    " + "B-ROLE"
            trainingFileObj.write((tags + "\n"))
        elif user_str in Orgs:
            #print(user_str + "    " + "B-ORGS")
            tags=user_str + "    " + "B-ORGS"
            trainingFileObj.write((tags + "\n"))
        elif user_str in suffix:
            #print(user_str + "    " + "B-SUFFIX")
            tags=user_str + "    " + "B-SUFFIX"
            trainingFileObj.write((tags + "\n"))
        elif user_str in Locations:
            #print(user_str + "    " + "B-LOCATION")
            tags=user_str + "    " + "B-LOCATION"
            trainingFileObj.write((tags + "\n"))
        # elif user_str in junk:
        #     #print(user_str + "    " + "B-JUNK")
        #     tags=user_str + "    " + "B-JUNK"
        #     trainingFileObj.write((tags + "\n"))

        else:
            #print(user_str + "    " + "O")
            tags=(user_str + "    " + "O")
            trainingFileObj.write((tags + "\n"))



# user_str='ca java developer requires,analyst'
# for i in roles:
#     if i in user_str:
#         user_str=(user_str.replace(i,"_".join(i.split())))
#
#
# for j in skills:
#     if j in user_str:
#         user_str=(user_str.replace(j,"-def-".join(j.split())))
#
#
# user_str=word_tokenize(user_str)
# #print(user_str)
#
#
# for i,user_str in enumerate(user_str):
#     if "-def-" in user_str :
#         for k,p in enumerate(user_str.split("-def-")):
#             if k==0:
#                 #print(p+ "  "+"B-SKILL")
#             else:
#                 #print(p+ "  "+"I-SKILL")
#     elif "_"in user_str:
#         for c,d in enumerate(user_str.split("_")):
#
#             if c==0:
#                 #print(d+ "  "+"B-ROLE")
#             elif c!=0:
#                 #print(d+"   "+"I-ROLE")
#
#     elif user_str in Locations:
#         #print(user_str+"    "+"B-LOC")
#     elif user_str in skills:
#         #print(user_str+"    "+"B-SKILL")
#     elif user_str in roles:
#         #print(user_str+"    "+"B-ROLE")
#     else:
#         #print(user_str + "    " + "O")
