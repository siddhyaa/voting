from tkinter import *
import mysql.connector as my
from tkinter import messagebox
import random
import string
import smtplib



def vote():
    global b1,b2,b3,b4,b5,mw2
    mw2 = Tk()
    mw2.geometry("300x300")
    mw2.configure(bg="red")
    b1 = Button(mw2, text="Shiv Sena",bg="orange",command=shivw)
    b1.place(x=200, y=40)
    b2 = Button(mw2, text="BJP",bg="light blue",command=bjpW)
    b2.place(x=200, y=90)
    b3 = Button(mw2, text="Congress",command=congw)
    b3.place(x=200, y=140)
    b4 = Button(mw2, text="Rastrvadi",command=rastrw)
    b4.place(x=200, y=190)
    b5 = Button(mw2, text="Manse",command=manw)
    b5.place(x=200, y=240)
    mw2.mainloop()

def registr():
    try:
        conn=my.connect(host="localhost",user="root",password="root",database="voter")
        cur=conn.cursor()
        q="select vid from register"
        cur.execute(q)
        r=cur.fetchall()
        na=e1.get()
        cn=int(e2.get())
        en=e3.get()
        vi=int(e4.get())
        for i in r:
                if i[0]==e4.get():
                    messagebox.showerror("error","already voter ID register")
                    break
        else:

                if na!="" and cn!="" and en!="" and vi!="":
                    if len(str(cn))==10:
                        if len(str(vi))==8:

                                q="insert into register values(%s,%s,%s,%s,%s)"
                                sc=random.randint(1000000001,9999999999)
                                v=(na,cn,en,vi,sc)
                                cur.execute(q,v)
                                conn.commit()
                                conn.close()
                        else:
                            messagebox.showerror("Error","Check Voter id Length")
                    else:
                        messagebox.showerror("Error","Check Contact Length")
                else:
                    messagebox.showerror("Error","Please Fill Details")
    except ValueError:
        messagebox.showerror("Error","Enter only number")
        mw1.destroy()


def reg():
    global e1,e2,e3,e4,mw1
    mw1 = Tk()
    mw1.geometry("400x300")
    Label(mw1, text="Full Name").place(x=10, y=50)
    e1 = Entry(mw1, width=25)
    e1.place(x=140, y=50)
    Label(mw1, text="Contact No").place(x=10, y=80)
    e2 = Entry(mw1, width=20)
    e2.place(x=140, y=80)
    Label(mw1, text="Email").place(x=10, y=110)
    e3 = Entry(mw1, width=20)
    e3.place(x=140, y=110)
    Label(mw1,text="Voter ID").place(x=10,y=140)
    e4=Entry(mw1,width=20)
    e4.place(x=140,y=140)
    mb4 = Button(mw1, text="Register",command=registr)
    mb4.place(x=120, y=210)
    mw1.mainloop()


def capv():
    global v
    v=random.choices(string.ascii_uppercase+string.digits,k=5)
    v="".join(v)
    capl.config(text=v)

def log():
    try:
        conn = my.connect(host="localhost", user="root", password="root", database="voter")
        cur = conn.cursor()
        q = "select vid,scode from register"
        cur.execute(q)
        r = cur.fetchall()
        q1="select * from vote"
        cur.execute(q1)
        r1=cur.fetchall()
        for j in r1:
            if ecn.get()==j[0]:
                messagebox.showerror("error","already vote")
                break
        else:
                vi = int(ecn.get())
                sc = int(ecp.get())
                cpv = cp.get()
                for i in r:

                        if int(i[0])==vi and int(i[1])==sc and cpv==v:
                            messagebox.showinfo("congo", "login sucessfull")
                            vote()
                            break
                else:
                    messagebox.showerror("error", "wrong details")
    except ValueError:
        messagebox.showerror("error","enter only numbers")
        mw.destroy()

def bjpW():
    conn = my.connect(user="root", password="root", host="localhost", database="voter")
    cur = conn.cursor()
    q="select cbjp from cvote"
    cur.execute(q)
    r=cur.fetchone()
    cn=int(r[0]+1)
    v1=(cn,r[0])
    q="update cvote set cbjp=%s where cbjp=%s "
    cur.execute(q,v1)

    q1="insert into vote value(%s)"%ecn.get()
    cur.execute(q1)
    conn.commit()
    conn.close()
    mw2.destroy()

def shivw():
    conn = my.connect(user="root", password="root", host="localhost", database="voter")
    cur = conn.cursor()
    q="select cshiv from cvote"
    cur.execute(q)
    r=cur.fetchone()
    cut=r[0]+1
    v=(cut,r[0])
    q="update cvote set cshiv=%s where cshiv=%s "
    cur.execute(q,v)

    q1="insert into vote value(%s)"%ecn.get()
    cur.execute(q1)
    conn.commit()
    conn.close()
    mw2.destroy()

def congw():
    conn = my.connect(user="root", password="root", host="localhost", database="voter")
    cur = conn.cursor()
    q="select ccong from cvote"
    cur.execute(q)
    r=cur.fetchone()
    cnt=r[0]+1
    v=(cnt,r[0])
    q="update cvote set ccong=%s where ccong=%s "
    cur.execute(q,v)

    q1="insert into vote value(%s)"%ecn.get()
    cur.execute(q1)
    conn.commit()
    conn.close()
    mw2.destroy()

def rastrw():
    conn = my.connect(user="root", password="root", host="localhost", database="voter")
    cur = conn.cursor()
    q="select crastr from cvote"
    cur.execute(q)
    r=cur.fetchone()
    cnt=r[0]+1
    v=(cnt,r[0])
    q="update cvote set crastr=%s where crastr=%s "
    cur.execute(q,v)

    q1="insert into vote value(%s)"%ecn.get()
    cur.execute(q1)
    conn.commit()
    conn.close()
    mw2.destroy()

def manw():
    conn = my.connect(user="root", password="root", host="localhost", database="voter")
    cur = conn.cursor()
    q="select cmanse from cvote"
    cur.execute(q)
    r=cur.fetchone()
    cnt=r[0]+1
    v=(cnt,r[0])
    q="update cvote set cmanse=%s where cmanse=%s "
    cur.execute(q,v)

    q1="insert into vote value(%s)"%ecn.get()
    cur.execute(q1)
    conn.commit()
    conn.close()
    mw2.destroy()

global ecn,ecp,cp,mw
mw = Tk()
mw.geometry("300x400")
Label(mw, text="Enter Voter ID").place(x=10, y=50)
ecn = Entry(mw, width=20)
ecn.place(x=140, y=50)
Label(mw, text="Security Code").place(x=10, y=80)
ecp = Entry(mw, width=20)
ecp.place(x=140, y=80)
Label(mw, text="Enter Capture").place(x=10, y=110)
cp = Entry(mw, width=15)
cp.place(x=140, y=110)
capl=Label(mw,text="Cptcha")
capl.place(x=10,y=200)
mb1 = Button(mw, text="Login",command=log)
mb1.place(x=70, y=150)
mb2 = Button(mw, text="Registration",command=reg)
mb2.place(x=150, y=150)
mb3 = Button(mw, text="Retry",command=capv)
mb3.place(x=110, y=200)
mw.mainloop()