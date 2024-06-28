from tkinter import *
from tkinter import ttk
from tkinter import messagebox
loggeduser=""
loggedname=""
def gotocpage():
    global root
    root.destroy()
    cabbook()
def validate():
    global userEntered
    global passEntered
    global root
    global loggeduser
    global loggedname
    flag=True
    usr=userEntered.get()
    pwd=passEntered.get()
    f=open("users.txt",'r')
    users=list(f)
    f.close()
    for i in users:
        uname,passw,name,email,secq,secan=i.split('|')
        if usr==uname and pwd==passw:
            root.destroy()
            loggeduser=usr
            loggedname=name
            cabbook()
            return
    messagebox.showerror("Error", "Invalid Id or password")
def RegisterNow():
    global userEntered
    global passEntered
    global nameEntered
    global emailEntered
    global root
    global user
    global securityanswer
    global var
    usr=userEntered.get()
    pwd=passEntered.get()
    name=nameEntered.get()
    email=emailEntered.get()
    secans=securityanswer.get()
    seques=var.get()
    if secans!="" and seques!="" and email!="" and usr!="" and pwd!="" and name!="": 
                if '@' in email and '.com' in email: 
                    flag=0
                    f=open("users.txt",'r')
                    users=list(f)
                    f.close()
                    for i in users:
                        if usr in i or email in i:
                           messagebox.showerror("Validatation Error", "Username/Email Already Exists")
                           flag=1
                    if flag==0:
                        f=open("users.txt",'a')
                        f.write(usr+'|'+pwd+'|'+name+'|'+email+'|'+seques+'|'+secans+'\n')
                        f.close()
                        messagebox.showinfo("Registration Successful", "Registration success! You Can Now Login")
                else:
                    messagebox.showerror("Validatation Error", "Invalid Email Address")
    else:
        messagebox.showerror("Invalid Entry", "Empty Entries given")
def RegisterPage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    global var
    global nameEntered
    global emailEntered
    global securityanswer
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background2.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(1178,178,890,554,fill="#5D478B",outline="white")
    canvas.create_text(600,50,text="REGISTRATION",fill='black',font=("Arial",50,'bold'))
    canvas.create_text(1035,210,text="Register",fill='white',font=("Arial",20,'bold'))
    canvas.create_text(937,270,text="Username:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(937,305,text="Your Name",fill='white',font=("Arial",13,'bold'))
    nameEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    emailEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_text(937,340,text="Password:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(937,450,text="Answer:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(937,375,text="Email:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(950,405,text="Security Question:",fill='white',font=("Arial",10,'bold'))
    bullet = "\u2022"
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show=bullet)
    canvas.create_window(1080,305,window=nameEntered)
    var = StringVar(root)
    var.set("What was your childhood nickname?")
    secmenu=  ttk.Combobox(root, width=20,height=20,textvariable=var)
    secmenu['values'] =["What was your childhood nickname?","What is your favorite movie?","What was the make and model of your first car?","What school did you attend for sixth grade?"]
    secmenu['state'] = 'readonly'
    securityanswer=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_window(1080,450,window=securityanswer)
    canvas.create_window(1080,375,window=emailEntered)
    canvas.create_window(1100,405,window=secmenu)
    canvas.create_window(1080,270,window=userEntered)
    canvas.create_window(1080,340,window=passEntered)
    Regbutton=Button(canvas,text="<< BACK",width=10,fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(965,500,window=Regbutton)
    Loginbutton=Button(canvas,text="REGISTER >>",fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=RegisterNow)
    canvas.create_window(1105,500,window=Loginbutton)

    
def forgotpass():
    global userEntered
    global passEntered
    global securityanswer
    global var
    global root
    global user
    usr=userEntered.get()
    pwd=passEntered.get()
    seciq=var.get()
    secians=securityanswer.get()
    if secians!="" and seciq!="" and usr!="" and pwd!="":
        flag=0
        f=open("users.txt",'r')
        users=list(f)
        f.close()
        for i in range(len(users)):
            uname,passw,nme,email,secq,secan=users[i].split('|')
            if usr==uname and secq.upper()==seciq.upper() and secan.upper().rstrip()==secians.upper():
                users[i]=uname+'|'+pwd+'|'+nme+'|'+email+'|'+secq+'|'+secan
                flag=1
        if flag:
             f=open("users.txt",'w')
             for i in users:
                 f.write(i)
             f.close()
             messagebox.showinfo("Successfull", "Password Reset Success ")
        else:
             messagebox.showerror("Error", "Invalid username or Security Question")
    else:
         messagebox.showerror("Error", "Empty Enrties")

def submitreview():
    global var
    global feedEntry
    global canvas
    global loggeduser
    review=feedEntry.get("1.0",'end-1c')
    with open('reviews.txt','a') as f:
        f.write(loggeduser+'|'+str(var.get())+'|'+review+'\n')
        messagebox.showinfo("Successfull", "Review Successfully submitted")
def feedpage():
    global root
    global canvas
    global gifimg
    global var
    global feedEntry
    canvas.delete('all')
    gifimg=PhotoImage(file="background6.gif")
    canvas.create_image(0,0,image=gifimg,anchor=NW)
    canvas.create_rectangle(30,105,545,490,fill="black")
    rebutton=Button(canvas,text="<< Back to Booking Page",width=25,fg="yellow",bg="black",bd=4,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(1170,30,window=rebutton)
    ebutton=Button(canvas,text="Give Review",width=15,fg="black",bg="yellow",font=("Arial",13,'bold'),command=submitreview)
    canvas.create_window(460,470,window=ebutton)
    canvas.create_text(250,170,text="Feedback" ,fill="yellow",font=("Arial",25,'underline'))
    canvas.create_text(70,240,text="Rating" ,fill="yellow",font=("Arial",13))
    canvas.create_text(70,280,text="Review" ,fill="yellow",font=("Arial",13))
    var = StringVar(root)
    var.set(1)
    secmenu=  ttk.Combobox(root, width=30,height=20,textvariable=var)
    secmenu['values'] =list(range(1,6))
    secmenu['state'] = 'readonly'
    feedEntry=Text(canvas, height=10, width=50,fg='black',bg="white",bd=4,font=("Arial",10,'italic'))
    canvas.create_window(350,365,window=feedEntry)
    canvas.create_window(277,240,window=secmenu)

def changepass():
    global oldpassEntered
    global passEntered
    global loggeduser
    global var
    global root
    global user
    opass=oldpassEntered.get()
    pwd=passEntered.get()
    if opass!="" and pwd!="":
        flag=0
        f=open("users.txt",'r')
        users=list(f)
        f.close()
        for i in range(len(users)):
            uname,passw,nme,email,secq,secan=users[i].split('|')
            if opass==passw and loggeduser ==uname:
                users[i]=uname+'|'+pwd+'|'+nme+'|'+email+'|'+secq+'|'+secan
                flag=1
        if flag:
             f=open("users.txt",'w')
             for i in users:
                 f.write(i)
             f.close()
             messagebox.showinfo("Successfull", "Password Reset Success ")
        else:
             messagebox.showerror("Error", "Invalid Eixting Password")
    else:
         messagebox.showerror("Error", "Empty Enrties")

def viewbooking():
    global canvas
    global backgroundIMG
    global y
    global loggeduser
    canvas.delete('all')
    
    rebutton=Button(canvas,text="<< BACK",width=15,fg="white",bg="gray",bd=5,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(1200,30,window=rebutton)
    backgroundIMG=PhotoImage(file="background5.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    x,y=0,30
    canvas.create_rectangle(100,430,1170,650,fill="gray")
    canvas.create_text(620,460,text="Your bookings " ,fill="white",font=("Arial",25,'bold'))
    try:
        f=open(loggeduser+'.txt','r')
        hiss=list(f)
        f.close()
        h=["Passanger","PhoneNo","Source","Destination","Date of Journey","class"]
        for j in range(len(h)):
                canvas.create_text(150+x,500,text=str(h[j]) ,fill="white",font=("Arial",13,'bold'))
                x+=230
        for i in range(len(hiss)):
            x=0
            xi=hiss[i].split('|')
            xi[-1]=xi[-1].rstrip()
            for j in range(len(xi)):
                canvas.create_text(150+x,510+y,text=str(xi[j]) ,fill="white",font=("Arial",12))
                x+=230
            y+=30
    except:
        canvas.create_text(620,280,text="No bookings to show" ,fill="white",font=("Arial",12))
def forgotpage():
    global root
    global canvas
    global userEntered
    global passEntered
    global var
    global securityanswer
    global backgroundIMG
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background4.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(90,150,430,550,fill="#000",outline="white")
    canvas.create_text(600,50,text="FORGOT PASSWORD",fill='yellow',font=("Arial",50,'bold'))
    canvas.create_text(245,200,text="Reset Password",fill='yellow',font=("Arial",25,'bold'))
    canvas.create_text(150,300,text="Username",fill='yellow',font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bg="white",bd=4,fg='#000',font=("Arial",13,'bold'))
    canvas.create_text(150,350,text="Password",fill='yellow',font=("Arial",13,'bold'))
    canvas.create_text(150,460,text="Answer",fill='yellow',font=("Arial",13,'bold'))
    canvas.create_text(250,390,text="Security Question:",fill='yellow',font=("Arial",13,'bold'))
    bullet = "\u2022"
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show=bullet)
    canvas.create_window(290,300,window=userEntered)
    canvas.create_window(290,350,window=passEntered)
    var = StringVar(root)
    var.set("What was your childhood nickname?")
    secmenu=  ttk.Combobox(root, width=40,height=20,textvariable=var)
    secmenu['values'] =["What was your childhood nickname?","What is your favorite movie?","What was the make and model of your first car?","What school did you attend for sixth grade?"]
    secmenu['state'] = 'readonly'

    securityanswer=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_window(280,420,window=secmenu)
    canvas.create_window(290,460,window=securityanswer)
    Resetbutton=Button(canvas,text="<< BACK",width=10,fg="black",bg="#fff",bd=4,font=("Arial",12,'bold'),command=loginpage)
    canvas.create_window(185,510,window=Resetbutton)
    loginbutton=Button(canvas,text="Reset Password",width=15,fg="black",bg="#fff",bd=4,font=("Arial",12,'bold'),command=forgotpass)
    canvas.create_window(330,510,window=loginbutton)
    
def book():
    global Fromvar
    global Tovar
    global DayVar
    global MonVar
    global yrVar
    global classvar
    global canvas
    global loggeduser
    global PassName
    global PhoneNo
    if PhoneNo.get().isdigit():
        f=open(loggeduser+'.txt','a')
        if len(PhoneNo.get())==10 or PassName.get()!='' :
            f.write(PassName.get()+'|'+PhoneNo.get()+'|'+Fromvar.get()+'|'+Tovar.get()+'|'+str(DayVar.get())+'-'+str(MonVar.get())+'-'+str(yrVar.get())+'|'+classvar.get()+'\n')
            messagebox.showinfo("Success", "Your booking is Successfull")
            f.close()
        else:
             messagebox.showerror("Error", "Empty PhoneNo or Passanger Name")
             f.close()
    else:
        messagebox.showerror("Error", "Please Enter Only Digits in PhoneNo")
cvar,cvar1=0,0
def createFrom(event):
    global canvas
    global cvar
    global fvar
    global Fromvar
    global line
    if cvar>0:
        canvas.delete(fvar,line)
    fvar=canvas.create_text(653,50,text=Fromvar.get(),font=("Arial",10,"bold"),fill="white")
    line=canvas.create_line(700,50,750,50,fill="White",arrow=LAST,width=2)
    cvar+=1
def createTo(event):
    global canvas
    global cvar1
    global fvar1
    global Tovar
    global Fromvar
    global fare
    if cvar1>0:
        canvas.delete(fvar1)
    fvar1=canvas.create_text(800,50,text=Tovar.get(),font=("Arial",10,"bold"),fill="white")
    fre=0
    cvar1+=1
cvar2=0
def classget():
    global canvas
    global cvar2
    global Tovar
    global classvar
    global Fromvar
    global fare
    if cvar2>0:
        canvas.delete(fare)
    mul=1
    if classvar.get()=="Economy":
        mul=1
    elif classvar.get()=="buissness":
        mul=3
    else:
        mul=5
    locs=["Delhi",
          "Mumbai",
          "Chennai",
          "Kolkata",
          "Jaipur",
          "Guwahati",
          "Indore",
          "Chandigarh",
          "Lucknow",
          "Agra",
          "Hayderabad",
          "Pune",
          "Nasik",
          "Panji"]
    fre=locs.index(Fromvar.get())-locs.index(Tovar.get())
    fare=canvas.create_text(880,50,text="Fare :"+str(abs(fre*100*mul)),font=("Arial",10,"bold"),fill="white")
    cvar2+=1
    
def cabbook():
    global root
    global backgroundIMG
    global Fromvar
    global Tovar
    global DayVar
    global MonVar
    global yrVar
    global classvar
    global canvas
    global loggeduser
    global PassName
    global PhoneNo
    global loggedname
    root=Tk()
    root.title("Login Page")
    canvas=Canvas(root,width=1270,height=680,highlightthickness=0)
    backgroundIMG=PhotoImage(file="background3.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(0,0,1270,120,fill="indigo",outline="navy blue")
    canvas.create_rectangle(490,120,790,390,fill="indigo")
    canvas.create_text(20,20,text="JCabs",fill='white',font=("bauhaus 93",25),anchor=NW)
    canvas.create_text(20,70,text="The best a cab can get",fill='white',font=("Lucida calligraphy",15),anchor=NW)
    IndiaMap=PhotoImage(file="India-map2.gif")
    canvas.create_image(600,60,image=IndiaMap)
    canvas.create_text(490,35,text="O",fill='white',font=("Comic sans",13))
    canvas.create_text(490,50,text=".",fill='white',font=("Comic sansr",20))
    canvas.create_text(490,70,text=".",fill='white',font=("Comic sans",20))
    canvas.create_text(522,35,text="From",fill='white',font=("Arial",10))
    canvas.create_text(520,100,text="To",fill='white',font=("Arial",10))
    Locicon=PhotoImage(file="loc-icon.gif")
    canvas.create_image(490,100,image=Locicon)
    Fromvar = StringVar(root)
    Fromvar.set("Delhi")
    From=  ttk.Combobox(root, width=30,height=20,textvariable=Fromvar)
    From['values'] =["Delhi",
                     "Mumbai",
                     "Chennai",
                     "Kolkata",
                     "Jaipur",
                     "Guwahati",
                     "Indore",
                     "Chandigarh",
                     "Lucknow",
                     "Agra",
                     "Hayderabad",
                     "Pune",
                     "Nasik",
                     "Panji"]
    From['state'] = 'readonly'
    From.bind('<<ComboboxSelected>>',createFrom)
    Tovar = StringVar(root)
    Tovar.set("Delhi")
    To=  ttk.Combobox(root, width=30,height=20,textvariable=Tovar)
    To['values'] =["Delhi",
                     "Mumbai",
                     "Chennai",
                     "Kolkata",
                     "Jaipur",
                     "Guwahati",
                     "Indore",
                     "Chandigarh",
                     "Lucknow",
                     "Agra",
                     "Hayderabad",
                     "Pune",
                     "Nasik",
                     "Panji"]

    To['state'] = 'readonly'
    To.bind('<<ComboboxSelected>>',createTo)
    canvas.create_window(765,35,window=From)
    canvas.create_window(765,100,window=To)
    DayVar = StringVar(root)
    DayVar.set(1)
    Day=  ttk.Combobox(root, width=3,height=20,textvariable=DayVar)
    Day['values'] =list(range(1,32))
    Day['state'] = 'readonly'
    canvas.create_text(510,140,text="Day",font=("Arial",10))
    canvas.create_window(555,140,window=Day)
    MonVar = StringVar(root)
    MonVar.set(1)
    Mon=  ttk.Combobox(root, width=3,height=20,textvariable=MonVar)
    Mon['values'] =list(range(1,13))
    Mon['state'] = 'readonly'
    canvas.create_text(600,140,text="Month",font=("Arial",10))
    canvas.create_window(660,140,window=Mon)
    yrVar = StringVar(root)
    yrVar.set(2018)
    yr=  ttk.Combobox(root, width=5,height=20,textvariable=yrVar)
    yr['values'] =list(range(2018,2030))
    yr['state'] = 'readonly'
    canvas.create_text(710,140,text="Year",font=("Arial",10))
    canvas.create_window(755,140,window=yr)
    classvar=StringVar(root)
    canvas.create_text(645,180,text="Select Class of Travel",font=("Arial",10))
    r1=Radiobutton(root,text="Economy",variable=classvar,bg="white",value="Economy",command=classget)
    canvas.create_window(545,210,window=r1)
    r2=Radiobutton(root,text="buissness",variable=classvar,bg="white",value="buissness",command=classget)
    canvas.create_window(645,210,window=r2)
    r3=Radiobutton(root,text="Luxury",variable=classvar,bg="white",value="Luxury",command=classget)
    canvas.create_window(745,210,window=r3)
    PhoneNo=Entry(canvas,bd=3)
    PassName=Entry(canvas,bd=3)
    canvas.create_text(555,250,text="Passanger Name",font=("Arial",10))
    canvas.create_window(715,250,window=PassName)
    canvas.create_text(570,280,text="Phone No.",font=("Arial",10))
    canvas.create_window(715,280,window=PhoneNo)
    bookbutton=Button(canvas,text="Book Ride",width=10,fg="white",bg="#800080",bd=5,font=("Arial",13,'bold'),command=book)
    canvas.create_window(565,350,window=bookbutton)
    canvas.create_text(300,270,text="Welcome "+loggedname,font=("Lucida calligraphy",20),fill="black")
    canvas.pack()
    detbutton=Button(canvas,text="Change your Password",width=25,fg="white",bg="purple",bd=5,font=("Arial",13,'bold'),command=changepasswordpage)
    canvas.create_window(1180,20,window=detbutton)
    lobutton=Button(canvas,text="View Past booking",width=25,fg="white",bg="purple",bd=5,font=("Arial",13,'bold'),command=viewbooking)
    canvas.create_window(1180,62,window=lobutton)
    cpbutton=Button(canvas,text="Review",width=25,fg="white",bg="purple",bd=5,font=("Arial",13,'bold'),command=feedpage)
    canvas.create_window(1180,102,window=cpbutton)
    revbutton=Button(canvas,text="Logout",width=10,fg="white",bg="purple",bd=5,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(695,350,window=revbutton)
    root.mainloop()
def cadminlogin():
    global userEntered
    global passEntered
    global root
    flag=True
    usr=userEntered.get()
    pwd=passEntered.get()
    if usr=="BABI" and pwd=="BABI":
            showfeed()
            return
    messagebox.showerror("Error", "Invalid Id or password")
def showfeed():
    global canvas
    global backgroundIMG
    global y
    global loggeduser
    canvas.delete('all')
    
    rebutton=Button(canvas,text="< LOGOUT >",width=15,fg="black",bg="yellow",bd=5,font=("Arial",13,'bold'),command=adminloginpage)
    canvas.create_window(615,475,window=rebutton)
    backgroundIMG=PhotoImage(file="background7.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    x,y=0,30
    canvas.create_rectangle(70,70,700,500,fill="black")
    canvas.create_text(370,100,text="Reviews " ,fill="yellow",font=("Arial",25,'bold'))
    try:
        f=open('reviews.txt','r')
        hiss=list(f)
        f.close()
        h=["User","Rating","Review"]
        for j in range(len(h)):
                canvas.create_text(110+x,150,text=str(h[j]) ,fill="yellow",font=("Arial",13,'bold'))
                x+=250
        for i in range(len(hiss)):
            x=0
            xi=hiss[i].split('|')
            xi[-1]=xi[-1].rstrip()
            for j in range(len(xi)):
                canvas.create_text(90+x,150+y,text=str(xi[j]) ,fill="yellow",font=("Arial",12),anchor=NW)
                x+=230
            y+=30
    except:
        canvas.create_text(350,280,text="No Reviews to show" ,fill="yellow",font=("Arial",12))
def adminloginpage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background2.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(1178,178,890,555,fill="#5D478B",outline="white")
    canvas.create_text(600,50,text="ADMIN",fill='black',font=("Arial",50,'bold'))
    canvas.create_text(1035,220,text="Admin Details",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(937,320,text="Username :",fill='white',font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'))
    canvas.create_text(937,370,text="Password :",fill='white',font=("Arial",13,'bold'))
    passEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(1080,320,window=userEntered)
    canvas.create_window(1080,370,window=passEntered)
    Loginbutton=Button(canvas,text="<< BACK",width=10,fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(970,450,window=Loginbutton)
    sbutton=Button(canvas,text="Login >>",width=10,fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=cadminlogin)
    canvas.create_window(1110,450,window=sbutton)
def changepasswordpage():
    global root
    global canvas
    global oldpassEntered
    global passEntered
    global var
    global securityanswer
    global backgroundIMG
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background4.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(50,150,430,500,fill="#000",outline="white")
    canvas.create_text(600,50,text="CHANGE PASSWORD",fill='yellow',font=("Arial",50,'bold'))
    canvas.create_text(205,200,text="Reset Password",fill='yellow',font=("Arial",25,'bold'))
    canvas.create_text(110,300,text="Old Password",fill='yellow',font=("Arial",13,'bold'))
    oldpassEntered=Entry(canvas,bg="white",bd=4,fg='#000',font=("Arial",13,'bold'),show="*")
    canvas.create_text(110,350,text="New Password",fill='yellow',font=("Arial",13,'bold'))
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(270,300,window=oldpassEntered)
    canvas.create_window(270,350,window=passEntered)
    Resetbutton=Button(canvas,text="<< Back",width=10,fg="black",bg="#fff",bd=4,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(145,430,window=Resetbutton)
    backbutton=Button(canvas,text="Reset Password",fg="black",width=15,bg="#fff",bd=4,font=("Arial",13,'bold'),command=changepass)
    canvas.create_window(290,430,window=backbutton)
def loginpage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background2.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(1178,178,890,555,fill="#5D478B",outline="black")
    canvas.create_text(600,50,text="LOGIN",fill='black',font=("Arial",50,'bold'))
    canvas.create_text(1035,220,text="Login Details",fill='white',font=("Arial",15,'bold'))
    canvas.create_text(937,300,text="USERNAME :",fill='white',font=("Arial",10,'bold'))
    userEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'))
    canvas.create_text(937,350,text="PASSWORD :",fill='white',font=("Arial",10,'bold'))
    passEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(1080,300,window=userEntered)
    canvas.create_window(1080,350,window=passEntered)
    Loginbutton=Button(canvas,text="ADMIN LOGIN",width=10,fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=adminloginpage)
    canvas.create_window(970,450,window=Loginbutton)
    Regbutton=Button(canvas,text="LOGIN >>",width=10,fg="white",bg="#8968CD",bd=5,font=("Arial",13,'bold'),command=validate)
    canvas.create_window(1110,450,window=Regbutton)
    forgbutton=Button(canvas,text="Forgot Password!",fg="white",bg="#5D478B",bd=0,font=("Arial",10,'underline'),command=forgotpage)
    canvas.create_window(1040,390,window=forgbutton)
    abutton=Button(canvas,text="Don't have account!",fg="white",bg="#5D478B",bd=0,font=("Arial",10,'underline'),command=RegisterPage)
    canvas.create_window(1035,500,window=abutton)
    canvas.pack()
    root.mainloop()
root=Tk()
root.title("Login Page")
canvas=Canvas(root,width=1270,height=680,highlightthickness=0)
loginpage()
