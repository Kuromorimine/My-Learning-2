# from tkinter import *  #import *หมายถึง  ทุกอย่างของtkinter

# window = Tk() #Tk คือหน้าต่างแอป

# window.title("hello world")#titleคือ ให้หัวเรื่อง
# window.geometry("400x400")
# lab = Label(window,text= "Hello Guys",font=("Arial Bold",50))
# lab.grid(column=0,row=0)


# txt=Entry(window,width=30,state="disabled") #Zoneของการพิม #disable คือ ทำให้ใช้ไม่ได้
# txt.grid(column=0,row=2)#ระบุตำแหน่งแบบ column

# def click():
#     x="Hello "+ txt.get()
#     lab.configure(text=x)


# bt=Button(window,text="Click Me",bg="black",fg="pink",command=click)
# bt.grid(column=0,row=1)



# window.mainloop() #mainloop ให้มันรันไปเรื่อยๆ


from tkinter import *  #import *หมายถึง  ทุกอย่างของtkinter
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

window = Tk() #Tk คือหน้าต่างแอป

window.title("hello world")#titleคือ ให้หัวเรื่อง
window.geometry("400x400")
# lab = Label(window,text= "Hello Guys",font=("Arial Bold",50))
# lab.grid(column=0,row=0)


df2=pd.read_csv("EntriesGender.csv")
female=0
male=0
dict2={}
for i in range(46):
    
    sport=int(df2.loc[i,"Female"])+int(df2.loc[i,"Male"])
    dict2[df2.loc[i,"Discipline"]]=sport
    male = male + int(df2.loc[i,"Male"])
    female = female +int(df2.loc[i,"Female"])
    df22=pd.DataFrame(dict2,index =["1"])


df3=pd.read_csv("Medals.csv")
# df3
total=0
dict3={}
list3=[]
for i in range(93):
    # print(df3.loc[i,"Team/NOC"],end=" ")
    con =int(df3.loc[i,"Gold"])+int(df3.loc[i,"Silver"])+int(df3.loc[i,"Bronze"])
    # print(con,end="")
    total = total +con
    # print()
    list3.append(i)
    dict3[df3.loc[i,"Team/NOC"]]=con

def click21():
    lab1=Label(window,text ="female :"+str(female)+"male : "+str(male))
    lab1.grid(column=0,row=3)
def click22():
    lab2=Label(window,text = df22)
    lab2.grid(column=0,row=4)

# def click31():
#     lab3=Label(window,text=)

def click32():
    lab4=Label(window,text=str(total))
    lab4.grid(column=0,row=5)

bt1 = Button(window,text="Data21",bg="black",fg="pink",command=click21)
bt1.grid(column=0,row=1)

bt2 = Button(window,text="Data22",bg="black",fg="pink",command=click22)
bt2.grid(column=1,row=1)

bt3 = Button(window,text="Data31",bg="black",fg="pink")
bt3.grid(column=2,row=1)

bt4 = Button(window,text="Data32",bg="black",fg="pink",command=click32)
bt4.grid(column=3,row=1)


window.mainloop() #mainloop ให้มันรันไปเรื่อยๆ




