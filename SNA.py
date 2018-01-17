import inspect,os
print('Welcome to Assignment 3 (Part1)')
print('-------------------------------')
network=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/sn.txt ','r+')
alldata={}
for line in network:
    line=line.replace(":"," ").split()
    alldata[line[0]]=line[1:]
def AddUser(new_user,existing_user):
    alldata[new_user]=existing_user
    alldata[existing_user].append(new_user)
    print("User '%s' has been added and tied to '%s' successfully"%(txt[1],txt[2]))
def RemoveUser(user_name):
    del alldata[user_name]
    for i in alldata.keys():
        for j in alldata[i]:
            if j==user_name:
                alldata[i].remove(j)
    print("User '%s' and its all relations have been removed successfully."%(txt[1]))
def AddNewRelation(source_user,target_user):
    if target_user and source_user in alldata.keys():
        if target_user not in alldata[source_user] and source_user not in alldata[target_user]:
            alldata[source_user].append(target_user)
            alldata[target_user].append(source_user)
            print("Relation between '%s' and '%s' has been added succesfully."%(txt[1],txt[2]))
        else:
            print("A relation between '%s' and '%s' already exists!!"%(txt[1],txt[2]))
def RemoveExistingRelation(source_user,target_user):
    alldata[source_user].remove(target_user)
    alldata[target_user].remove(source_user)
    print("A relation between '%s' and '%s' has been removed successfully."%(txt[1],txt[2]))
def RankUsers(toplist_size):
    dict1={}
    for i in alldata.keys():
        rank=len(alldata[i])
        print("User '%s' has %d friends"%(i,rank))
        dict1[i]=(rank)
    list1=[]
    for j in dict1.values():
        list1.append(j)
    for k in range(len(list1)-1, 0, -1):
        for index in range(k):
             if list1[index] < list1[index + 1]:
                list1[index], list1[index + 1] = list1[index + 1], list1[index]
    count=0
    for b in list1:
        for c in dict1.keys():
            if dict1[c]==b:
                 del dict1[c]
                 print("%d. '%s':%d"%((count+1),c,b))
                 count+=1
                 if count==(toplist_size):
                    break
        if count==(toplist_size):
                    break
def SuggestFriendship(username,MD):
    item=alldata[username]
    allval=[]
    for leng in range(len(alldata[username])):
        for sel in item[leng]:
            for d in alldata[sel]:
                allval.append(d)
    check=[]
    print("Suggestion List for '%s' (when MD is %d):"%(username,MD))
    for cnt in allval:
        if cnt!=username:
            if cnt not in check:
                if 1<allval.count(cnt)>=int(MD):
                    print("'%s' has %d mutual friends with %s"%(username,allval.count(cnt),cnt))
        check.append(cnt)
com1=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/commandsP1.txt ','r+')
for line in com1:
    txt=line.split()
    val=txt[0]
    if val=="AU":
        if len(txt)==3:
            if txt[1] in alldata:
                print("This user already exists!!")
            else:
                if not txt[2] in alldata:
                    print("There is no user named '%s'"%(txt[2]))
                else:
                    AddUser(txt[1],txt[2])
        else:
            print("Error: Wrong input type for 'AU'!")
    elif val=="RU":
        if len(txt)==2:
            if txt[1] in alldata:
                RemoveUser(txt[1])
            else:
                print("There is no user named '%s'!!"%(txt[1]))
        else:
            print("Error: Wrong input type! for 'RU'!")
    elif val=="AR":
         if len(txt)==3:
            if (txt[1] not in alldata.keys()) or (txt[2] not in alldata.keys()):
                print("No user named '%s' or '%s' found!!"%(txt[1],txt[2]))

            else:
                AddNewRelation(txt[1],txt[2])
         else:
             print("Error: Wrong input type! for 'AR'!")
    elif val=="RR":
         if len(txt)==3:
            if txt[1] in alldata.keys():
                if txt[2] in alldata.keys():
                    if txt[1] in alldata[txt[2]] and txt[2] in alldata[txt[1]]:
                        RemoveExistingRelation(txt[1],txt[2])
                    else:
                        print("No relation between '%s' and '%s' found!"%(txt[1],txt[2]))
                else:
                    print("No user named '%s' or '%s' found!!"%(txt[1],txt[2]))
            else:
                print("No user named '%s' or '%s' found!!"%(txt[1],txt[2]))
         else:
             print("Error: Wrong input type! for 'RR'!")
    elif val=="PA":
        if len(txt)==2:
            x=int(txt[1])
            if x<len(alldata.keys()):
                RankUsers(x)
            else :
                print("Invalid input since n is greater than %d"%(len(alldata.keys())))
        else:
             print("Error: Wrong input type! for 'PA'!")
    elif val=="SA":
        if len(txt)==3:
            y=int(txt[2])
            if txt[1] in alldata.keys():
                if y<=len(alldata[txt[1]]):
                    SuggestFriendship(txt[1],y)
                else:
                    print("User '%s' has less friend than %d"%(txt[1],y))
            else:
                print("No user named '%s' found!!"%(txt[1]))
        else:
            print("Error: Wrong input type! for 'SA'!")
    else:
        print("Error: Undefined command type!")
network.close()
network=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/sn.txt ','w+')
for i in alldata.keys():
    add=i+":"
    for j in alldata[i]:
        add=add+j+" "
    network.write(add+"\n")
network.close()




