#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 6


# In[3]:


pig = input("Enter a character:")

if(pig[0]=='A' or pig[0]=='a' or pig[0]=='E' or pig[0]=='e' or pig[0]=='I'
 or pig[0]=='i' or pig[0]=='O' or pig[0]=='o' or pig[0]=='U' or pig[0]=='u'):
        print((pig+"way").lower())
else:
    remove= pig[1:]+pig[0].lower()+"ay"

    print(remove.lower())


# In[ ]:


#Question 7


# In[69]:


bloodtype


# In[4]:



def bldcount(filename):
    openFile = open(filename)
    content = openFile.read()
    bloodList = list(content.split(" "))
    
    b_count = bloodList.count('B')
    a_count = bloodList.count('A')
    oo_count = bloodList.count('OO')
    o_count = bloodList.count('O')
    ab_count = bloodList.count('AB')
    
    if (b_count == 0):
        print("There are no patients of blood type B")
    if (b_count == 1):
        print("There is one patient of blood type B")
    else:
        print ("There are", bloodList.count('B'), "patients of blood type B")
    
    if (o_count == 0):
        print("There are no patients of blood type O")
    if (o_count == 1):
        print("There is one patient of blood type O")
    else:
        print ("There are", bloodList.count('O'), "patients of blood type O")
    
    
    
    if (oo_count == 0):
        print("There are no patients of blood type OO")
    if (oo_count == 1):
        print("There is one patients of blood type OO")
    else:
        print ("There are", bloodList.count('A'), "patients of blood type A")
   
    
    if (ab_count == 0):
        print("There are no patients of blood type AB")
    if (ab_count == 1):
        print("There is one patients of blood type AB")
    else:
        print ("There are", bloodList.count('AB'), "patients of blood type AB")    

   
bldcount("C:\\Users\\Babur\\OneDrive\\Desktop\\bloodtype.txt")


# In[45]:


#Question 8 
currency=pd.read_table("C:\\Users\\Babur\\OneDrive\\Desktop\\currency.txt")


# In[46]:


currency


# In[2]:


def curconv(a,b):
    ans=0
    l=['CHF','CNY','DKK','EUR','GBP','HKD','INR','JPY','MXN','MYR','NOK','NZD','PHP','SEK','SGD','THB']
    l1=[1.023741,0.155018,0.165144,1.229654,1.555099,0.127021,0.017764,0.012414,0.075185,0.314541,0.167706,0.800359,0.023323,0.148269,0.788871,0.031379]
    for i in range(len(l)):
        if(l[i]==a):
            ans=b*l1[i]
    return ans
print(curconv("EUR",100))
print(curconv("JPY",100))


# In[ ]:


#question 9


# In[2]:


Trying to add incompatible variables, as in 
adding 6 + ‘a’: NumberFormatException 
    
Referring to the 12th item of a list that has only 10 
items :ArrayIndexOutOfBoundsException

Using a value that is out of range for a function’s 
input, such as calling math.sqrt(-1.0): ArithmeticException
    
    
Using an undeclared variable, such as print(x)
when x has not been defined :ArithmeticException 
    
Trying to open a file that does not exist, such as 
mistyping the file name or looking in the wrong 
directory : FileNotFoundException


# In[50]:


#question 10


# In[1]:


def frequency(stringName):
    stringName = stringName.lower()
    a2z = 'abcdefghijklmnopqrstuvwxyz'
    count  = []
    for a in a2z:
        count.append(stringName.count(a))
    print (count)
    
frequency("The quick red fox got bored and went home")
frequency("Apple")


# In[ ]:




