from tkinter  import *
from tkinter import ttk
from tkinter import messagebox
import random
import os
from datetime import date
from datetime import datetime
#import mysql.connector
import psycopg2
from PIL import ImageTk,Image
con = psycopg2.connect(database="dbms_miniproject", user="postgres", password="postgres", host="127.0.0.1",
                        port="5432")
c = con.cursor()
def chres(S4,gbid):
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    e="""Select bid from reservation"""
    c.execute(e)
    blist=[]
    blist=[b[0] for b in c.fetchall()]
    #print(blist)
    con.commit()
    if gbid not in blist:
        messagebox.showinfo("Not Found","Sorry there were no matching reservations",parent=S4)
        return
    else:
        e1="""select cname from customer where bid=%s"""
        c.execute(e1,(str(gbid),))
        cname=[b[0] for b in c.fetchall()]
        #print(cname)
        con.commit()
        e2="""select dateofres from reservation where bid=%s"""
        c.execute(e2,(str(gbid),))
        dateres=[b[0] for b in c.fetchall()]
        con.commit()
        e3="""select hours from reservation where bid=%s"""
        c.execute(e3,(str(gbid),))
        hrs=[b[0] for b in c.fetchall()]
        con.commit()
        e4="""select mins from reservation where bid=%s"""
        c.execute(e4,(str(gbid),))
        mns=[b[0] for b in c.fetchall()]
        con.commit()
        e5="""select no_of_seats from reservation where bid=%s"""
        c.execute(e5,(str(gbid),))
        ns=[b[0] for b in c.fetchall()]
        con.commit()
        colr="peachpuff"
        final="Booking done by "+cname[0]+"  on "+dateres[0]+"  at "+hrs[0]+" : "+mns[0]+" for "+ns[0]+"  number of seats"
        le=Label(S4,text=final,font=('Times new roman',18,'bold'),bd=8,relief=GROOVE,bg=colr)
        le.place(x=250,y=550,height=75,width=950)
        #con.close()
        
    
def pres():
    S4=Toplevel()
    S4.title("Reservations")
    S4.geometry("1500x1001")
    colr="peachpuff"
    m2=Label(S4,image=my_image6).grid(row=0,column=0)
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    m3=Label(S4,text="Enter business ID: ",font=('Times new roman',24,'bold'),bd=8,relief=GROOVE,bg=colr)
    m3.place(x=350,y=200,height=75,width=475)
    m4=Entry(S4,font=('Times new roman',18,'bold'),bd=8,relief=GROOVE)
    m4.place(x=850,y=200,height=75,width=300)
    m5=Button(S4,text="Check ",font=('Times new roman',24,'bold'),bd=8,relief=GROOVE,bg=colr,command= lambda: chres(S4,m4.get()))
    m5.place(x=700,y=300,height=50,width=150)
    
def todaysres():
    S3=Toplevel()
    S3.title("Reservations")
    S3.geometry("1500x1001")
    colr="darkkhaki"
    now=datetime.now()
    date=now.strftime("%d/%m/%Y")
    m1=Label(S3,image=my_image5).grid(row=0,column=0)
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    w="""select cname from customer where bid in( select bid from reservation where dateofres=%s)"""
    #c=con.cursor()
    c.execute(w,(str(date),))
    namelist=[]
    namelist=[b[0] for b in c.fetchall()]
    con.commit()
    w1="""select no_of_seats from reservation where dateofres=%s """
    #c=con.cursor()
    c.execute(w1,(str(date),))
    seatslist=[]
    seatslist=[b[0] for b in c.fetchall()]
    con.commit()
    w2="""select hours from reservation where dateofres=%s"""
    #c=con.cursor()
    c.execute(w2,(str(date),))
    hlist=[]
    hlist=[b[0] for b in c.fetchall()]
    con.commit()
    w3="""select mins from reservation where dateofres=%s"""
    #c=con.cursor()
    c.execute(w3,(str(date),))
    mlist=[]
    mlist=[b[0] for b in c.fetchall()]
    con.commit()
    w4="""select bid from reservation where dateofres=%s"""
    #c=con.cursor()
    c.execute(w4,(str(date),))
    bidlist=[]
    bidlist=[b[0] for b in c.fetchall()]
    con.commit()
    w5="""select count(*) from reservation where dateofres=%s"""
    #c=con.cursor()
    c.execute(w5,(str(date),))
    num=[b[0] for b in c.fetchall()]
    con.commit()
    if len(mlist)!=len(hlist) or len(hlist)!=len(namelist) :
        messagebox.showerror("Unexpected error","Try again",parent=S3)
        return
    else:
        lm=Label(S3,text="Today's Reservation are:",font=('Times new roman',24,'bold'),bd=8,relief=GROOVE,bg=colr)
        lm.place(x=350,y=200,height=75,width=700)
        for i in range (len(hlist)):
            k=i+1
            txt="Customer  :-  "+namelist[i]+" for "+seatslist[i]+"  seats"+" at "+hlist[i]+" : "+mlist[i]+" pm with business id:- "+bidlist[i]
            
            y1=k*50+300
            lab=Label(S3,text=txt,font=('times new roman',18,'bold'),relief=GROOVE,bg=colr,justify='left')
            lab.place(x=300,y=y1,height=45,width=800)
        
        tt=" Total Number Of Reservations for today  : "
        lmm=Label(S3,text=tt,font=('times new roman',18,'bold'),relief=GROOVE,bg=colr,bd=8)
        lmm.place(x=275,y=750,height=75,width=570)
        n=IntVar()
        n.set(num)
        lmmm=Label(S3,textvariable=n,font=('times new roman',18,'bold'),relief=GROOVE,bg=colr,bd=8)
        lmmm.place(x=875,y=750,height=75,width=100)


    con.commit()
    #con.close()

def openbill(fname):
    new=Toplevel()
    new.title("bill")
    filename=r"C:\Users\USER\Desktop\bills\\"+fname+".txt"
    fileop=open(filename,"r")
    data=fileop.read()
    L=Label(new,text=data,font=('Times new roman',16,'bold'))
    L.grid(row=0,column=0)
    
