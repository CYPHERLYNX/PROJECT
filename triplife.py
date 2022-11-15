import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
#import mysql.connector
import PIL
from PIL import ImageTk,Image

app = tk.Tk() 
app.title('Train_Reservation (Speedster)')
image_0=Image.open('D:\\Users\\Hembel\\Desktop\\New folder (2)\\PROJECT\\bgm.webp')
bck_end=ImageTk.PhotoImage(image_0)
app.geometry('500x300')
lbl=Label(app,image=bck_end)
lbl.place(x=0,y=0)
label=Label(app,text='FROM',background='white')
label.grid(column=2,row=1)
boxvalue=StringVar()
combobox = ttk.Combobox(app,textvariable=boxvalue,values=["-Select The Station-"," Ahmedabad Junction (ADI)","Allahabad Junction (ALD)","Anand Junction (ANND)","Asansol Junction (ASN)","Bhubaneshwar (BBS)","Bhopal Junction (BPL)","Vadodara Junction (BRC)","Varanasi Junction (BSB)","Bhusaval Junction (BSL)","Barddhaman Junction (BWN)","Vijayawada Junction (BZA)"," Kanpur Central (CNB)","Delhi Junction (DLI)","Erode Junction (ED)","Itarsi Junction (ET)","Gorakhpur Junction (GKP)","Gwalior Junction (GWL)","Ghaziabad Junction (GZB)","Howrah Junction (HWH)","Jhansi Junction (JHS)","Jaipur Junction (JP)"])
combobox.grid(column=2,row=2)
combobox.current(0)
label1=Label(app,text='To',background='white')
label1.grid(column=6,row=1)
boxvalue1=StringVar()
combobox1=ttk.Combobox(app,textvariable=boxvalue1,values=["-Select The Station-"," Ahmedabad Junction (ADI)","Allahabad Junction (ALD)","Anand Junction (ANND)","Asansol Junction (ASN)","Bhubaneshwar (BBS)","Bhopal Junction (BPL)","Vadodara Junction (BRC)","Varanasi Junction (BSB)","Bhusaval Junction (BSL)","Barddhaman Junction (BWN)","Vijayawada Junction (BZA)"," Kanpur Central (CNB)","Delhi Junction (DLI)","Erode Junction (ED)","Itarsi Junction (ET)","Gorakhpur Junction (GKP)","Gwalior Junction (GWL)","Ghaziabad Junction (GZB)","Howrah Junction (HWH)","Jhansi Junction (JHS)","Jaipur Junction (JP)"])
combobox1.current(0)
combobox1.grid(column=6,row=2)

adult=IntVar()
children=IntVar()
rawa=0
rawc=0
labelhead=Label(app,text='Passengers',background='white')
labelhead.grid(column=4,row=3)
label2=Label(app,text='Adults',background='white')
label2.grid(column=2,row=4)
adult=tk.Spinbox(app, from_=0, to=5,increment=1)
adult.grid(column=2,row=5)
label3=Label(app,text='Children',background='white')
label3.grid(column=6,row=4)
children=tk.Spinbox(app,from_=0,to=5,increment=1)
children.grid(column=6,row=5)

#GUI -- trip
var=IntVar()
var1=IntVar()
selection=''
selection1=''
def sel1():
   global selection
   selection=str(var.get())
   print(selection)
   
Label(app, text = "Match Type",background='white').grid(row=6, column=4)
Radiobutton(app, text = "One_Way", variable = var, value=1,command=sel1).grid(row=7,column=4)
'''Radiobutton(app, text = "Two_Way", variable = var, value=2,command=sel1).grid(row=8,column=4)'''
#class
def cls():
    global selection1
    selection1=str(var1.get())
    
Label(app,text="Gallery Class",background='white').grid(row=9,column=2)
Radiobutton(app, text='AC First Class', variable = var1, value=1,command=cls).grid(row=10,column=2),
Radiobutton(app,text='Ac 2 Tier', variable = var1, value=2,command=cls).grid(row=10,column=4)
Radiobutton(app,text='General Class', variable = var1, value=3,command=cls).grid(row=10,column=6)
Radiobutton(app,text='Sleeper Class', variable = var1, value=4,command=cls).grid(row=10,column=8)
def end():#function to end app-GUI
    global rawa
    global rawc
    f1=boxvalue.get()  #from value
    f2=boxvalue1.get() #to value
    a=adult.get()
    rawa=a
    b=children.get()
    rawc=b
    if f1=='-Select-' and f2=='-Select-':
        return messagebox.showerror('Error','Please select To')
    elif f2=='-Select-':
        return messagebox.showerror("Error", "Please select FROM")
    elif f1==f2:
        return messagebox.showerror("Error", "Invalid Match!")
    elif f1=='-Select-':
        return messagebox.showerror('Error','Please select From ')
    elif rawa=='0' and rawc=='0':
        return messagebox.showerror("Error", "Choose no. of seats")
    elif selection=='':
        return messagebox.showerror("Error", "Choose Match Type")
    elif selection1=='':
        return messagebox.showerror("Error", "Choose Gallery Class") 
    else:
        app.destroy()
img=Image.open('PL1.jpg')
img1=Image.open('LP2.png')
img1=img1.resize((50,50),Image.ANTIALIAS)
img=img.resize((50,50),Image.ANTIALIAS)
render=ImageTk.PhotoImage(img)
render1=ImageTk.PhotoImage(img1)
Label(app,image=render1).place(x=380,y=210)
Label(app,image=render).place(x=440,y=210)
tk.Button(app,text='Continue',command=end,bg='yellow').grid(column=8,row=6)
app.mainloop()
#values
f1=boxvalue.get()  #from value
f2=boxvalue1.get() #to value
sel1()    #method of travel value
print(rawa,rawc)  #adult and children value raw-adult  raw-children
#conversions(str to int)
adultnumber=int(rawa)
childnumber=int(rawc)
deptime1=''
arrtime1=''
pricead1=0
pricech1=0
tprice=0
flname=''
flag=0
totaltime=''
'''def database():
    global adultnumber
    global childnumber
    global adultlist
    global childlist
    global adpslist
    global chpslist
    global bnumber
    global selection
    global f1
    global f2
    global cnum
    global cvvnum
    global expmonth
    global expyear
    type1=''
    if selection=='1':
        type1='oneway'
    else:
        type1='roundtrip'
    db = mysql.connector.connect(host='localhost',user='root',passwd='isamrn37',database='triplife')
    mycursor=db.cursor()
    mycursor.execute("use trip")
    db.commit()
    if adultnumber!=0:
        for i in range(adultnumber):
            mycursor=db.cursor()
            mycursor.execute("insert into details values (%s,%s,%s,%s, %s, %s)",(bnumber,adultlist[i],adpslist[i],type1,f1,f2))
            db.commit()
    if childnumber!=0:
        for i in range(childnumber):
            mycursor=db.cursor()
            mycursor.execute("insert into details values (%s,%s,%s,%s, %s, %s)",(bnumber,childlist[i],chpslist[i],type1,f1,f2))
            db.commit()
    db.close()
    db = mysql.connector.connect(host='localhost',user='root',passwd='isamrn37',database='trip')
    mycursor=db.cursor()
    mycursor.execute("use trip")
    mycursor.execute("insert into payment values (%s,%s,%s,%s)",(cnum,cvvnum,expmonth,expyear))                                                                                                                                        
    db.commit()'''
def ltw1():     
    global flag
    global flname
    global pricead1
    global pricech1
    global deptime1
    global arrtime1
    global selection1
    global tprice
    global f1
    global f2
    global totaltime
    flname='ltw'
    basefare=10
