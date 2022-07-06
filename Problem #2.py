#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# problem 2 


# In[ ]:


#question 1


# In[ ]:


a=0

def b():
    global a 
    a= c(a)
    
def c(a):
    return a+2


# In[ ]:


b() 
b()
b()
a

When the final expression is evaluated, the value displayed is 6.
This is because a is first set to 0 when b() is called. 
Then with a value O,c() is invoked, returning 2. When b() is invoked a second time, a is set to 2. 
Then, with a value of 2,c() is invoked, returning 4. When b() is invoked a third time is a set to 4. Then,with a value of 4, c() is invoked, returning 6


# In[ ]:


# question2


# In[ ]:


fileName = input("Enter file name ")
fileName= open("C:/Users/Babur/OneDrive/Desktop/midterm.py")

def fileLength(file):
    try:
        fileName= open(file)
        content = fileName.read()
        fileName.close()
        fileLengh= len(content)
        print('Number of characters in text file :{}'.format(fileLengh))

    except:
        print('File idterm.py not found')
    


# In[ ]:


fileName= "C:/Users/Babur/OneDrive/Desktop/midterm.py"
fileLength(fileName)


# In[ ]:


fileName = input("Enter file name")
fileLength(fileName)


# In[ ]:


# question 3


# In[ ]:


class Marsupial:
    def __init__(self):
        self.lst=[]
        
    def put_in_pouch(self,item):
        self.lst.append(item)
        
    def pouch_contents(self):
        return self.lst
    
    


# In[ ]:


m=Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetuck')
m.put_in_pouch('kitten')


# In[ ]:


class Kangaroo(Marsupial):
    
    def __init__(self,x,y):
        Marsupial.__init__(self)
        self.x=x
        self.y=y
        
    def jump(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return 'I ama Kangaroo located at coordinates({},{})'.format(self.x,self.y)
    
    


# In[ ]:


k=Kangaroo(0,0)
print(k)


# In[ ]:


k.put_in_pouch('doll')
k.put_in_pouch('firestruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())


# In[ ]:


k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# In[ ]:


# question 4


# In[ ]:


def collatz(n):
    
    print(n)
    if n==1:
        return 
    elif n%2==0:
        return collatz(n//2)
    else:
        return collatz(n*3+1)
 


# In[ ]:


collatz(1)
collatz(10)


# In[ ]:


#question 5


# In[ ]:


def binary(n):
   
    if n > 1:
        binary(n//2)
    print(n % 2, end='')
          


# In[ ]:


binary(0)
print()
binary(1)
print()
binary(3)
print()
binary(9)
print()


# In[ ]:


#question 6 


# In[26]:


from html.parser import HTMLParser 

class HeadingParser(HTMLParser):
    headers=['h1','h2','h3','h4','h5','h6']
    
    def handle_starttag(self,tag,attrs):
        if tag in self.headers:
            print(tag)
    
    def handle_endtag(self,tag):
        if tag in self.headers: 
            print(tag)
    
    def handle_data(self,data):
            print(data)
            

parser= HeadingParser()
infile=open("C:/Users/Babur/OneDrive/Desktop/w3c.html")
content=infile.read()
infile.close()
hp= HeadingParser()
hp.feed(content)


# In[ ]:


#question 7


# In[32]:


def webdir(url, depth, indent):
    if depth == 0:
        return
   
    print(indent * ' ' + url)
    
    try:
        response= requests.get(url)
    except:
        return
    
    soup=BeautifulSoup(response.text, 'html.parser')
    
    
   
    for link in soup.find_all('a'):
        webdir(link.get('href'), depth - 1, indent + 1)

webdir("http://reed.cs.depaul.edu/lperkovic/csc242/test1.html", 2, 0)


# In[ ]:


#question 8 


# In[ ]:


import sqlite3
con = sqlite3.connect('web4.db')
cur = con.cursor()


# In[ ]:


cur.execute("CREATE TABLE Weather (City, Country,Season,Temperature,Rainfall)")
cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India','Winter',24.8,5.9)")
cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India','Spring',28.4,16.2)")
cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India','Summer',27.9,1549.2)")
cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India','Fall',27.6,346.0)")
cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom','Winter',4.2,207.7)")
cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom','Spring',8.3,169.6)")
cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom','Summer',15.7,157.0)")
cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom','Fall',10.4,218.5)")
cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt','Winter',13.6,16.5)")
cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt','Spring',20.7,6.5)")
cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt','Summer',27.7,0.1)")
cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt','Fall',22.2,4.5)")


# In[ ]:


cur.execute('SELECT * FROM Weather')

for record in cur:
    print(record)


# In[ ]:


cur.execute('SELECT Temperature FROM Weather')
print(cur.fetchall())
cur.execute('SELECT DISTINCT City FROM Weather')
print(cur.fetchall())
Country = 'India'
cur.execute('SELECT * FROM Weather WHERE Country = ?', (Country,))
print(cur.fetchall())
Season = 'Fall'
cur.execute('SELECT * FROM Weather WHERE Season = ?', (Season,))
print(cur.fetchall())


# In[ ]:


cur.execute('SELECT City, Country, Season FROM Weather WHERE Rainfall between 200 and 400')
cur.fetchall()


# In[ ]:



cur.execute("SELECT City, Country FROM Weather WHERE Season = 'Fall' and Temperature >20 order by Temperature")

cur.fetchall()


# In[ ]:


cur.execute("SELECT SUM(Rainfall) FROM Weather WHERE City = 'Cairo'")
cur.fetchall()


# In[ ]:


cur.execute("SELECT Season,SUM(Rainfall) FROM Weather group by Season")
cur.fetchall()


# In[ ]:


#question 9


# In[ ]:


words =["The", "quick","brown","fox","jumps","over","the","lazy","dog"]
converted_list = [x.upper() for x in words]
print(converted_list)

converted_list = [x.lower() for x in words]
print(converted_list)

converted_list= [len(x) for x in words]
print(converted_list)

converted_list= [[x.upper(),x.lower(),len(x)] for x in words]
print(converted_list)
converted_list= [x for x in words if len(x)>3]
print(converted_list)


# In[ ]:




