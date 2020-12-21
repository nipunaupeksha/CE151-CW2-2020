#!/usr/bin/env python
# coding: utf-8

# In[1]:


from re import sub
from decimal import Decimal
#pip install prettytable
from prettytable import PrettyTable


# In[2]:


def tupleCreation(text):
    t = text.strip().split(" ")
    
    team = t[0]
    position = t[1]
    first_name=t[2]
    last_name=t[3]
    salary=t[4]
    
    validation = False
    
    if (len(team)<=15 and len(position)<=15 and len(first_name)<=15 and len(last_name)<=15) and len(salary)<=10:
        validation = True
    if validation==True:
        t = (last_name, first_name, salary, position, team)
        return t
    else:
        return False
    


# In[3]:


def option_1(content):
    last_name = input("Input the last name of a player: ")
    last_name=last_name.casefold()
    t = PrettyTable()
    t.field_names = ["Last Name", "First Name","Salary", "Position", "Team"]
    for item in content:
        if last_name == item[0].casefold():
            t.add_row(item)
    print(t)


# In[4]:


def option_2(content):
    lower = input("Input the lower range of salary: ")
    lower = Decimal(sub(r'[^\d.]', '', lower))
    upper = input("Input the upper range of salary: ")
    upper = Decimal(sub(r'[^\d.]', '', upper))
    
    t = PrettyTable();
    t.field_names = ["Last Name", "First Name","Salary", "Position", "Team"]
    

    for item in content:
        salary = Decimal(sub(r'[^\d.]', '', item[2]))
        if salary<=upper and salary>=lower:
            t.add_row(item)
            
    print(t)


# In[5]:


def option_3(content):
    team = input("Input the team name: ")
    team = team.casefold()
    
    t = PrettyTable();
    t.field_names = ["Last Name", "First Name"]
    
    for item in content:
        if team == item[4].casefold():
            t.add_row([item[0],item[1]])
    
    print(t)


# In[7]:


def option_4(content):
    position = input("Input position: ")
    position = position.casefold()
    team = input("Input team: ")
    team = team.casefold()
    
    t = PrettyTable()
    t.field_names = ["Last Name", "First Name","Salary", "Position", "Team"]
    
    for item in content:
        if position == item[3].casefold() and team == item[4].casefold():
            t.add_row(item)
    
    print(t)


# In[8]:


def option_5(content):
    position = input("Input position: ")
    position = position.casefold()
    lower = input("Input the lower range of salary: ")
    lower = Decimal(sub(r'[^\d.]', '', lower))
    upper = input("Input the upper range of salary: ")
    upper = Decimal(sub(r'[^\d.]', '', upper))
    
    t = PrettyTable();
    t.field_names = ["Last Name", "First Name","Salary", "Position", "Team"]
    

    for item in content:
        salary = Decimal(sub(r'[^\d.]', '', item[2]))
        if (salary<=upper and salary>=lower) and position == item[3].casefold():
            t.add_row(item)
    
    print(t)


# In[9]:


def option_6():
    last_name = input("Input last name: ")
    first_name = input("Input first name: ")
    salary = input("Input salary: ")
    position = input("Input position: ")
    team = input("Input team: ")
    
    validation = False
    
    if (len(team)<=15 and len(position)<=15 and len(first_name)<=15 and len(last_name)<=15) and len(salary)<=10:
        validation = True
    if validation==True:
        t = (last_name, first_name, salary, position, team)
        return t
    else:
        return False


# In[15]:


def printFullTable(content):
    t = PrettyTable()
    t.field_names = ["Last Name", "First Name","Salary", "Position", "Team"]
    for item in content:
        t.add_row(item)
        
    print(t)


# In[17]:


try:
    content = []
    
    userInput = input("Input filename to be read: ")
    filename = open(userInput)
    lines = filename.readlines()
    
    for line in lines:
        val = tupleCreation(line)
        if type(val)!=bool:
            content.append(val)

    printFullTable(content)
    userOptions =[
        "1. Display Full Details of the player with a given last name ",
        "2. Display full details of all players with a salary in particular range.",
        "3. Display first and last names of all players of a team.",
        "4. Display full details of a certain position and a team",
        "5. Display full details of a certain position and a salary in particular range.",
        "6. Add a player to the list",
        "7. Quit"
    ]
    
    val ="0"
    while(val!="7"):
        for option in userOptions:
            print(option)
        val = input("Enter a number: ")
        if val == "1": 
            option_1(content)
        elif val =="2":
            option_2(content)
        elif val =="3":
            option_3(content)
        elif val =="4":
            option_4(content)
        elif val =="5":
            option_5(content)
        elif val =="6":
            x = option_6()
            if type(x)!=bool:
                content.append(x)
            printFullTable(content)
        elif val =="7":
            print("Quitting ...")
            break
                
    
except FileNotFoundError:
    print("Error opening file")


# In[ ]:




