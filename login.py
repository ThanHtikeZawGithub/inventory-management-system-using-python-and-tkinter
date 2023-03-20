from tkinter import *
from PIL import ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import os
import email_pass
import smtplib
import time

class loginclass:

    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("Login System | Developed by ThanHtikeZaw")
        self.root.config(bg='#fafafa')

        # self.otp=''
        #--title---
        self.phone_image = ImageTk.PhotoImage(file='C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\icover.PNG')
        self.lbl_phone_image = Label(self.root,image=self.phone_image,bd=0).place(x=0,y=0)

        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_frame.place(x=1000,y=50,width=350,height=450)

        title = Label(login_frame,text='Login System',compound='left',font=('Elephant', 30, 'bold'),bg='#010c48',fg='white',anchor='w',padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        lbl_user = Label(login_frame,text='Employee ID',font=('Andalus',15),bg='white',fg='#767171')
        lbl_user.place(x=50,y=100)
        self.employee_id = StringVar()
        self.password = StringVar()
        txt_user = Entry(login_frame,textvariable=self.employee_id,font=('times new roman',15),bg='#ECECEC')
        txt_user.place(x=50,y=140,width=250)

        lbl_passwd = Label(login_frame,text='Password',font=('Andalus',15),bg='white',fg='#767171')
        lbl_passwd.place(x=50,y=200)
        txt_passwd = Entry(login_frame,textvariable=self.password,font=('times new roman',15),bg='#ECECEC')
        txt_passwd.place(x=50,y=240,width=250)

        btn_login = Button(login_frame,text='Log in',command=self.login,font=('Arial Rounded MT Bold',15),bg='#00B0F0',activeforeground='white',cursor='hand2')
        btn_login.place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg='lightgray').place(x=50,y=360,width=250,height=2)
        or_=Label(login_frame,text='OR',bg='white',fg='lightgray',font=('times new roman',15,'bold')).place(x=150,y=350)

        btn_forget = Button(login_frame,text='Forget Password?',command=self.forget_window,font=('times new roman',13),bg='white',fg='#00759E',bd=0,activebackground='white',activeforeground='#00759E')
        btn_forget.place(x=100,y=390)

        #===Frame2=========
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        register_frame.place(x=1000,y=570,width=350,height=60)


        lbl_reg=Label(register_frame,text="Don't have an account?",font=('times new roman',13),bg='white').place(x=40,y=20)
        btn_signup = Button(register_frame,text='Sign UP',font=('times new roman',13,'bold'),bg='white',fg='#00759E',bd=0,activebackground='white',activeforeground='#00759E')
        btn_signup.place(x=200,y=17)

        # self.send_email('xyz')


        





    def login(self):
        db = mysql.connector.connect(
                host ='localhost',
                user = 'root',
                passwd = 'Thanhtikezaw1998@',
                database = 'ims'
                )
        mycursor = db.cursor()
        try:
            if self.employee_id.get()=='' or self.password.get()=='':
                messagebox.showerror('Error','All Fields are required',parent=self.root)
            else:
                mycursor.execute('SELECT utype FROM employee WHERE eid=%s AND passwd=%s',(self.employee_id.get(),self.password.get()))
                user = mycursor.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid UserName/Password',parent=self.root)
                else:
                    print(user)
                    if user[0]=='Admin':
                        self.root.destroy()
                        os.system("python C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\billing.py") 
        except Exception as ex:
            messagebox.showerror('Error',f'Error Due to : {str(ex)}',parent=self.root)

    def forget_window(self):
        db = mysql.connector.connect(
                host ='localhost',
                user = 'root',
                passwd = 'Thanhtikezaw1998@',
                database = 'ims'
                )
        mycursor = db.cursor()
        try:
            if self.employee_id.get()=='':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                mycursor.execute('SELECT email FROM employee WHERE eid=%s',(self.employee_id.get(),))
                email = mycursor.fetchone()
                if email==None:
                    messagebox.showerror('Error','Invalid Employee ID,try again',parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_conf_password=StringVar()
                    # chk=self.send_email(email[0])
                    # if chk == 'f':
                    #     messagebox.showerror('Error','Connection Error,try again',parent=self.root)
                    # else:      
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()

                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white')
                    title.pack(side=TOP,fill=X)
                        #====forget window=====
                    lbl_reset=Label(self.forget_win,text='Enter OTP sent on Registered Email',font=('times new roman',15))
                    lbl_reset.place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('times new roman',15),bg='lightyellow')
                    txt_reset.place(x=20,y=100,width=250,height=30)
                    self.btn_submit=Button(self.forget_win,text='Submit',font=('times new roman',15),bg='lightblue')
                    self.btn_submit.place(x=280,y=100,height=30)

                    lbl_new_password=Label(self.forget_win,text='New Password',font=('times new roman',15))
                    lbl_new_password.place(x=20,y=160)
                    txt_new_password=Entry(self.forget_win,textvariable=self.var_new_password,font=('times new roman',15),bg='lightyellow')
                    txt_new_password.place(x=20,y=190,width=250,height=30)

                    lbl_conf_password=Label(self.forget_win,text='Confirm Password',font=('times new roman',15))
                    lbl_conf_password.place(x=20,y=225)
                    txt_conf_password=Entry(self.forget_win,textvariable=self.var_conf_password,font=('times new roman',15),bg='lightyellow')
                    txt_conf_password.place(x=20,y=255,width=250,height=30)

                    self.btn_update=Button(self.forget_win,text='Update',state=DISABLED,font=('times new roman',15),bg='lightblue')
                    self.btn_update.place(x=150,y=300,width=100,height=30)
        except Exception as ex:
            messagebox.showerror('Error',f'Error Due to : {str(ex)}',parent=self.root)


    # def send_email(self,to_):
    #     s = smtplib.SMTP('smtp.gmail.com',587)
    #     s.starttls()
    #     email_=email_pass.email_
    #     pass_=email_pass.pass_

    #     s.login(email_,pass_)

    #     self.otp = str(time.strftime("%H%M%S"))+str(time.strftime("%S"))
        
    #     subj = 'IMS-Reset Password OTP'
    #     msg = 'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\n With Regards,\nIMS Team'
    #     msg='Subject:{}\n\n{}'.format(subj,msg)
    #     s.sendmail(email_,to_,msg)
    #     chk=s.ehlo()
    #     if chk[0]==250:
    #         return 's'
    #     else:
    #         return 'f'


root = Tk()
obj = loginclass(root)
root.mainloop()