def chorder(S1,goid):
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    f=""" select order_id from bill"""
    c.execute(f)
    olist=[]
    olist=[b[0] for b in c.fetchall()]
    con.commit()
    if goid not in olist:
        messagebox.showinfo("Not Found","Orders with this order id not found ",parent=S1)
        return
    else:
        f1="""select dateofbill from bill where order_id=%s"""
        c.execute(f1,(str(goid),))
        db=[b[0] for b in c.fetchall()]
        con.commit()
        f2="""select bill_amt from bill where order_id=%s"""
        c.execute(f2,(str(goid),))
        ba=[b[0] for b in c.fetchall()]
        con.commit()
        f3="""select cname from customer where bid in (select bid from food_order where order_id=%s group by bid)"""
        c.execute(f3,(str(goid),))
        cname=[b[0] for b in c.fetchall()]
        con.commit()
        #con.close()
        colr="lightcoral"
        fnn="Order made by "+cname[0]+" on "+db[0]+" with the bill amount  "+ba[0]+" Rs."
        lb=Label(S1,text=fnn,font=('times new roman',18,'bold'),bd=8,relief=GROOVE,bg=colr)
        lb.place(x=100,y=450,height=50,width=750)
        filename=goid+"_"+cname[0]
        m41=Button(S1,text="View Bill",font=('times new roman',16,'bold'),bd=8,relief=GROOVE,bg=colr,command= lambda: openbill(filename))
        m41.place(x=395,y=550,height=75,width=200)
        
        
def prevorder():
    S1=Toplevel()
    S1.title("Search Orders")
    S1.geometry("1000x700")
    colr="lightcoral"
    ml=Label(S1,image=my_image7).grid(row=0,column=0)
    m2=Label(S1,text="Enter Order ID:",font=('times new roman',22,'bold'),bd=8,relief=GROOVE,bg=colr)
    m2.place(x=150,y=200,height=75,width=400)
    m3=Entry(S1,font=('times new roman',18,'bold'),bd=8,relief=GROOVE)
    m3.place(x=675,y=200,height=75,width=150)
    m4=Button(S1,text="Check",font=('times new roman',18,'bold'),bd=8,relief=GROOVE,bg=colr,command= lambda: chorder(S1,m3.get()))
    m4.place(x=495,y=300,height=75,width=100)

    

def prevres():
    S2=Toplevel()
    S2.title("Search Reservation")
    S2.geometry("1500x1001")
    colr="silver"
    mm=Label(S2,image=my_image4).grid(row=0,column=0)
    prb1=Button(S2,text="View Today's Reservation",font=('times new roman',20,'bold'),bd=8,relief=GROOVE,bg=colr,command= todaysres)
    prb1.place(x=500,y=300,height=100,width=450)
    prb2=Button(S2,text="Check Particular Reservation",font=('times new roman',20,'bold'),bd=8,relief=GROOVE,bg=colr,command= pres)
    prb2.place(x=500,y=550,height=100,width=450)
    
    
def feedbk(name,bid,oid):
            feedwindow=Toplevel()
            feedwindow.title("Feedback Page")
            feedwindow.geometry("750x340")
            colr="lightsteelblue"
            my_label= Label(feedwindow,image=my_image2).grid(row=0,column=0)
            welcomestr="Hello..."+" "+name+"!"
            ws=StringVar()
            ws.set(welcomestr)
            lol=Label(feedwindow,textvariable=ws,font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr)
            lol.place(x=250,y=75,height=45,width=250)
            lol1=Label(feedwindow,text="Rate Food on 10:",font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr)
            lol1.place(x=125,y=150,height=30,width=225)
            loll2=Entry(feedwindow,font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr)
            loll2.place(x=400,y=150,height=30,width=225)
            lol3=Label(feedwindow,text="Rate Service on 10:",font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr)
            lol3.place(x=125,y=200,height=30,width=225)
            loll3=Entry(feedwindow,font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr)
            loll3.place(x=400,y=200,height=30,width=225)
            def fdbk(bid,oid,rf,rs):
                    messagebox.showinfo("Submission Success","Thank You!",parent=feedwindow)
                    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
                    #c=con.cursor()
                    fdq1="""insert into feedback (bid,order_id,rate_food,rate_service) values (%s,%s,%s,%s)"""
                    c.execute(fdq1,(str(bid),str(oid),str(rf),str(rs)))
                    con.commit()
                    #con.close()
                
                
                
            but=Button(feedwindow,text="Submit",font=('times new roman',15,'bold'),bd=3,relief=GROOVE,bg=colr,command= lambda: fdbk(bid,oid,loll2.get(),loll3.get()))
            but.place(x=300,y=275,height=30,width=150)
            
               
    
    
def upload(res,lg,cname,pnlist,bid1,bid):
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()   
    mq2="""insert into customer (cname,bid) values (%s,%s)"""
    c.execute(mq2,(str(cname),str(bid)))
    con.commit()
    mq3="""insert into cust_phone (bid,cphone) values (%s,%s)"""
    if len(pnlist)==1:
        cphone1=pnlist[0]
        c.execute(mq3,(str(bid),str(cphone1)))
    if len(pnlist)==2:
        cphone1=pnlist[0]
        c.execute(mq3,(str(bid),str(cphone1)))
        cphone2=pnlist[1]
        c.execute(mq3,(str(bid),str(cphone2)))
    if len(pnlist)==3:
        cphone1=pnlist[0]
        c.execute(mq3,(str(bid),str(cphone1)))
        cphone2=pnlist[1]
        c.execute(mq3,(str(bid),str(cphone2)))
        cphone3=pnlist[2]
        c.execute(mq3,(str(bid),str(cphone3)))
    con.commit()
    #con.close()
    lg["state"]=DISABLED
def res1(res,lg,cname,cphone,bid1,bid):
    gp=cphone
    gpn=str(gp)
    pnlist=[]
    if len(gpn)!=10 and len(gpn)!=21 and len(gpn)!=32:
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn)<10 :
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn) in (11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31):
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn)==10:
        pnlist.append(gpn[0:])
        #print(pnlist)
    if len(gpn)==21:
        pnlist.append(gpn[:10])
        pnlist.append(gpn[11:])
        #print(pnlist)
    if len(gpn)==32:
        pnlist.append(gpn[:10])
        pnlist.append(gpn[11:21])
        pnlist.append(gpn[22:])
        #print(pnlist)
    for i in range (len(pnlist)):
        #print(pnlist[i])
        pass
    msgg=messagebox.askquestion("save details?","Are you sure you want to save deatils?",parent=res)
    if msgg=='yes':
        upload(res,lg,cname,pnlist,bid1,bid)
    else:
        return
    
    
def res2(res,lgg,date,hours,mins,seats,bid):
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    mq4="""select dateofres from reservation"""
    mq5="""select hours from reservation"""
    mq6="""select mins from reservation"""
    c.execute(mq4)
    datelist2=[]
    datelist2=[b[0] for b in c.fetchall()]
    con.commit()
    c.execute(mq5)
    hhlist2=[]
    hhlist2=[b[0] for b in c.fetchall()]
    con.commit()
    c.execute(mq6)
    mmlist2=[]
    mmlist2=[b[0] for b in c.fetchall()]
    con.commit()
    if date in datelist2:
        if hours in hhlist2:
            if mins in mmlist2:
                reslabel1=Label(res,text="Sorry Customer, the time slot selected is not available. Please choose another slot.",bd=5,relief=GROOVE,bg=bg_color1,font=('arial',15,'bold'))
                reslabel1.place(x=100,y=800,height=50,width=1000)
                #con.close()
                return
    mq7="""insert into reservation (bid,dateofres,hours,mins,no_of_seats) values (%s,%s,%s,%s,%s)"""
    c.execute(mq7,(str(bid),str(date),str(hours),str(mins),str(seats)))
    con.commit()
    #con.close()
    msgg2=messagebox.askquestion("Save Deatils?","Reserve tables for given date? ",parent=res)
    if msgg2=='yes':
        lgg["state"]=DISABLED
        reslabel2 =Label(res,text="Your Reservation is SUCCESSFUL! ",font=('Times new roman',15,"bold"),bd=5,relief=GROOVE,bg=bg_color1)
        reslabel2.place(x=100,y=800,height=50,width=1000)
    else:
        return

def check(res,givendate1):
        now=datetime.now()
        yearr=now.strftime("%Y")
        monthh=now.strftime("%m")
        dayy=now.strftime("%d")
        givendate=str(givendate1)
        print(givendate)
        if len(givendate)!=10 and len(givendate)!=8:
            messagebox.showerror("wrong info","please input correct date",parent=res)
        
        if len(givendate)==10:
            date=givendate[:2]
            month=givendate[3:5]
            year=givendate[8:]
            #print(date+month+year)
            if year<yearr[2:]:
                #print("less than 2020")
                messagebox.showerror("wrong info","please check given year",parent=res)
                #print("first msgbox ok")
                
            if year==yearr[:2] and month<monthh:
                #print("2020 but less than dec")
                messagebox.showerror("wrong info","please check given month",parent=res)
                #print("second msgbox ok")
            if month==monthh and date<dayy:
                #print("2020 dec but less than today")
                messagebox.showerror("wrong info","please check given date",parent=res)
                #print("third msgbox ok")
            if date==dayy:
                messagebox.showerror("wrong info","Reservations for today are full",parent=res)
                
        if len(givendate)==8:
           date1=givendate[:2]
           month1=givendate[2:4]
           year1=givendate[6:]
           #print(date1+month1+year1)
           if year1<yearr[2:]:
                #print("less than 2020")
                messagebox.showerror("wrong info","please check given year",parent=res)
                #print("first msgbox ok")
                
           if year1==yearr[:2] and month1<monthh:
                #print("2020 but less than dec")
                messagebox.showerror("wrong info","please check given month",parent=res)
                #print("second msgbox ok")
           if month1==monthh and date1<dayy:
                #print("2020 dec but less than today")
                messagebox.showerror("wrong info","please check given date",parent=res)
                #print("third msgbox ok")
           if date1==dayy:
                messagebox.showerror("wrong info","Reservations for today are full",parent=res)
                
def tableres():
    res = Toplevel()
    res.geometry("1925x1200+0+0")
    res.title("Page-3")
    my_label1= Label(res,image=my_image1).grid(row=0,column=0)
    tt = Label(res,text="Table Reservation ",bd=12,relief=RIDGE,bg=bg_color1,font=('Times new roman',25,"bold"),pady=3)
    tt.place(x=0,y=0,height=75,width=1925)
    
    c1=Label(res,text="Customer name: ",font=('Times new roman',18,"bold"),bg=bg_color1,relief=GROOVE,bd=5)
    c1.place(x=100,y=100,height=50,width=500)
    c2=Entry(res,font=("arial",13),bg="white",relief=GROOVE,)
    c2.place(x=700,y=100,height=50,width=500)

    c3=Label(res,text="Customer Phone: ",font=('Times new roman',18,"bold"),bg=bg_color1,relief=GROOVE,bd=5)
    c3.place(x=100,y=200,height=50,width=500)
    c4=Entry(res,font=("arial",13),bg="white",relief=GROOVE)
    c4.place(x=700,y=200,height=50,width=500)

    c5=Label(res,text="Your Business ID is: ",font=('Times new roman',18,"bold"),bg=bg_color1,relief=GROOVE,bd=5)
    c5.place(x=100,y=400,height=50,width=500)
    bid1=Entry(res,font=('Times new roman',15),bg="white",relief=GROOVE)
    bid1.place(x=700,y=400,height=50,width=500)
    bid=random.randint(100000,900000)
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    mq1="""select bid from customer"""
    c.execute(mq1)
    bidlist=[]
    bidlist=[b[0] for b in c.fetchall()]
    while bid in bidlist:
        bid=random.randint(100000,900000)
    #print(bidlist)
    bid1.insert(0,bid)
    lg=Button(res,text="Save customer details",font=('Times new roman',18,'bold'),bg=bg_color1,bd=5,relief=GROOVE,command= lambda:res1(res,lg,c2.get(),c4.get(),bid1,bid))
    lg.place(x=1200,y=300,height=50,width=500)

    c9=Label(res,text=" Date for Reservation: ",font=('Times new roman',15,"bold"),bg=bg_color1,bd=5,relief=GROOVE)
    c9.place(x=100,y=500,height=50,width=200)

    entrytext1=StringVar()
    entrytext1.set("DD/MM/YYYY")
    ff1=Entry(res,font=('Times new roman',15),bg="white",bd=5,relief=GROOVE,textvariable=entrytext1,justify='center')
    ff1.place(x=350,y=500,height=50,width=150)
       
    bh=Button(res,text="ok",bd=5,font=('Times new roman',15,"bold"),bg=bg_color1,relief=GROOVE,command=lambda: check(res,entrytext1.get()))
    bh.place(x=525,y=500,height=50,width=50)

    c9=Label(res,text="Time for Reservation: ",bd=5,font=('Times new roman',15,"bold"),bg=bg_color1,relief=GROOVE)
    c9.place(x=600,y=500,height=50,width=200)
    entrytext2=StringVar()
    entrytext2.set("HH")
    ff2=OptionMenu(res,entrytext2,"12","01","02","03","04","05","06","07","08","09","10","11")
    ff2.place(x=850,y=500,height=50,width=100)

    lk=Label(res,text="  :  ",font=('Times new roman',13,"bold"),relief=GROOVE,bd=5)
    lk.place(x=960,y=500,height=50,width=30)
    
    entrytext3=StringVar()
    entrytext3.set("MM")
    ff3=OptionMenu(res,entrytext3,"00","15","30","45")
    ff3.place(x=1000,y=500,height=50,width=100)

    ff4=Label(res,text=" pm ",font=('Times new roman',13,"bold"),relief=GROOVE,bd=5)    
    ff4.place(x=1150,y=500,height=50,width=50)
    
    c11=Label(res,text="Enter no. of seats: ",font=('Times new roman',15,"bold"),bg=bg_color1,relief=GROOVE,bd=5)
    c11.place(x=100,y=600,height=50,width=400)
    entrytext5=StringVar()
    entrytext5.set("seats")
    ff5=Entry(res,font=('Times new roman',15),bg="white",relief=GROOVE,textvariable=entrytext5,justify='center',bd=5)
    ff5.place(x=600,y=600,height=50,width=150)

    lgg=Button(res,text="Save reservation details",font=('Times new roman',18,'bold'),bd=5,bg=bg_color1,relief=GROOVE,command= lambda: res2(res,lgg,entrytext1.get(),entrytext2.get(),entrytext3.get(),entrytext5.get(),bid1.get()))
    lgg.place(x=1200,y=700,height=50,width=500)

def upload1(res,lg,cname,pnlist,bid):
    #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
    #c=con.cursor()
    mq11="""insert into customer (cname,bid) values (%s,%s)"""
    c.execute(mq11,(str(cname),str(bid)))
    con.commit()
    
    mqq3="""insert into cust_phone (bid,cphone) values (%s,%s)"""
    if len(pnlist)==1:
        cphone1=pnlist[0]
        c.execute(mqq3,(str(bid),str(cphone1)))
    if len(pnlist)==2:
        cphone1=pnlist[0]
        c.execute(mqq3,(str(bid),str(cphone1)))
        cphone2=pnlist[1]
        c.execute(mqq3,(str(bid),str(cphone2)))
    if len(pnlist)==3:
        cphone1=pnlist[0]
        c.execute(mqq3,(str(bid),str(cphone1)))
        cphone2=pnlist[1]
        c.execute(mqq3,(str(bid),str(cphone2)))
        cphone3=pnlist[2]
        c.execute(mqq3,(str(bid),str(cphone3)))
    con.commit()
    #con.close()
    lg["state"]=DISABLED
def foone(res,lg,cname,cphone,bid):
    gp=cphone
    gpn=str(gp)
    pnlist=[]
    if len(gpn)!=10 and len(gpn)!=21 and len(gpn)!=32:
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn)<10 :
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn) in (11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31):
        messagebox.showerror("wrong details given","please check phone number",parent=res)
        return
    if len(gpn)==10:
        pnlist.append(gpn[0:])
        #print(pnlist)
    if len(gpn)==21:
        pnlist.append(gpn[:10])
        pnlist.append(gpn[11:])
        #print(pnlist)
    if len(gpn)==32:
        pnlist.append(gpn[:10])
        pnlist.append(gpn[11:21])
        pnlist.append(gpn[22:])
        #print(pnlist)
    for i in range (len(pnlist)):
        print(pnlist[i])
    msgg3=messagebox.askquestion("Save Detail?","Are you sure you want to save details?",parent=res)
    if msgg3=='yes':
        upload1(res,lg,cname,pnlist,bid)
    else:
        return
  
