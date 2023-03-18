from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox

class sweet_hours:
    cartlist=[]
    amount=0

#--  main page 1------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass
        

        sf.scr.geometry("1366x768")
        sf.scr.title("wellcome to the world of sweet")
        
        sf.scr.iconbitmap('icon.ico')
        sf.main_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.png")
        sf.Label=Label(sf.main_frame1,image=sf.logo)
        sf.Label.place(x=0,y=0)
        sf.main_frame1.pack(fill=BOTH,expand=1)

        sf.main_frame2=Frame(sf.scr,height=668,width=1366)
        sf.canvas=Canvas(sf.main_frame2,height=610,width=1366)
        sf.canvas.pack()
        sf.back=PhotoImage(file="2.png")
        sf.canvas.create_image(683,284,image=sf.back)
        sf.lab_button=Button(sf.main_frame2,text= "WELCOME to \n the World of HAPPINESS",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
        sf.lab_button.place(x=410,y=200)
        sf.main_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ login page 2------
    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')
        
        sf.login_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")

        sf.label=Label(sf.login_frame1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.login_frame1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=1050,y=65)

        sf.about_button=Button(sf.login_frame1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.about_button.config(command=lambda:sf.about())
        sf.about_button.place(x=1180,y=65)
        sf.login_frame1.pack(fill=BOTH,expand=1)

        sf.login_frame2=Frame(sf.scr,height=668,width=1366)
        sf.canvas=Canvas(sf.login_frame2,height=618,width=1366)
        sf.canvas.pack()

        sf.logo1=PhotoImage(file="10.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
       
        sf.login=Label(sf.login_frame2,text="LOGIN",fg="beige",bg="saddlebrown",width=20,font=("cooper black",27))
        sf.login.place(x=450,y=120)

        sf.user_label=Label(sf.login_frame2,text="UserName",bg="burlywood",font=("cooper black",22))
        sf.user_label.place(x=400,y=220)

        sf.user_entry=Entry(sf.login_frame2,bg="bisque",font=("cooper black",22),bd=6 ,justify='left')
        sf.user_entry.place(x=600,y=220)

        sf.pasw_label=Label(sf.login_frame2,text="Password",bg="burlywood",font=("cooper black",22))
        sf.pasw_label.place(x=400,y=290)

        sf.pasd_entry=Entry(sf.login_frame2,bg="bisque",font=("cooper black",22),bd=6 ,justify='left')
        sf.pasd_entry.place(x=600,y=290)

        sf.log_button=Button(sf.login_frame2,text="Login",cursor="hand2",command=lambda:sf.login_database(),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.log_button.place(x=400,y=350)

        def clear(sf):
            sf.user_entry.delete(0,END)
            sf.pasd_entry.delete(0,END)
        sf.clear=Button(sf.login_frame2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.clear.place(x=850,y=350)
        sf.regis=Button(sf.login_frame2,text="New Entry",command=lambda:sf.Register(),fg="black",cursor="hand2",bg="burlywood",font=("cooper black",25),bd=8)
        sf.regis.place(x=570,y=420)
        
        sf.login_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser=sf.user_entry.get()
        sf.logpass=sf.pasd_entry.get()
        return sf.loguser,sf.logpass

    def about(sf):
        sf.scr1=Tk()
        sf.L=Label(sf.scr1,text="NEW BAKERY SHOP")
        sf.L.pack()
        sf.scr1.mainloop()


#--  login database page 3------
    def login_database(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("sweet.db")
        sf.cursor=sf.con.cursor()
        try:
            sf.cursor.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cursor.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        #print()
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome to the sweet hours")            
            sf.delivery()

 #_________register page 4________________           


        
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')
        
        sf.reg_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.label=Label(sf.reg_frame1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home_button=Button(sf.reg_frame1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.home_button.place(x=1050,y=65)
        
        sf.abt_button=Button(sf.reg_frame1,text="About Us",command=lambda:sf.about(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.abt_button.place(x=1180,y=65)
        
        sf.reg_frame1.pack(fill=BOTH,expand=1)
        
        sf.reg_frame2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.reg_frame2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="24.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
       
        sf.log=Label(sf.reg_frame2,text="REGISTRATION       FORM",bg="saddlebrown",fg="beige",width=20,font=("cooper black",32))
        sf.log.place(x=150,y=50)

        sf.lab1=Label(sf.reg_frame2,text="FirstName",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab1.place(x=170,y=180)

        sf.first=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.first.place(x=420,y=180)

        sf.lab2=Label(sf.reg_frame2,text="LastName",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab2.place(x=170,y=230)

        sf.last=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.last.place(x=420,y=230)

        sf.lab3=Label(sf.reg_frame2,text="Username",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab3.place(x=170,y=280)

        sf.usern=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.usern.place(x=420,y=280)

        sf.lab4=Label(sf.reg_frame2,text="Password",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab4.place(x=170,y=330)

        sf.passd=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.passd.place(x=420,y=330)

        sf.lab5=Label(sf.reg_frame2,text="Email",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab5.place(x=170,y=380)

        sf.email=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.email.place(x=420,y=380)

        sf.lab6=Label(sf.reg_frame2,text="Mobile No.",bg="burlywood",font=("cooper black",20),fg="black")
        sf.lab6.place(x=170,y=430)

        sf.mob_no=Entry(sf.reg_frame2,bg="bisque",width=15,font=("cooper black",20),bd=5)
        sf.mob_no.place(x=420,y=430)

        sf.back=Button(sf.reg_frame2,text="Back",cursor="hand2",command=lambda:sf.login(),fg="black",bg="burlywood",font=("cooper black",20),bd=7)
        sf.back.place(x=170,y=500)

        sf.register=Button(sf.reg_frame2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Reg_database(),font=("cooper black",20),bd=7)
        sf.register.place(x=350,y=500)

        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob_no.delete(0,END)
       
        sf.clear_button=Button(sf.reg_frame2,text="Clear",cursor="hand2",fg="black",bg="burlywood",command=lambda:clear(sf),font=("cooper black",20),bd=7)
        sf.clear_button.place(x=570,y=500)
        sf.reg_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob_no=sf.mob_no.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob_no

    
#_________register database page 5_________   

    def Reg_database(sf):
        sf.credreg=sf.resultreg()
        sf.con=connect("sweet.db")
        sf.cursor=sf.con.cursor()
        try:
            sf.cursor.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
            
        except:
            pass
        x=sf.cursor.execute("select count(*) from customer where username=%r and mob=%r "%(sf.credreg[0],sf.credreg[5]))
        #print(x)
        if list(x)[0][0]==0:
            if sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                sf.cursor.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2],sf.credreg[3],sf.credreg[4],sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")


#dated--> 6sep
#----menulist page 6------

            
    def menulist(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.menu_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.label=Label(sf.menu_frame1,image=sf.logo,height=150).place(x=0,y=0)
        sf.menu_frame1.pack(fill=BOTH,expand=1)
        
        
        sf.menu_frame2=Frame(sf.scr,height=668,width=1366)
        sf.canvas=Canvas(sf.menu_frame2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)

        

        sf.home_button=Button(sf.menu_frame1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home_button.place(x=1100,y=60)
        
        
        sandwich=PhotoImage(file="s1.png")
        sf.sand_but=Button(sf.menu_frame2,image=sandwich,cursor="hand2",fg="black",command=lambda:sf.sandwich(sf.x))
        sf.sand_but.place(x=300,y=40)

        
        jarcake=PhotoImage(file="s2.png")
        sf.jar_but=Button(sf.menu_frame2,image=jarcake,cursor="hand2",fg="black",command=lambda:sf.jarcake(sf.x))
        sf.jar_but.place(x=300,y=140)

        pastry=PhotoImage(file="s3.png")
        sf.pastry_but=Button(sf.menu_frame2,image=pastry,cursor="hand2",fg="black",command=lambda:sf.pastry(sf.x))
        sf.pastry_but.place(x=300,y=240)


        pizza=PhotoImage(file="s4.png")
        sf.pizza_but=Button(sf.menu_frame2,image=pizza,cursor="hand2",fg="black",command=lambda:sf.pizza(sf.x))
        sf.pizza_but.place(x=300,y=340)

        
        coffee=PhotoImage(file="s5.png")
        sf.coffee_but=Button(sf.menu_frame2,image=coffee,cursor="hand2",fg="black",command=lambda:sf.coffee(sf.x))
        sf.coffee_but.place(x=300,y=440)

       
        sf.menu_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#-- --delivery page 7------


    def delivery(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')


        sf.deliv_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.label=Label(sf.deliv_f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.deliv_f1.pack(fill=BOTH,expand=1)
        
        sf.deliv_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.deliv_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak2.png")
        sf.canvas.create_image(683,309,image=sf.logo1)

        sf.out=Button(sf.deliv_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16))
        sf.out.place(x=1100,y=60)
        
        sf.deli=PhotoImage(file="del1.png")
        sf.canvas.create_image(370,270,image=sf.deli)
        
        sf.delivery=Button(sf.deliv_f2,text="DELIVERY",cursor="hand2",fg="white",command=lambda:sf.menulist("deli"),bg="#0b1335",font=("default",16),bd=3)
        sf.delivery.place(x=150,y=270)
        
        sf.deliv_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------- sandwich page 8------


    def sandwich(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.sandwich_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.sandwich_f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.sandwich_f1.pack(fill=BOTH,expand=1)
        
        
        sf.sandwich_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.sandwich_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        
        
        sf.home=Button(sf.sandwich_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)

        sf.canvas.create_text(1150,180,text="SANDWICH",fill="lightsalmon",font=("broadway",35))
        
        sf.canvas.create_rectangle(400, 40, 966, 540,fill="black",outline="black",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # cheese sandwich 1

        sf.canvas.create_rectangle(405, 50, 960, 170,width=2,fill="lightsalmon")
        sf.cheese=PhotoImage(file="cheese.png")
        sf.canvas.create_image(470,110,image=sf.cheese)
        sf.canvas.create_text(690,80,text="CHEESE SANDWICH",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,90,text="₹100",fill="black",font=("default",19,'bold'))
        
        sf.canvas.create_text(600,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.sandwich_f2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=650,y=140)

        sf.add1=Button(sf.sandwich_f2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=880,y=120)

        sf.v1=IntVar()
        def addch1():
            if sf.v1.get()==10:
                ch1="Medium"
               
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
               
                pric1=650
            else:
                ch1="Regular"
                
                pric1=100
            sf.addlist(["Cheese",ch1,sf.q1.get(),pric1*int(sf.q1.get())])

            #veg sandwich 2
        sf.canvas.create_rectangle(405, 170, 960, 290,width=2,fill="lightsalmon")
        sf.vag=PhotoImage(file="vegsand.png")
        sf.canvas.create_image(470,230,image=sf.vag)
        sf.canvas.create_text(670,200,text="VEG SANDWICH",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,210,text="₹80",fill="black",font=("default",17,'bold'))
       
        sf.canvas.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.sandwich_f2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=650,y=260)

        sf.add2=Button(sf.sandwich_f2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=880,y=240)
        sf.v2=IntVar()
        def addch2():
            
            if sf.v1.get()==10:
                ch2="Medium"
               
                pric2=450
            elif sf.v1.get()==20:
                ch2="Large"
               
                pric2=650
            else:
                ch2="Regular"
                
                pric2=100
           
            sf.addlist(["Veg Sandwich",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
        #grill sandwich 3

        sf.canvas.create_rectangle(405, 290, 960, 410,width=2,fill="lightsalmon")
        sf.grill=PhotoImage(file="grill.png")
        sf.canvas.create_image(470,350,image=sf.grill)
        sf.canvas.create_text(680,320,text="GRILL SANDWICH",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,330,text="₹85",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.sandwich_f2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=650,y=380)

        sf.add3=Button(sf.sandwich_f2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=880,y=360)

        sf.v3=IntVar()
        def addch3():
            if sf.v1.get()==10:
                ch3="Medium"
               
                pric3=450
            elif sf.v1.get()==20:
                ch3="Large"
               
                pric3=650
            else:
                ch3="Regular"
                
                pric3=85
            
            sf.addlist(["grill sandwich ",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #overload sandwich 4
        sf.canvas.create_rectangle(405, 410, 960, 530,width=2,fill="lightsalmon")
        sf.load=PhotoImage(file="overload.png")
        sf.canvas.create_image(470,470,image=sf.load)
        sf.canvas.create_text(670,440,text="VEG OVERLOAD",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,450,text="₹90",fill="black",font=("default",17,'bold'))
        
        sf.v4=IntVar()
        
        
        sf.canvas.create_text(590,510,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.sandwich_f2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=650,y=500)
        
        sf.add4=Button(sf.sandwich_f2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=880,y=480)
        def addch4():
            if sf.v1.get()==10:
                ch4="Medium"
               
                pric4=450
            elif sf.v1.get()==20:
                ch4="Large"
               
                pric4=650
            else:
                ch4="Regular"
                
                pric4=90
           
            sf.addlist(["veg overload  ",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con_order=Button(sf.sandwich_f2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con_order.place(x=1050,y=250)
        sf.more_button=Button(sf.sandwich_f2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more_button.place(x=1050,y=350)
        sf.sandwich_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()


    ############################
    
        
#-----jarcake page 9------
    def jarcake(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.jar_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.jar_frame1,image=sf.logo,height=150).place(x=0,y=0)
       
        sf.jar_frame1.pack(fill=BOTH,expand=1)
        
        
        sf.jar_frame2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.jar_frame2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        
        
        sf.home=Button(sf.jar_frame1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)
        
        sf.canvas.create_text(1150,180,text="JAR CAKE",fill="lightsalmon",font=("broadway",35))                                                                        
        
        sf.canvas.create_rectangle(400, 40, 966, 540,fill="black",outline="black",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # OREO JARCAKE

        sf.canvas.create_rectangle(405, 50, 960, 170,width=2,fill="lightsalmon")
        sf.oreo=PhotoImage(file="j3.png")
        sf.canvas.create_image(470,110,image=sf.oreo)
        sf.canvas.create_text(625,80,text="OREO CAKE",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,90,text="₹110",fill="black",font=("default",19,'bold'))
        
        sf.canvas.create_text(600,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.jar_frame2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=650,y=140)
        sf.add1=Button(sf.jar_frame2,text="ADD",command=lambda:addch5(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=880,y=120)

        sf.v1=IntVar()
        def addch5():
            if sf.v1.get()==10:
                ch1="Medium"
               
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
               
                pric1=650
            else:
                ch1="Regular"
                
                pric1=110
            sf.addlist(["Oreo",ch1,sf.q1.get(),pric1*int(sf.q1.get())])

            #RED VELVET
        sf.canvas.create_rectangle(405, 170, 960, 290,width=2,fill="lightsalmon")
        sf.velvet=PhotoImage(file="t1.png")
        sf.canvas.create_image(470,230,image=sf.velvet)
        sf.canvas.create_text(635,200,text="RED VELVET",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,210,text="₹100",fill="black",font=("default",17,'bold'))
       
        sf.canvas.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.jar_frame2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=650,y=260)
        sf.add2=Button(sf.jar_frame2,text="ADD",command=lambda:addch6(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=880,y=240)

        sf.v2=IntVar()
        def addch6():
            if sf.v1.get()==10:
                ch2="Medium"
               
                pric2=450
            elif sf.v1.get()==20:
                ch2="Large"
               
                pric2=650
            else:
                ch2="Regular"
                
                pric2=100
           
            sf.addlist(["Red Velvet",ch2,sf.q2.get(),pric2*int(sf.q2.get())])

        #MUD CAKE

        sf.canvas.create_rectangle(405, 290, 960, 410,width=2,fill="lightsalmon")
        sf.mud=PhotoImage(file="j4.png")
        sf.canvas.create_image(470,350,image=sf.mud)
        sf.canvas.create_text(620,320,text="MUD CAKE",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,330,text="₹120",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.jar_frame2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=650,y=380)

        sf.add3=Button(sf.jar_frame2,text="ADD",command=lambda:addch7(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=880,y=360)

        sf.v3=IntVar()
         
        def addch7():
            if sf.v1.get()==10:
                ch3="Medium"
               
                pric3=450
            elif sf.v1.get()==20:
                ch3="Large"
               
                pric3=650
            else:
                ch3="Regular"
                
                pric3=120
            sf.addlist(["Mud Cake",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #PINEAPPLE
        sf.canvas.create_rectangle(405, 410, 960, 530,width=2,fill="lightsalmon")
        sf.pine=PhotoImage(file="j5.png")
        sf.canvas.create_image(470,470,image=sf.pine)
        sf.canvas.create_text(660,440,text="PINEAPPLE JAR",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,450,text="₹90",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,510,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.jar_frame2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=650,y=500)
        
        sf.add4=Button(sf.jar_frame2,text="ADD",command=lambda:addch8(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=880,y=480)

        sf.v4=IntVar()
        def addch8():
            if sf.v1.get()==10:
                ch4="Medium"
               
                pric4=450
            elif sf.v1.get()==20:
                ch4="Large"
               
                pric4=650
            else:
                ch4="Regular"
                
                pric4=90
            sf.addlist(["   Pineapple",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.jar_frame2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.jar_frame2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.jar_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    

#-------pastry  page 10------


    def pastry(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.pastry_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.pastry_f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.pastry_f1.pack(fill=BOTH,expand=1)

        sf.pastry_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.pastry_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        sf.home=Button(sf.pastry_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)
   
        sf.canvas.create_text(1150,180,text="PASTRY",fill="lightsalmon",font=("broadway",35))
        
        sf.canvas.create_rectangle(400, 40, 966, 540,fill="black",outline="black",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # BUTTER SCOTCH

        sf.canvas.create_rectangle(405, 50, 960, 170,width=2,fill="lightsalmon")
        sf.butter=PhotoImage(file="p1.png")
        sf.canvas.create_image(470,110,image=sf.butter)
        sf.canvas.create_text(665,80,text="BUTTER SCOTCH",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,90,text="₹60",fill="black",font=("default",19,'bold'))
        
        sf.canvas.create_text(600,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.pastry_f2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=650,y=140)
        sf.add1=Button(sf.pastry_f2,text="ADD",command=lambda:addch9(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=880,y=120)

        sf.v1=IntVar()
        def addch9():
            if sf.v1.get()==10:
                ch1="Medium"
               
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
               
                pric1=650
            else:
                ch1="Regular"
                
                pric1=60
            sf.addlist(["Butter Scotch",ch1,sf.q1.get(),pric1*int(sf.q1.get())])

            #CREAM SANDWICH
        sf.canvas.create_rectangle(405, 170, 960, 290,width=2,fill="lightsalmon")
        sf.cream=PhotoImage(file="p2.png")
        sf.canvas.create_image(470,230,image=sf.cream)
        sf.canvas.create_text(680,200,text="CREAM SANDWICH",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,210,text="₹80",fill="black",font=("default",17,'bold'))

        sf.canvas.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.pastry_f2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=650,y=260)
        sf.add2=Button(sf.pastry_f2,text="ADD",command=lambda:addch10(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=880,y=240)

        sf.v2=IntVar()
        def addch10():
            if sf.v1.get()==10:
                ch2="Medium"
               
                pric2=450
            elif sf.v1.get()==20:
                ch2="Large"
               
                pric2=650
            else:
                ch2="Regular"
                
                pric2=80
            sf.addlist(["Cream Sandwich",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
        #CARAMEL

        sf.canvas.create_rectangle(405, 290, 960, 410,width=2,fill="lightsalmon")
        sf.caramel=PhotoImage(file="p3.png")
        sf.canvas.create_image(470,350,image=sf.caramel)
        sf.canvas.create_text(615,320,text="CARAMEL",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,330,text="₹70",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.pastry_f2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=650,y=380)

        sf.add3=Button(sf.pastry_f2,text="ADD",command=lambda:addch11(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=880,y=360)

        sf.v3=IntVar()
        
        def addch11():
            if sf.v1.get()==10:
                ch3="Medium"
               
                pric3=450
            elif sf.v1.get()==20:
                ch3="Large"
               
                pric3=650
            else:
                ch3="Regular"
                
                pric3=70
            sf.addlist(["Caramel",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #DOUBLE CHOCO
        sf.canvas.create_rectangle(405, 410, 960, 530,width=2,fill="lightsalmon")
        sf.choco=PhotoImage(file="p4.png")
        sf.canvas.create_image(470,470,image=sf.choco)
        sf.canvas.create_text(655,440,text="DOUBLE CHOCO",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,450,text="₹95",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,510,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.pastry_f2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=650,y=500)
        
        sf.add4=Button(sf.pastry_f2,text="ADD",command=lambda:addch12(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=880,y=480)

        sf.v4=IntVar()
        def addch12():
            if sf.v1.get()==10:
                ch4="Medium"
               
                pric4=450
            elif sf.v1.get()==20:
                ch4="Large"
               
                pric4=650
            else:
                ch4="Regular"
                
                pric4=95
           
            sf.addlist(["Double Choco",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.pastry_f2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.pastry_f2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.pastry_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

        
#--------pizza  page 11------


    def pizza(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.pizza_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.pizza_f1,image=sf.logo,height=150).place(x=0,y=0)
       
        sf.pizza_f1.pack(fill=BOTH,expand=1)
        
        
        sf.pizza_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.pizza_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        sf.home=Button(sf.pizza_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)

        sf.canvas.create_text(1150,180,text="VEG PIZZA",fill="lightsalmon",font=("broadway",35))

        sf.canvas.create_rectangle(400, 40, 966, 540,fill="black",outline="black",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # pizza 1
        sf.canvas.create_rectangle(405, 50, 960, 170,width=2,fill="lightsalmon")
        sf.delux=PhotoImage(file="piz1.png")
        sf.canvas.create_image(470,110,image=sf.delux)
        sf.canvas.create_text(640,80,text="Deluxe Veggie",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(870,80,text="₹450/650/250",fill="#000000",font=("default",17,'bold'))
        
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.pizza_f2,text = "Medium",value=10,variable=sf.v1,bg="salmon")
        sf.C11.place(x=550,y=110)
        sf.C12 = Radiobutton(sf.pizza_f2, text = "Large",value = 20, variable =sf.v1,bg="salmon")
        sf.C12.place(x=640,y=110)
        sf.C13 = Radiobutton(sf.pizza_f2, text = "Regular",value = 30, variable =sf.v1,bg="salmon")
        sf.C13.place(x=710,y=110)
        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()
        sf.canvas.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.pizza_f2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=650,y=140)
        sf.add1=Button(sf.pizza_f2,text="ADD",command=lambda:addch13(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=850,y=120)
        def addch13():
            if sf.v1.get()==10:
                ch1="Medium"
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
                pric1=650
            else:
                ch1="Regular"
                pric1=250
            sf.addlist(["Deluxe Veggie",ch1,sf.q1.get(),pric1*int(sf.q1.get())])
            
        #pizza 2
        sf.canvas.create_rectangle(405, 170, 960, 290,width=2,fill="lightsalmon")
        sf.vag=PhotoImage(file="piz4.png")
        sf.canvas.create_image(470,230,image=sf.vag)
        sf.canvas.create_text(630,200,text="Veg Vaganza",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(870,200,text="₹400/600/250",fill="#000000",font=("default",17,'bold'))

        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.pizza_f2,text = "Medium",value=10,variable=sf.v2,bg="salmon")
        sf.C21.place(x=550,y=230)
        sf.C22 = Radiobutton(sf.pizza_f2, text = "Large",value = 20, variable =sf.v2,bg="salmon")
        sf.C22.place(x=640,y=230)
        sf.C23 = Radiobutton(sf.pizza_f2, text = "Regular",value = 30, variable =sf.v2,bg="salmon")
        sf.C23.place(x=710,y=230)
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()
        sf.canvas.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.pizza_f2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=650,y=260)
        sf.add2=Button(sf.pizza_f2,text="ADD",command=lambda:addch14(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=850,y=240)
        def addch14():
            if sf.v2.get()==10:
                ch2="Medium"
                pric2=400
            elif sf.v2.get()==20:
                ch2="Large"
                pric2=600
            else:
                ch2="Regular"
                pric2=250

            sf.addlist(["Veg Vaganza",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
        #pizza 3
        sf.canvas.create_rectangle(405, 290, 960, 410,width=2,fill="lightsalmon")
        sf.pep=PhotoImage(file="piz3.png")
        sf.canvas.create_image(470,350,image=sf.pep)
        sf.canvas.create_text(610,320,text="5 Pepper",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(870,320,text="₹385/550/225",fill="#000000",font=("default",17,'bold'))
        
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.pizza_f2,text = "Medium",value=10,variable=sf.v3,bg="salmon")
        sf.C31.place(x=550,y=350)
        sf.C32 = Radiobutton(sf.pizza_f2, text = "Large",value = 20, variable =sf.v3,bg="salmon")
        sf.C32.place(x=640,y=350)
        sf.C33 = Radiobutton(sf.pizza_f2, text = "Regular",value = 30, variable =sf.v3,bg="salmon")
        sf.C33.place(x=710,y=350)
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.canvas.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.pizza_f2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=650,y=380)

        sf.add3=Button(sf.pizza_f2,text="ADD",command=lambda:addch15(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=850,y=360)
        def addch15():
            if sf.v3.get()==10:
                ch3="Medium"
                pric3=385
            elif sf.v3.get()==20:
                ch3="Large"
                pric3=550
            else:
                ch3="Regular"
                pric3=225
            sf.addlist(["5 Pepper     ",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #pizza 4
        sf.canvas.create_rectangle(405, 410, 960, 530,width=2,fill="lightsalmon")
        sf.mag=PhotoImage(file="piz2.png")
        sf.canvas.create_image(470,470,image=sf.mag)
        sf.canvas.create_text(620,440,text="Margherita",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(870,440,text="₹195/385/99",fill="#000000",font=("default",17,'bold'))
        
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.pizza_f2,text = "Medium",value=10,variable=sf.v4,bg="salmon")
        sf.C41.place(x=550,y=470)
        sf.C42 = Radiobutton(sf.pizza_f2, text = "Large",value = 20, variable =sf.v4,bg="salmon")
        sf.C42.place(x=640,y=470)
        sf.C43 = Radiobutton(sf.pizza_f2, text = "Regular",value = 30, variable =sf.v4,bg="salmon")
        sf.C43.place(x=710,y=470)
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()
        
        sf.canvas.create_text(590,510,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.pizza_f2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=650,y=500)
        
        sf.add4=Button(sf.pizza_f2,text="ADD",command=lambda:addch16(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=850,y=480)
        def addch16():
            if sf.v4.get()==10:
                ch4="Medium"
                pric4=195
            elif sf.v4.get()==20:
                ch4="Large"
                pric4=385
            else:
                ch4="Regular"
                pric4=99
            sf.addlist(["Margherita  ",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.pizza_f2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.pizza_f2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.pizza_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
        

#-----------coffee page 12-------------------

    def coffee(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.coffee_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.coffee_f1,image=sf.logo,height=150).place(x=0,y=0)
       
        sf.coffee_f1.pack(fill=BOTH,expand=1)
        
        sf.coffee_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.coffee_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="bak3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        sf.home=Button(sf.coffee_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)

        sf.canvas.create_text(1150,180,text="COFFEE",fill="lightsalmon",font=("broadway",35))
        
        sf.canvas.create_rectangle(400, 40, 966, 540,fill="black",outline="black",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # CHARCOAL LATTE

        sf.canvas.create_rectangle(405, 50, 960, 170,width=2,fill="lightsalmon")
        sf.charcoal=PhotoImage(file="cof1.png")
        sf.canvas.create_image(470,110,image=sf.charcoal)
        sf.canvas.create_text(675,80,text="CHARCOAL LATTE",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,90,text="₹100",fill="black",font=("default",19,'bold'))
        
        sf.canvas.create_text(600,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.coffee_f2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=650,y=140)
        sf.add1=Button(sf.coffee_f2,text="ADD",command=lambda:addch17(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=880,y=120)

        sf.v1=IntVar()
        def addch17():
            if sf.v1.get()==10:
                ch1="Medium"
               
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
               
                pric1=650
            else:
                ch1="Regular"
                
                pric1=100
            sf.addlist(["Charcoal Latte",ch1,sf.q1.get(),pric1*int(sf.q1.get())])

            #ESPRESSO
        sf.canvas.create_rectangle(405, 170, 960, 290,width=2,fill="lightsalmon")
        sf.espresso=PhotoImage(file="cof5.png")
        sf.canvas.create_image(470,230,image=sf.espresso)
        sf.canvas.create_text(620,200,text="ESPRESSO",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,210,text="₹70",fill="black",font=("default",17,'bold'))

        sf.canvas.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.coffee_f2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=650,y=260)
        sf.add2=Button(sf.coffee_f2,text="ADD",command=lambda:addch18(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=880,y=240)

        sf.v2=IntVar()
        def addch18():
            if sf.v1.get()==10:
                ch2="Medium"
               
                pric2=450
            elif sf.v1.get()==20:
                ch2="Large"
               
                pric2=650
            else:
                ch2="Regular"
                
                pric2=70
           
            sf.addlist(["Eepresso",ch2,sf.q2.get(),pric2*int(sf.q2.get())])

        #MOCHA GREEN

        sf.canvas.create_rectangle(405, 290, 960, 410,width=2,fill="lightsalmon")
        sf.mocha=PhotoImage(file="cof4.png")
        sf.canvas.create_image(470,350,image=sf.mocha)
        sf.canvas.create_text(655,320,text="MOCHA GREEN",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,330,text="₹110",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.coffee_f2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=650,y=380)

        sf.add3=Button(sf.coffee_f2,text="ADD",command=lambda:addch19(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=880,y=360)

        sf.v3=IntVar()
        def addch19():
            if sf.v1.get()==10:
                ch3="Medium"
               
                pric3=450
            elif sf.v1.get()==20:
                ch2="Large"
               
                pric3=650
            else:
                ch3="Regular"
                
                pric3=110
            sf.addlist(["Mocha Green",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #CAPPUCCINO
        sf.canvas.create_rectangle(405, 410, 960, 530,width=2,fill="lightsalmon")
        sf.capp=PhotoImage(file="cof6.png")
        sf.canvas.create_image(470,470,image=sf.capp)
        sf.canvas.create_text(645,440,text="CAPPUCCINO",fill="#000000",font=("Cooper Black",20))
        sf.canvas.create_text(900,450,text="₹85",fill="black",font=("default",17,'bold'))
        
        sf.canvas.create_text(590,510,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.coffee_f2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=650,y=500)
        
        sf.add4=Button(sf.coffee_f2,text="ADD",command=lambda:addch20(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=880,y=480)

        sf.v4=IntVar()
        def addch20():
            if sf.v1.get()==10:
                ch4="Medium"
               
                pric4=450
            elif sf.v1.get()==20:
                ch4="Large"
               
                pric4=650
            else:
                ch4="Regular"
                
                pric4=85
           
            sf.addlist(["Cappuccino ",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.coffee_f2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.coffee_f2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.coffee_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()




    def addlist(sf,q):
        if q[-2]!="0" and q[-2].isdigit():
            sf.cartlist.append(q)
            sf.amount=sf.amount+q[-1]
            messagebox.showinfo("Cart","Item Successfully added")
        else:
            messagebox.showinfo("Cart","Enter Valid Quantity to add")
        print(sf.cartlist,sf.amount)

#------address page 13------
    def Address(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.add_frame1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.label=Label(sf.add_frame1,image=sf.logo,height=150).place(x=0,y=0)
       
        sf.add_frame1.pack(fill=BOTH,expand=1)
        
        
        sf.add_frame2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.add_frame2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="a3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
       
        
        sf.out=Button(sf.add_frame1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16))
        sf.out.place(x=1100,y=60)
        
       

        sf.log=Label(sf.add_frame2,text="ADDRESS",bg="saddlebrown",width=20,fg="beige",font=("default",27, 'bold'))
        sf.log.place(x=795,y=50)

       
        sf.lab1=Label(sf.add_frame2,text="City",bg="peru",font=("cooper black",18))
        sf.lab1.place(x=780,y=150)

        sf.city=Entry(sf.add_frame2,bg="bisque",width=15,font=("default",18),bd=5)
        sf.city.place(x=1030,y=150)

        sf.lab2=Label(sf.add_frame2,text="Locality",bg="peru",font=("cooper black",18))
        sf.lab2.place(x=780,y=200)

        sf.local=Entry(sf.add_frame2,bg="bisque",width=15,font=("default",18),bd=5)
        sf.local.place(x=1030,y=200)

        sf.lab3=Label(sf.add_frame2,text="Building Name",bg="peru",font=("cooper black",18))
        sf.lab3.place(x=780,y=250)

        sf.build=Entry(sf.add_frame2,bg="bisque",width=15,font=("default",18),bd=5)
        sf.build.place(x=1030,y=250)

        sf.lab4=Label(sf.add_frame2,text="House No.",bg="peru",font=("cooper black",18))
        sf.lab4.place(x=780,y=300)

        sf.house=Entry(sf.add_frame2,bg="bisque",width=15,font=("default",18),bd=5)
        sf.house.place(x=1030,y=300)

        sf.lab5=Label(sf.add_frame2,text="Landmark",bg="peru",font=("cooper black",18))
        sf.lab5.place(x=780,y=350)

        sf.land=Entry(sf.add_frame2,bg="bisque",width=15,font=("default",18),bd=7)
        sf.land.place(x=1030,y=350)

        sf.back_button=Button(sf.add_frame2,text="Back",command=lambda:sf.Orderde(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.back_button.place(x=800,y=450)

        sf.order_button=Button(sf.add_frame2,text="Order Now",command=lambda:sf.thankyou(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.order_button.place(x=950,y=450)

        def clear(sf):
            sf.city.delete(0,END)
            sf.local.delete(0,END)
            sf.build.delete(0,END)
            sf.house.delete(0,END)
            sf.land.delete(0,END)
        sf.clear_butt=Button(sf.add_frame2,text="Clear",command=lambda:clear(sf),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.clear_butt.place(x=1150,y=450)
        sf.add_frame2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

        
#-----order page 14------

    def Orderde(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.order_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.order_f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.order_f1.pack(fill=BOTH,expand=1)
        
        sf.order_f2=Frame(sf.scr,height=618,width=1366)
        sf.canvas=Canvas(sf.order_f2,height=618,width=1366)
        sf.canvas.pack()
        sf.logo1=PhotoImage(file="a3.png")
        sf.canvas.create_image(683,309,image=sf.logo1)
        
        sf.home=Button(sf.order_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1100,y=60)
        
        sf.log_order=Label(sf.order_f2,text="YOUR ORDER",bg="saddlebrown",fg="beige",width=18,font=("Cooper Black",22,'bold'))
        sf.log_order.place(x=880,y=26)

        sf.canvas.create_rectangle(1300, 90, 850, 500,fill="burlywood",outline="black",width=6)
        sf.amt=sf.amount

        sf.text="Total : "+str(sf.amt)
        sf.tot=Label(sf.order_f2,text=sf.text,bg="#f2da9d",width=12,font=("Cooper Black",22,'bold'))
        sf.tot.place(x=950,y=510)

        if sf.x=="deli":
            sf.y=sf.Address
        if sf.x=="pick":
            sf.y=sf.orderpay
        sf.pay=Button(sf.order_f2,text="Pay",command=lambda:sf.y(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pay.place(x=660,y=390)
        sf.add_button=Button(sf.order_f2,text="Add more",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.add_button.place(x=660,y=450)
        sf.canvas.create_text(1080,105,text="Items\tSize\tQty\tPrice",font=("cooper black",18))
        sf.canvas.create_text(1075,115,text="_____________________________________",font=("cooper black",18))
        y=100
        for i in sf.cartlist:
            y+=45
            s=i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+str(i[3])
            
            sf.canvas.create_text(1060,y,text=s,font=("default",17))
            
            
        sf.order_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

 #------------last page 15------------


    def thankyou(sf,x):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("wellcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap('icon.ico')

        sf.last_f1=Frame(sf.scr,height=100,width=1366)
        sf.logo=PhotoImage(file="1.PNG")
        sf.ba=Label(sf.last_f1,image=sf.logo,height=150).place(x=0,y=0)
       
        sf.last_f1.pack(fill=BOTH,expand=1)
        
        sf.last_f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.last_f2,height=618,width=1366)
        sf.c.pack()

        sf.logo1=PhotoImage(file="last.png")
        sf.c.create_image(683,309,image=sf.logo1)
        
        sf.out=Button(sf.last_f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",font=("default",18))
        sf.out.place(x=1150,y=60)

        sf.last_f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    

    
    
x=sweet_hours()
x.main()