pricead2=0
pricech2=0
deptime2=''  
arrtime2=''
tprice1=0
af1=''
af2=''
def platform1():
    global flag
    global af1
    global af2
    global pricead
    global pricech
    global deptime2
    global arrtime2
    global selection1
    global tprice1
    global flname1
    global f1
    global f2
    global totaltime
    flname1='Lusail '
    basefare=10

ltw1()
platform1()
   
def confirmation():
    global bnumber
    confirmation=tk.Tk()
    confirmation.title('Booking Confirmation')
    confirmation.geometry('500x500')
    bnumber=random.randint(10000,40000)
    
    def quit():
        confirmation.destroy()
        database()
    Label(confirmation,text='Confirmation',font='Helvetica 12 bold').grid(row=1,column=2)
    Label(confirmation,text='Booking Is Confirmed').grid(row=2,column=2)
    Label(confirmation,text='Your Booking Reference Number:'+str(bnumber),font='Helvetica 12 bold').grid(row=3,column=2)
    Label(confirmation,text='Contact Us:').grid(row=4,column=1)
    Label(confirmation,text='Phone Number:987654378').grid(row=5,column=2)
    Label(confirmation,text='Email:Speedster.com').grid(row=6,column=2)
    Button(confirmation,text='Quit',command=quit).grid(row=7,column=3)
    bnumber=int(bnumber)
cnum=''
cvvnum=''
expmonth=''
expyear=''
def payments():#payment window
    payments=tk.Tk()
    payments.geometry('700x350')
    payments.title('Payment')
    img1=Image.open('card.png')
    img1=img1.resize((110,110),Image.ANTIALIAS)
    render1=ImageTk.PhotoImage(img1)
    Label(payments,image=render1).place(x=100,y=220)
    v=tk.IntVar()
    cnumber=StringVar()
    cvv=StringVar()
    month=StringVar()
    year=StringVar()
    def check():
        global cnum
        global cvvnum
        global expmonth
        global expyear
        ctype=v.get()
        cnum=cnumber.get()
        cvvnum=cvv.get()
        expmonth=month.get()
        expyear=year.get()
        
        if ctype==0:
            return messagebox.showerror('Error','Select Card Type')
        elif cnum=='':
            return messagebox.showerror('Error','Enter Card Number')
        elif cvvnum=='':
            return messagebox.showerror('Error','Enter CVV number')
        elif expmonth=='':
            return messagebox.showerror('Error','Enter Month of Expiry')
        elif expyear=='':
            return messagebox.showerror('Error','Enter Year of Expiry')
        elif len(cvvnum)<3:
            return messagebox.showerror('Error','Enter valid CVV number')
        elif len(cvvnum)>3:
            return messagebox.showerror('Error','Enter valid CVV number')
        else:
            payments.destroy()
            confirmation()
    Label(payments,text='Payments',font='Helvetica 12 bold').grid(row=1,column=2)
    Label(payments,text='>>Total amount to pay: INR'+totalprice).grid(row=2,column=1)
    Label(payments,text='>>Select Card Type').grid(row=3,column=1)
    Radiobutton(payments,text='Credit Card',variable=v,value=1).grid(row=4,column=1) 
    Radiobutton(payments,text='Debit Card',variable=v,value=2).grid(row=4,column=2)
    Label(payments,text='Enter Card Number').grid(row=5,column=1)
    Entry(payments,width=30,textvariable=cnumber).grid(row=5,column=2)
    Label(payments,text='CVV').grid(row=6,column=1)
    Entry(payments,width=3,textvariable=cvv).grid(row=7,column=1)
    Label(payments,text='Enter Card expiry date').grid(row=8,column=2)
    Label(payments,text='Month').grid(row=9,column=2)
    Entry(payments,width=4,textvariable=month).grid(row=10,column=2)
    Label(payments,text='(Enter in MM format)').grid(row=11,column=2)
    Label(payments,text='Year').grid(row=9,column=3)
    Entry(payments,width=6,textvariable=year).grid(row=10,column=3)
    Label(payments,text='(Enter in YYYY format)').grid(row=11,column=3)
    Button(payments,text='Confirm booking',command=check).grid(row=12,column=3)
    
    payments.mainloop()



def details(): #details GUI-GLOBAL 
        def command1():
            global adultlist
            global childlist
            global adpslist
            global chpslist
            a=adstr.get()
            b=chstr.get()
            c=psadstr.get()
            d=pschstr.get()
            adultlist=list(a.split(','))
            childlist=list(b.split(','))
            adpslist=list(c.split(','))
            chpslist=list(d.split(','))
 
            details.destroy()
            payments()
            
        details=tk.Tk()
        details.geometry('500x500')
        Label(details,text='Enter Your Details').grid(row=1,column=4)
        Label(details,text='(Name)Adults').grid(row=2,column=4)
        adstr=StringVar()
        chstr=StringVar()
        psadstr=StringVar()
        pschstr=StringVar()
        Entry(details,textvariable=adstr,width=40).grid(row=3,column=4)
        Label(details,text='(Name)Children').grid(row=4,column=4)
        Entry(details,textvariable=chstr,width=40).grid(row=5,column=4)
        Label(details,text='Address-(adults)').grid(row=6,column=4)
        Entry(details,textvariable=psadstr,width=40).grid(row=7,column=4)
        Label(details,text='Address-(children)').grid(row=8,column=4)
        Entry(details,textvariable=pschstr,width=40).grid(row=9,column=4)
        Button(details,text='proceed',command=command1).grid(row=10,column=5) 
       

        

def itenary(): #itenary and details window
    global matchname
    global totalprice
    global origin
    global destination
    global Departure_Time
    global endtime
    itenary=tk.Tk()
    itenary.geometry('600x500')
    Label(itenary,text='Details',font='Helvetica 12 bold').grid(row=1,column=3)
    Label(itenary,text='From:'+origin+'      '+'To:'+destination).grid(row=3,column=3)
    Label(itenary,text='Departure_Time:12.30 AM'+' Arrival Time:2.00 AM').grid(row=4,column=3)
    Label(itenary,text='Travel Duration:1.5 hrs').grid(row=5,column=3)
    Label(itenary,text='Seats',font='Helvetica 12 bold').grid(row=6,column=3)
    Label(itenary,text='Number of Adults:'+str(adultnumber)).grid(row=7,column=3)
    Label(itenary,text='Number of Children:'+str(childnumber)).grid(row=8,column=3)
    def insure():
            global totalprice
            totalprice=int(totalprice)
            totalprice=totalprice+15
            totalprice=str(totalprice)
    var3=IntVar()
    Checkbutton(itenary, text="Add Insurance(INR 20)",variable=var3,command=insure).grid(row=9,column=3)
    def func():
        itenary.destroy()
        details()
    Button(itenary,text='Proceed for booking',command=func).grid(row=10,column=4)
    itenary.mainloop()
matchname=''
totalprice=''
origin=''
destination=''
Departure_Time=''
endtime=''
def end1():#domestic forward
    global matchname
    global totalprice
    global origin
    global destination
    global Departure_Time
    global endtime
    fselection.destroy()
    matchname=flname1
    origin=f1
    destination=f2
    totalprice=tprice1
    Departure_Time=deptime2
    endtime=arrtime2
    itenary()
   
def end2():#international forward
    global matchname
    global totalprice
    global origin
    global destination
    global Departure_Time
    global endtime
    fselection.destroy()
    matchname=flname
    origin=f1
    destination=f2
    totalprice=tprice
    Departure_Time=deptime1
    endtime=arrtime1
    itenary()

def details1():#platform
    round.destroy()
    global matchname
    global origin
    global destination
    global Departure_Time
    global endtime
    global totalprice
    global f1
    global f2
    itenary=tk.Tk()
    itenary.title('Itenary')
    itenary.geometry('500x500')
    matchname=flname1
    totalprice=str(tprice1*2)
    platform1()
    Departure_Time=deptime2
    endtime=arrtime2
    origin=f1
    destination=f2
    f1,f2=f2,f1
    platform1()

    def insure():
            global totalprice
            totalprice=int(totalprice)
            totalprice=totalprice+15
            totalprice=str(totalprice)
    def outward():
        itenary.destroy()
        details()
    var8=IntVar()
    Checkbutton(itenary, text="Add Travel Insurance(INR 20)",variable=var8,command=insure).grid(row=10,column=2)
    Button(itenary,text='Proceed',command=outward).grid(row=11,column=3)
def details2():#ltw
    round.destroy()
    global matchname
    global origin
    global destination
    global Departure_Time
    global endtime
    global totalprice
    global f1
    global f2
    itenary=tk.Tk()
    itenary.title('Itenary')
    itenary.geometry('500x500')
    matchname=flname
    totalprice=str(tprice*2)
    ltw1()
    Departure_Time=deptime1
    endtime=arrtime1
    origin=f1
    destination=f2
    f1,f2=f2,f1
    ltw1()
    Departure_Time1=deptime2
    endtime1=arrtime2
    origin1=f1
    destination1=f2
    Label(itenary,text='Onward Flight--',font='Helvetica 12 bold').grid(row=1,column=1)
    Label(itenary,text='Flight Name:'+matchname).grid(row=2,column=2)
    Label(itenary,text=origin+'    To    '+destination).grid(row=3,column=2)
    Label(itenary,text='Departure_Time Time:'+Departure_Time+'     '+'endtime Time:'+endtime).grid(row=4,column=2)
    Label(itenary,text='Return Flight--',font='Helvetica 12 bold').grid(row=5,column=1)
    Label(itenary,text='Flight Name:'+matchname).grid(row=6,column=2)
    Label(itenary,text=origin1+'    To    '+destination1).grid(row=7,column=2)
    Label(itenary,text='Departure_Time Time:'+Departure_Time1+'     '+'endtime Time:'+endtime1).grid(row=8,column=2)#timings
    Label(itenary,text='************************').grid(row=9,column=1)
    def insure():
            global totalprice
            totalprice=int(totalprice)
            totalprice=totalprice+15
            totalprice=str(totalprice)
    def outward():
        itenary.destroy()
        details()
    var8=IntVar()
    Checkbutton(itenary, text="Add Insurance(RS 15)",variable=var8,command=insure).grid(row=10,column=2) 
    Button(itenary,text='Proceed',command=outward).grid(row=11,column=3)

def oneway(): #oneway-gui
    global tprice
    global tprice1
    global flname
    global flname1
    tprice=str(tprice)
    tprice1=str(tprice1)
    img=Image.open('platform.jpg')
    img1=Image.open('ltw.webp')
    img1=img1.resize((110,50),Image.ANTIALIAS)
    img=img.resize((110,50),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(img)
    render1=ImageTk.PhotoImage(img1)
    Label(fselection,image=render1).place(x=100,y=210)
    Label(fselection,image=render).place(x=220,y=210)
    if flag==0:#domestic
        Label(fselection,text=f1+'  --- '+f2,font='Helvetica 12 bold').grid(row=5,column=3)
        Label(fselection,text = ">>On-Going Trip>>",font='Helvetica 12 bold').grid(row=6, column=2)
        book2=ttk.Button(fselection,text='Book',command=end1)
        book2.grid(row=8,column=5)
    fselection.mainloop()
if selection=='1':
    fselection=tk.Tk()
    fselection.title('One_Way')
    fselection.geometry('700x400')
    oneway()
'''if selection=='2':
    round=tk.Tk()
    round.title('Two_Way')
    round.geometry('600x500')
    roundtrip()'''
