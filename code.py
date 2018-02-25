
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


fn=[] #contains first name
ln=[] #contains last name
dobgn=[] #contains date of birth and gender

with open("Deduplication Problem - Sample Dataset.csv","r") as alldata:
    data=alldata.readlines()
    for line in data:
        words=line.split(',')
        fn.append(words[3])
        ln.append(words[0])
        dobgn.append(words[1]+words[2])


# In[3]:


def exist(temp):
    for i in range(0,len(groups)):
        if temp==groups[i]:
            return True
    return False


# In[4]:


groups=[] # contains unique dob and gender combination
groupfn=[] #a 2d list, each row contains all first names of a unique dob and gender combination 
groupln=[] #a 2d list, each row contains all last names of a unique dob and gender combination 
for i in range(1,len(fn)):
    temp=dobgn[i]
    if (not exist(temp)):
        groups.append(temp)


# In[5]:


for i in range(len(groups)):
    temp=groups[i]
    localfn=[]
    localln=[]
    for j in range(len(dobgn)):
        if dobgn[j]==temp:
            firstname=fn[j]
            localfn.append(firstname[0:-1])
            localln.append(ln[j])
    groupfn.append(localfn)
    groupln.append(localln)


# In[6]:


#output a new csv file after deduplication

csv = open("output.csv", "w")
columnTitleRow = "ln, dob, gn, fn\n"
csv.write(columnTitleRow)


# In[7]:


def commonexist(str1,str2): #function to check if common substring exists between two names 
    a=str1.split(' ')
    b=str2.split(' ')
    for i in range(len(a)):
        if len(a[i])<3: #this can avoid some words( like Jr., any single character)
            continue
        for j in range(len(b)):
            if a[i]==b[j]:
                return True
    return False


# In[8]:


for i in range(len(groups)):
    current_dobgn=groups[i]
    unique=np.ones(len(groupfn[i])) #array to tell if some thing is unique or repeated
    ### comparing first names and last names
    for j in range(len(groupfn[i])-1):
        for k in range(j+1,len(groupfn[i])):
            if(commonexist(groupfn[i][j],groupfn[i][k])): #checking first name
                if(commonexist(groupln[i][j],groupln[i][k])): #checking last name
                    unique[k]=0
    
    #write to the output
    for p in range(len(unique)):
        if unique[p]==1:
            row = groupln[i][p] + "," + current_dobgn[0:-1] + "," + current_dobgn[-1] + "," +groupfn[i][p] + "\n"
            #print(row)
            csv.write(row)
                    