def __init__():
            root=Toplevel()
            root.geometry("1925x1200+0+0")
            root.title("Page-2")
            
            itemid=["BIR01","BIR02","BIR03","ST01","ST02","ST03","CU01","CU02","IB01","IB02","DE01","DE02","BE01","BE02"]
            t1 = Label(root,text=" Food Ordering Page ",bd=12,relief=RIDGE,bg=bg_color0,font=('Times new roman',25,"bold"),pady=3).pack(fill=X)
            F1=LabelFrame(root,bd=10,relief=RIDGE,text="Customer Details",font=('arial',13,"underline"),bg=bg_color3)
            F1.place(x=0,y=70,relwidth=5)

            cn=Label(F1,text="Customer name: ",font=('arial',15,"bold"),bg=bg_color0,relief=GROOVE,bd=3)
            cn.grid(row=2,column=0,padx=20,pady=5)
            cne=Entry(F1,font=("arial",13),bg="white",relief=GROOVE,)
            cne.grid(row=2,column=1,padx=10,pady=10)

            cp=Label(F1,text="Customer Phone: ",font=('arial',15,"bold"),bg=bg_color0,relief=GROOVE,bd=3)
            cp.grid(row=2,column=4,padx=20,pady=5)
            cpe=Entry(F1,font=("arial",13),bg="white",relief=GROOVE)
            cpe.grid(row=2,column=5,padx=10,pady=10)

            cp1=Label(F1,text="Your BusinessID is: ",font=('arial',15,"bold"),bg=bg_color0,relief=GROOVE,bd=3)
            cp1.grid(row=2,column=9,padx=20,pady=5)
            cpe1=Entry(F1,font=("arial",13),bg="white",relief=GROOVE)
            cpe1.grid(row=2,column=10,padx=10,pady=10)
            bn=Label(F1,text="Your OrderID is: ",font=('arial',15,"bold"),bg=bg_color0,relief=GROOVE,bd=3)
            bn.grid(row=2,column=13,padx=20,pady=5)
            bne=Entry(F1,font=("arial",15),bg="white",relief=GROOVE)
            bne.grid(row=2,column=14,padx=10,pady=10)

            bid=random.randint(100000,900000)
            #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
            #c=con.cursor()
            mqq1="""select bid from customer"""
            c.execute(mqq1)
            bidlist=[]
            bidlist=[b[0] for b in c.fetchall()]
            while bid in bidlist:
                  bid=random.randint(100000,900000)
            cpe1.insert(0,bid)
            con.commit()
            #con.close()

          
            lg=Button(F1,text="Save customer details",font=('arial',13,'bold'),bg=bg_color0,fg="black",command= lambda: foone(root,lg,cne.get(),cpe.get(),bid))
            lg.grid(row=2,column=7,padx=5,pady=10)
            #........................menu and ordering frame...........................#
            F2=LabelFrame(root,text=" Menu ",bd=10,relief=RIDGE,font=('arial',13,"underline"),bg=bg_color3)
            F2.place(x=0,y=150,height=850,width=550)


            a1=Label(F2,text="Item Number ",font=('arial',12,"underline"),bg=bg_color).grid(row=5,column=0,padx=20,pady=5)
            a2=Label(F2,text="Item Name ",font=('arial',12,"underline"),bg=bg_color).grid(row=5,column=5,padx=20,pady=5)
            a3=Label(F2,text="Item Cost ",font=('arial',12,"underline"),bg=bg_color).grid(row=5,column=10,padx=20,pady=5)
            n1=Label(F2,text="Biryani",font=('arial',15,"bold"),bg=bg_color).grid(row=6,column=5,padx=10,pady=5)
            n2=Label(F2,text="BIR01",font=('arial',15),bg=bg_color).grid(row=7,column=0,padx=10,pady=5)
            o1=Label(F2,text="Veg Supreme biryani",font=('arial',15),bg=bg_color).grid(row=7,column=5,padx=10,pady=5)
            p1=Label(F2,text="180 Rs.",font=('arial',15),bg=bg_color).grid(row=7,column=10,padx=10,pady=5)
            n3=Label(F2,text="BIR02",font=('arial',15),bg=bg_color).grid(row=8,column=0,padx=10,pady=5)
            o2=Label(F2,text="Chicken Biryani",font=('arial',15),bg=bg_color).grid(row=8,column=5,padx=10,pady=5)
            p2=Label(F2,text="210 Rs.",font=('arial',15),bg=bg_color).grid(row=8,column=10,padx=10,pady=5)
            n4=Label(F2,text="BIR03",font=('arial',15),bg=bg_color).grid(row=9,column=0,padx=10,pady=5)
            o3=Label(F2,text="Mutton Biryani",font=('arial',15),bg=bg_color).grid(row=9,column=5,padx=10,pady=5)
            p3=Label(F2,text="250 Rs.",font=('arial',15),bg=bg_color).grid(row=9,column=10,padx=10,pady=5)
            
            n17=Label(F2,text="Starters",font=('arial',15,"bold"),bg=bg_color).grid(row=10,column=5,padx=10,pady=5)
            n5=Label(F2,text="ST01",font=('arial',15),bg=bg_color).grid(row=11,column=0,padx=10,pady=5)
            o4=Label(F2,text="Veg Manchurian",font=('arial',15),bg=bg_color).grid(row=11,column=5,padx=10,pady=5)
            p4=Label(F2,text="150 Rs.",font=('arial',15),bg=bg_color).grid(row=11,column=10,padx=10,pady=5)
            n6=Label(F2,text="ST02",font=('arial',15),bg=bg_color).grid(row=12,column=0,padx=10,pady=5)
            o5=Label(F2,text="Chilli Chicken",font=('arial',15),bg=bg_color).grid(row=12,column=5,padx=10,pady=5)
            p5=Label(F2,text="200 Rs.",font=('arial',15),bg=bg_color).grid(row=12,column=10,padx=10,pady=5)
            n7=Label(F2,text="ST03",font=('arial',15),bg=bg_color).grid(row=13,column=0,padx=10,pady=5)
            o6=Label(F2,text="Mutton Pepper Dry",font=('arial',15),bg=bg_color).grid(row=13,column=5,padx=10,pady=5)
            p6=Label(F2,text="220 Rs.",font=('arial',15),bg=bg_color).grid(row=13,column=10,padx=10,pady=5)

            
            n18=Label(F2,text="Curry",font=('arial',15,"bold"),bg=bg_color).grid(row=14,column=5,padx=10,pady=5)
            n8=Label(F2,text="CU01",font=('arial',15),bg=bg_color).grid(row=15,column=0,padx=10,pady=5)
            o7=Label(F2,text="Butter panner",font=('arial',15),bg=bg_color).grid(row=15,column=5,padx=10,pady=5)
            p7=Label(F2,text="170 Rs.",font=('arial',15),bg=bg_color).grid(row=15,column=10,padx=10,pady=5)
            n9=Label(F2,text="CU02",font=('arial',15),bg=bg_color).grid(row=16,column=0,padx=10,pady=5)
            o8=Label(F2,text="Butter Chicken",font=('arial',15),bg=bg_color).grid(row=16,column=5,padx=10,pady=5)
            p8=Label(F2,text="200 Rs.",font=('arial',15),bg=bg_color).grid(row=16,column=10,padx=10,pady=5)
            
            n19=Label(F2,text="Indian Bread",font=('arial',15,"bold"),bg=bg_color).grid(row=17,column=5,padx=10,pady=5)
            n10=Label(F2,text="IB01",font=('arial',15),bg=bg_color).grid(row=18,column=0,padx=10,pady=5)
            o9=Label(F2,text="Tandoori Roti-2pc",font=('arial',15),bg=bg_color).grid(row=18,column=5,padx=10,pady=5)
            p9=Label(F2,text="60 Rs.",font=('arial',15),bg=bg_color).grid(row=18,column=10,padx=10,pady=5)
            n11=Label(F2,text="IB02",font=('arial',15),bg=bg_color).grid(row=19,column=0,padx=20,pady=5)
            o10=Label(F2,text="Rumali Roti-2pc",font=('arial',15),bg=bg_color).grid(row=19,column=5,padx=10,pady=5)
            p10=Label(F2,text="60 Rs.",font=('arial',15),bg=bg_color).grid(row=19,column=10,padx=10,pady=5)
            
            n20=Label(F2,text="Desserts",font=('arial',15,"bold"),bg=bg_color).grid(row=20,column=5,padx=10,pady=5)
            n12=Label(F2,text="DE01",font=('arial',15),bg=bg_color).grid(row=21,column=0,padx=10,pady=5)
            o11=Label(F2,text="Rasmalai-1pc",font=('arial',15),bg=bg_color).grid(row=21,column=5,padx=10,pady=5)
            p11=Label(F2,text="50 Rs.",font=('arial',15),bg=bg_color).grid(row=21,column=10,padx=10,pady=5)
            n13=Label(F2,text="DE02",font=('arial',15),bg=bg_color).grid(row=22,column=0,padx=10,pady=5)
            o12=Label(F2,text="Jamoon-1pc",font=('arial',15),bg=bg_color).grid(row=22,column=5,padx=10,pady=5)
            p12=Label(F2,text="50 Rs.",font=('arial',15),bg=bg_color).grid(row=22,column=10,padx=10,pady=5)
            
            n21=Label(F2,text="Beverages",font=('arial',15,"bold"),bg=bg_color).grid(row=23,column=5,padx=10,pady=5)
            n14=Label(F2,text="BE01",font=('arial',15),bg=bg_color).grid(row=24,column=0,padx=10,pady=5)
            o13=Label(F2,text="Mineral Water-500ml",font=('arial',15),bg=bg_color).grid(row=24,column=5,padx=10,pady=5)
            p13=Label(F2,text="30 Rs.",font=('arial',15),bg=bg_color).grid(row=24,column=10,padx=10,pady=5)
            n15=Label(F2,text="BE02",font=('arial',15),bg=bg_color).grid(row=25,column=0,padx=10,pady=5)
            o14=Label(F2,text="Coke-500ml",font=('arial',15),bg=bg_color).grid(row=25,column=5,padx=10,pady=5)
            p14=Label(F2,text="30 Rs.",font=('arial',15),bg=bg_color).grid(row=25,column=10,padx=10,pady=5)
                        #...............ordering frame......#

            F3=LabelFrame(root,text=" Order Here ",bd=10,relief=RIDGE,font=('arial',13,"underline"),bg=bg_color3)
            F3.place(x=555,y=150,height=850,width=750)
            or1=Label(F3,text="Item Name ",font=('arial',14,"underline"),bg=bg_color).grid(row=5,column=5,padx=20,pady=5)
            dummy1=Label(F3,bg=bg_color).grid(row=5,column=10,padx=20,pady=5)
            or2=Label(F3,text="Quantity ",font=('arial',14,"underline"),bg=bg_color).grid(row=5,column=15,padx=20,pady=5)
            or3=Label(F3,text="Cost ",font=('arial',14,"underline"),bg=bg_color).grid(row=5,column=25,padx=20,pady=5)
            oid=random.randint(10000,90000)
            q1="""select order_id from  food_order"""
            #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
            #c=con.cursor()
    
            c.execute(q1)
            oidlist=[]
            oidlist=[b[0] for b in c.fetchall()]
            while oid in oidlist:
                 oid=random.randint(10000,90000)

            con.commit()
            bne.insert(0,oid)
            #con.close()

            #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
            #c=con.cursor()
            
            
            def fb1(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[0]
                cost=int(q)*180
                cost1=IntVar()
                cost1.set(cost)
                or444=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or444.grid(row=7,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb1["state"]=DISABLED

            or4=Label(F3,text="Veg Supreme biryani",font=('arial',15),bg=bg_color).grid(row=7,column=5,padx=10,pady=5)
            bir1=StringVar()
            bir1.set("0")
            or44=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=bir1,justify='center')
            or44.grid(row=7,column=15,padx=10,pady=5)
            orb1=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb1(bir1.get()))
            orb1.grid(row=7,column=20,padx=5,pady=5)
            

            def fb2(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[1]
                cost=int(q)*210
                cost1=IntVar()
                cost1.set(cost)
                or555=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or555.grid(row=8,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb2["state"]=DISABLED
            or5=Label(F3,text="Chicken Biryani",font=('arial',15),bg=bg_color).grid(row=8,column=5,padx=10,pady=5)
            bir2=StringVar()
            bir2.set("0")
            or55=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=bir2,justify='center')
            or55.grid(row=8,column=15,padx=10,pady=5)
            orb2=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb2(bir2.get()))
            orb2.grid(row=8,column=20,padx=5,pady=5)

            def fb3(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[2]
                cost=int(q)*250
                cost1=IntVar()
                cost1.set(cost)
                or666=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or666.grid(row=9,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb3["state"]=DISABLED
            or6=Label(F3,text="Mutton Biryani",font=('arial',15),bg=bg_color).grid(row=9,column=5,padx=10,pady=5)
            bir3=StringVar()
            bir3.set("0")
            or66=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=bir3,justify='center')
            or66.grid(row=9,column=15,padx=10,pady=5)
            orb3=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb3(bir3.get()))
            orb3.grid(row=9,column=20,padx=5,pady=5)

            dummyx1=Label(F3,bg=bg_color).grid(row=10,column=5)
            
            def fb4(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[3]
                cost=int(q)*150
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=11,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb4["state"]=DISABLED
            or7=Label(F3,text="Veg Manchurian",font=('arial',15),bg=bg_color).grid(row=11,column=5,padx=10,pady=5)
            st1=StringVar()
            st1.set("0")
            or77=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=st1,justify='center')
            or77.grid(row=11,column=15,padx=10,pady=5)
            orb4=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb4(st1.get()))
            orb4.grid(row=11,column=20,padx=5,pady=5)
            


            def fb5(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[4]
                cost=int(q)*200
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=12,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb5["state"]=DISABLED
            or8=Label(F3,text="Chilli Chicken",font=('arial',15),bg=bg_color).grid(row=12,column=5,padx=10,pady=5)
            st2=StringVar()
            st2.set("0")
            or88=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=st2,justify='center')
            or88.grid(row=12,column=15,padx=10,pady=5)
            orb5=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb5(st2.get()))
            orb5.grid(row=12,column=20,padx=5,pady=5)


            def fb6(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[5]
                cost=int(q)*220
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=13,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb6["state"]=DISABLED
            or9=Label(F3,text="Mutton Pepper Dry",font=('arial',15),bg=bg_color).grid(row=13,column=5,padx=10,pady=5)
            st3=StringVar()
            st3.set("0")
            or77=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=st3,justify='center')
            or77.grid(row=13,column=15,padx=10,pady=5)
            orb6=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb6(st3.get()))
            orb6.grid(row=13,column=20,padx=5,pady=5)

            dummyx2=Label(F3,bg=bg_color).grid(row=14,column=5)

            def fb7(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[6]
                cost=int(q)*170
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=15,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb7["state"]=DISABLED
            or10=Label(F3,text="Butter panner",font=('arial',15),bg=bg_color).grid(row=15,column=5,padx=10,pady=5)
            cu1=StringVar()
            cu1.set("0")
            or100=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=cu1,justify='center')
            or100.grid(row=15,column=15,padx=10,pady=5)
            orb7=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb7(cu1.get()))
            orb7.grid(row=15,column=20,padx=5,pady=5)
            


            def fb8(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[7]
                cost=int(q)*200
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=16,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb8["state"]=DISABLED
            or11=Label(F3,text="Butter Chicken",font=('arial',15),bg=bg_color).grid(row=16,column=5,padx=10,pady=5)
            cu2=StringVar()
            cu2.set("0")
            or101=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=cu2,justify='center')
            or101.grid(row=16,column=15,padx=10,pady=5)
            orb8=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb8(cu2.get()))
            orb8.grid(row=16,column=20,padx=5,pady=5)

            dummyx3=Label(F3,bg=bg_color).grid(row=17,column=5)
            




            def fb9(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[8]
                cost=int(q)*60
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=18,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb9["state"]=DISABLED
            or12=Label(F3,text="Tandoori Roti-2pc",font=('arial',15),bg=bg_color).grid(row=18,column=5,padx=10,pady=5)
            ib1=StringVar()
            ib1.set("0")
            or102=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=ib1,justify='center')
            or102.grid(row=18,column=15,padx=10,pady=5)
            orb9=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb9(ib1.get()))
            orb9.grid(row=18,column=20,padx=5,pady=5)


            def fb10(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[9]
                cost=int(q)*60
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=19,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb10["state"]=DISABLED
            or13=Label(F3,text="Rumali Roti-2pc",font=('arial',15),bg=bg_color).grid(row=19,column=5,padx=10,pady=5)
            ib2=StringVar()
            ib2.set("0")
            or103=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=ib2,justify='center')
            or103.grid(row=19,column=15,padx=10,pady=5)
            orb10=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb10(ib2.get()))
            orb10.grid(row=19,column=20,padx=5,pady=5)

            dummyx4=Label(F3,bg=bg_color).grid(row=20,column=5)


            def fb11(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[10]
                cost=int(q)*50
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=21,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb11["state"]=DISABLED
            or14=Label(F3,text="Rasmalai-1pc",font=('arial',15),bg=bg_color).grid(row=21,column=5,padx=10,pady=5)
            de1=StringVar()
            de1.set("0")
            or104=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=de1,justify='center')
            or104.grid(row=21,column=15,padx=10,pady=5)
            orb11=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb11(de1.get()))
            orb11.grid(row=21,column=20,padx=5,pady=5)



            def fb12(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[11]
                cost=int(q)*50
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=22,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb12["state"]=DISABLED
            or15=Label(F3,text="Jamoon-1pc",font=('arial',15),bg=bg_color).grid(row=22,column=5,padx=10,pady=5)
            de2=StringVar()
            de2.set("0")
            or105=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=de2,justify='center')
            or105.grid(row=22,column=15,padx=10,pady=5)
            orb12=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb12(de2.get()))
            orb12.grid(row=22,column=20,padx=5,pady=5)

            dummyx5=Label(F3,bg=bg_color).grid(row=23,column=5)



            def fb13(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[12]
                cost=int(q)*30
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=24,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb13["state"]=DISABLED
            or16=Label(F3,text="Mineral Water-500ml",font=('arial',15),bg=bg_color).grid(row=24,column=5,padx=10,pady=5)
            be1=StringVar()
            be1.set("0")
            or106=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=be1,justify='center')
            or106.grid(row=24,column=15,padx=10,pady=5)
            orb13=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb13(be1.get()))
            orb13.grid(row=24,column=20,padx=5,pady=5)



            def fb14(q):
                bid=cpe1.get()
                oid=bne.get()
                iid=itemid[13]
                cost=int(q)*30
                cost1=IntVar()
                cost1.set(cost)
                or777=Entry(F3,textvariable=cost1,font=("arial",13),bg=bg_color,relief=GROOVE,justify='center')
                or777.grid(row=25,column=25,padx=20,pady=5)
                sq1="""insert into food_order (bid,order_id,item_id,quantity,cost) values (%s,%s,%s,%s,%s)"""
                c.execute(sq1,(str(bid),str(oid),str(iid),str(q),str(cost1.get())))
                con.commit()
                orb14["state"]=DISABLED
            or17=Label(F3,text="Coke-500ml",font=('arial',15),bg=bg_color).grid(row=25,column=5,padx=10,pady=5)
            be2=StringVar()
            be2.set("0")
            or107=Entry(F3,font=("arial",13),bg="white",relief=GROOVE,textvariable=be2,justify='center')
            or107.grid(row=25,column=15,padx=10,pady=5)
            orb14=Button(F3,text="select",font=('arial',8,'bold'),relief=RIDGE,command= lambda:fb14(be2.get()))
            orb14.grid(row=25,column=20,padx=5,pady=5)



            def fotwo(orb15):
                  msgg4=messagebox.askquestion("Proceed Further?","Confirm order?",parent=F3)
                  if msgg4=='yes':
                          bid=cpe1.get()
                          oid=bne.get()
                          datebill=date.today()
                          sq2="""insert into bill (bid,order_id,dateofbill) values (%s,%s,%s)"""
                          c.execute(sq2,(str(bid),str(oid),str(datebill)))
                          con.commit()

                          sq3="""select sum(o.cost) from food_order o, bill b where o.bid=b.bid and o.order_id=b.order_id and o.bid= %s and o.order_id=%s"""
                          c.execute(sq3,(str(bid),str(oid),))
                          billamt2=0.0
                          billamt=0
                          billamt=c.fetchall()
                          for i in billamt:
                              billamt2=i[0]
                          con.commit()

                          sq4="""update bill set bill_amt = %s where order_id= %s and bid=%s"""
                          c.execute(sq4,(str(billamt2),str(oid),str(bid),))
                          con.commit()
                          #con.close()
                          orb15["state"]=DISABLED
                  else:
                      return


            def fothree(orb16):
                orb16["state"]=DISABLED
                
                wlcmbill()


    
            orb15=Button(F3,text="Place Order ",relief=RIDGE,font=("arial",12,'bold'),command= lambda: fotwo(orb15))
            orb15.grid(row=33,column=5,padx=20,pady=5)
            dummy1=Label(F3,bg=bg_color).grid(row=28,column=5,padx=10,pady=5)

            dummy1=Label(F3,bg=bg_color).grid(row=36,column=5,padx=10,pady=5)
            orb16=Button(F3,text="Generate bill ",relief=RIDGE,font=("arial",12,'bold'),command= lambda: fothree(orb16))
            orb16.grid(row=33,column=25,padx=20,pady=5)

            

            #................billing frame...................#
            F4=LabelFrame(root,text="Your Bill Here",font=('arial',13,"underline"),bd=10,relief=RIDGE,bg=bg_color3)
            F4.place(x=1310,y=150,height=850,width=610) 
            def wlcmbill():
                txtarea=Text(F4,relief=RIDGE,font=('Times new roman',15,'bold'),height=750,width=600)
                txtarea.config(state="normal")
                name=cne.get()
                oid=bne.get()
                phone=cpe.get()
                now=datetime.now()
                date=now.strftime("%d")
                monthh=now.strftime("%m")
                yearr=now.strftime("%Y")
                datee=date+'-'+monthh+'-'+yearr
                timee=now.strftime("%H:%M:%S")
                
                
                bid=cpe1.get()
                #con=mysql.connector.connect(host="localhost",user="root",password="heyitsme139",database="demo")
                #c=con.cursor()
                #gives name for bill
                qq1="""select item_name from menu where item_id in(select item_id from food_order where bid=%s and order_id=%s)"""
                c.execute(qq1,(str(bid),str(oid)))
                itemname=[item[0] for item in c.fetchall()]
                #print(itemname)
                con.commit()
                # givves quantity for bill
                qq2="""select quantity from food_order where bid=%s and order_id= %s"""
                c.execute(qq2,(str(bid),str(oid)))
                itemq=[item[0] for item in c.fetchall()]
                #print(itemq)
                con.commit()
                #gives cost for bill
                qq3="""select cost from food_order where bid=%s and order_id= %s"""
                c.execute(qq3,(str(bid),str(oid)))
                itemc=[item[0] for item in c.fetchall()]
                #print(itemc)
                con.commit()

                #gives final bill
                qq4="""select bill_amt from bill where bid=%s and order_id= %s"""
                c.execute(qq4,(str(bid),str(oid)))
                billamt2=0.0
                billamt=0
                billamt=c.fetchall()
                for i in billamt:
                    billamt2=i[0]
                #print(billamt2)
                con.commit()
                txtarea.delete('1.0',END)
                txtarea.insert(END,"=======================================================\n")
                txtarea.insert(END,"\t\t\tYOUR BILL \t\t\t\n")
                txtarea.insert(END,"=======================================================\n")
                txtarea.insert(END,f"Name: {name} \n")
                txtarea.insert(END,f"Phone: {phone}\n")
                txtarea.insert(END,f"Date: {datee} \n")
                txtarea.insert(END,f"Time: {timee} \n")
                txtarea.insert(END,f"Order id: {oid}\n ")
                txtarea.insert(END,"=====================================================\n")
                txtarea.insert(END,"\t Items\t\t   Quantity\t\t Price\t \n")
                txtarea.insert(END,"=======================================================\n")
                

                if len(itemname)==len(itemq)==len(itemc):
                    m=len(itemc)
                    final=billamt2
                    for i in range(m):
                        k=i+1
                        nnn=itemname[i]
                        qqq=itemq[i]
                        ccc=itemc[i]
                        txtarea.insert(END,f"{k}. {nnn}\t\t\t  ....{qqq}\t.... {ccc}\t\n ")
                        
                    txtarea.insert(END,"=======================================================\n")
                    txtarea.insert(END,f"TOTAL AMOUNT : {final} \n")
                    txtarea.insert(END,"=======================================================\n")
                    txtarea.insert(END,"\t\t\tTHANK YOU \n")
                    txtarea.insert(END,"=======================================================\n")
                        
                txtarea.config(state="disabled")
                txtarea.grid(row=0,column=0)
                msgg6=messagebox.askquestion("Save Bill?","Do You Want to Save bill?",parent=F4)
                if msgg6=='yes':
                    fname1=str(oid)+"_"+str(name)
                    fname=r"C:\Users\USER\Desktop\bills\\"+fname1
                    billdata=txtarea.get('1.0',END)
                    f1=open(fname+".txt","w")
                    f1.write(billdata)
                    f1.close()
                else:
                    pass
                feedbk(name,bid,oid)
                             
            
window=Tk()#main page
window.geometry("1925x1200+0+0")
window.title("Page-1")
bg_color0="tan"
bg_color="bisque"
bg_color3="bisque"
bg_color1="tan"
my_image= ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\mainpage.png"))
my_label= Label(window,image=my_image).grid(row=0,column=0)
my_image1= ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\respage.png"))
my_image2= ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\fdbkk.png"))
my_image4=ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\newres.png"))
my_image5=ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\newres2.png"))
my_image6=ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\newres1.png"))
my_image7=ImageTk.PhotoImage(Image.open(r"C:\Users\Ramanand\PycharmProjects\dbmsproject\finallsearchorder1000x700.png"))

LL=Label(window,text=" Hotel  Namma Mane ",bd=15,fg='black',bg='burlywood',font=('Times new roman',35,'underline'),padx=800,pady=50,relief=GROOVE)
LL.place(x=500,y=300,height=120,width=900)

LL1=Label(window,text="Address: #32/A,6th main,Rajajinagar 2nd block,Bangalore-79 \n Email: htellen27@gmail.com \n Timings: 12pm - 11pm ",relief=GROOVE,fg='black',bg='burlywood',font=('Times new roman',16),padx=800,pady=50,bd=5)
LL1.place(x=500,y=430,height=85,width=900)

buttonlg=Button(window,fg='black',bg='wheat',bd=12,text='Order food',font=('Times new roman',25),padx=400,pady=25,relief=RIDGE,command=__init__)
buttonlg.place(x=200,y=625,height=100,width=500)

buttonlg1=Button(window,fg='black',bg='wheat',bd=12,text='Reserve tables',font=('Times new roman',25),padx=400,pady=25,relief=RIDGE,command=tableres)
buttonlg1.place(x=1200,y=625,height=100,width=500)

buttonlg2=Button(window,fg='black',bg='wheat',bd=12,text='Search Orders',font=('Times new roman',25),padx=400,pady=25,relief=RIDGE,command= prevorder)
buttonlg2.place(x=200,y=750,height=100,width=500)

buttonlg3=Button(window,fg='black',bg='wheat',bd=12,text='Search Reservations',font=('Times new roman',25),padx=400,pady=25,relief=RIDGE,command=prevres)
buttonlg3.place(x=1200,y=750,height=100,width=500)

window.mainloop()

