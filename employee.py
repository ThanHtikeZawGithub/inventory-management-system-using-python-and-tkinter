from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector
class employeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x520+220+130')
        self.root.title("Inventory Management System | Employees")
        self.root.config(bg='white')
        self.root.focus_force()
        #===========================================
        #All variables=========
        self.var_emp_searchby = StringVar()
        self.var_emp_searchtext = StringVar()
        self.var_emp_id = StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_pass = StringVar()
        self.var_emp_utype = StringVar() 
        self.var_emp_salary = StringVar()


        #search frame
        SearchFrame= LabelFrame(self.root,text='Search Employee',bg='white')
        SearchFrame.place(x=250,y=20,width=600, height=70)
 
        #list in search (option)
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_emp_searchby, values=('Select','Email','Name','Contact'),state='randomly', justify=CENTER, font=('goudy old style',15,'bold'))
        cmb_search.place(x=10,y=10, width=180) 
        cmb_search.current(0)

        txt_search = Entry(SearchFrame,textvariable=self.var_emp_searchtext,font=('goudy old style',15),bg='lightyellow')
        txt_search.place(x=200,y=10)
        txt_but = Button(SearchFrame,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',fg='white')
        txt_but.place(x=410,y=10,width=150,height=30)

        #title
        title = Label(self.root,text='Employee Detail',font=('goudy old style',15),bg='#0f4d7d',fg='white')
        title.place(x=50,y=100,width=1000)

        #content

        #row 1
        lbl_empid = Label(self.root,text='Emp ID',font=('goudy old style',15),bg='white')
        lbl_empid.place(x=50,y=150)
        lbl_gender = Label(self.root,text='Gender',font=('goudy old style',15),bg='white')
        lbl_gender.place(x=400,y=150)
        lbl_contact = Label(self.root,text='Contact',font=('goudy old style',15),bg='white')
        lbl_contact.place(x=750,y=150)

        lbl_empid = Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),bg='white')
        lbl_empid.place(x=150,y=150)
        # lbl_gender = Entry(self.root,textvariable=self.var_emp_gender,font=('goudy old style',15),bg='white')
        # lbl_gender.place(x=500,y=150)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_emp_gender,values=('Select','Male','Female'),font=('goudy old style',15,'bold'))
        cmb_gender.place(x=500,y=150,width=200)
        cmb_gender.current(0)

        lbl_contact = Entry(self.root,textvariable=self.var_emp_contact,font=('goudy old style',15),bg='white')
        lbl_contact.place(x=850,y=150)

        # row 2

        lbl_name = Label(self.root,text='Name',font=('goudy old style',15),bg='white')
        lbl_name.place(x=50,y=200)
        lbl_dob = Label(self.root,text='D.O.B',font=('goudy old style',15),bg='white')
        lbl_dob.place(x=400,y=200)
        lbl_doj = Label(self.root,text='D.O.J',font=('goudy old style',15),bg='white')
        lbl_doj.place(x=750,y=200)

        lbl_name = Entry(self.root,textvariable=self.var_emp_name,font=('goudy old style',15),bg='white')
        lbl_name.place(x=150,y=200)
        lbl_dob = Entry(self.root,textvariable=self.var_emp_dob,font=('goudy old style',15),bg='white')
        lbl_dob.place(x=500,y=200)
        lbl_doj = Entry(self.root,textvariable=self.var_emp_doj,font=('goudy old style',15),bg='white')
        lbl_doj.place(x=850,y=200)

        #row 3

        lbl_email = Label(self.root,text='Email',font=('goudy old style',15),bg='white')
        lbl_email.place(x=50,y=250)
        lbl_password = Label(self.root,text='Password',font=('goudy old style',15),bg='white')
        lbl_password.place(x=400,y=250)
        lbl_usertype = Label(self.root,text='User Type',font=('goudy old style',15),bg='white')
        lbl_usertype.place(x=750,y=250)

        lbl_email = Entry(self.root,textvariable=self.var_emp_email,font=('goudy old style',15),bg='white')
        lbl_email.place(x=150,y=250)
        lbl_password = Entry(self.root,textvariable=self.var_emp_pass,font=('goudy old style',15),bg='white')
        lbl_password.place(x=500,y=250)
        cmb_usertype = ttk.Combobox(self.root,textvariable=self.var_emp_utype,values=('Select','Admin','Employee'),font=('goudy old style',15))
        cmb_usertype.place(x=850,y=250)
        cmb_usertype.current(0)
        

        lbl_address = Label(self.root,text='Address',font=('goudy old style',15),bg='white')
        lbl_address.place(x=50,y=300)
        lbl_salary = Label(self.root,text='Salary',font=('goudy old style',15),bg='white')
        lbl_salary.place(x=550,y=300)
        
        self.txt_address = Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txt_address.place(x=150,y=300,width=300,height=60)
        lbl_salary = Entry(self.root,textvariable=self.var_emp_salary,font=('goudy old style',15),bg='white')
        lbl_salary.place(x=600,y=300)

        #save button
        save_but = Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white',cursor='hand2')
        save_but.place(x=500,y=335,width=110,height=28)
        update_but = Button(self.root,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2')
        update_but.place(x=620,y=335,width=110,height=28)
        clear_but = Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#f44336',fg='white',cursor='hand2')
        clear_but.place(x=740,y=335,width=110,height=28)
        delete_but = Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#607d8b',fg='white',cursor='hand2')
        delete_but.place(x=860,y=335,width=110,height=28)


        #Employee Details======

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=370,relwidth=1,height=150)

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=('eid','name','email','gender','contact','dob','doj','passwd','utype','address','salary'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)


        self.EmployeeTable.heading('eid',text='EMP ID')
        self.EmployeeTable.heading('name',text='Name')
        self.EmployeeTable.heading('email',text='Email')
        self.EmployeeTable.heading('gender',text='Gender')
        self.EmployeeTable.heading('contact',text='Contact')
        self.EmployeeTable.heading('dob',text='D.O.B')
        self.EmployeeTable.heading('doj',text='D.O.J')
        self.EmployeeTable.heading('passwd',text='Password')
        self.EmployeeTable.heading('utype',text='User Type')
        self.EmployeeTable.heading('address',text='Address')
        self.EmployeeTable.heading('salary',text='Salary')

        self.EmployeeTable['show'] = 'headings'

        self.EmployeeTable.column('eid', width=90)
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('email',width=100)
        self.EmployeeTable.column('gender',width=100)
        self.EmployeeTable.column('contact',width=100)
        self.EmployeeTable.column('dob',width=100)
        self.EmployeeTable.column('doj',width=100)
        self.EmployeeTable.column('passwd',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('address',width=100)
        self.EmployeeTable.column('salary',width=200)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>',self.get_data)

        self.show()

#==============================================================================
    def add(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM employee WHERE eid=%s ",(self.var_emp_id.get(),))
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror('Error','This Employee ID already assinged, try different ID')
                else:
                    mycursor.execute('INSERT INTO employee (eid,name,email,gender,contact,dob,doj,passwd,utype,address,salary) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(    
                                        self.var_emp_id.get(),
                                        self.var_emp_name.get(),
                                        self.var_emp_email.get(),
                                        self.var_emp_gender.get(),
                                        self.var_emp_contact.get(),
                                        self.var_emp_dob.get(),
                                        self.var_emp_doj.get(),
                                        self.var_emp_pass.get(),
                                        self.var_emp_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_emp_salary.get()
                                        ))
                    db.commit()
                    messagebox.showinfo('Success','Employee Added Successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)


    def show(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            mycursor.execute('SELECT * FROM employee')
            rows = mycursor.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_gender.set(row[3]),
        self.var_emp_contact.set(row[4]),
        self.var_emp_dob.set(row[5]),
        self.var_emp_doj.set(row[6]),
        self.var_emp_pass.set(row[7]),
        self.var_emp_utype.set(row[8]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_emp_salary.set(row[10])

    def update(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM employee WHERE eid=%s ",(self.var_emp_id.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Employee ID',parent=self.root)
                else:
                    mycursor.execute('UPDATE employee SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,doj=%s,passwd=%s,utype=%s,address=%s,salary=%s WHERE eid=%s',(    
                                        self.var_emp_name.get(),
                                        self.var_emp_email.get(),
                                        self.var_emp_gender.get(),
                                        self.var_emp_contact.get(),
                                        self.var_emp_dob.get(),
                                        self.var_emp_doj.get(),
                                        self.var_emp_pass.get(),
                                        self.var_emp_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_emp_salary.get(),
                                        self.var_emp_id.get()
                                        ))
                    db.commit()
                    messagebox.showinfo('Success','Employee Updated Successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

    def delete(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM employee WHERE eid=%s ",(self.var_emp_id.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Employee ID',parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm",'Do u really want to delete?',parent=self.root)
                    if op == True:
                        mycursor.execute("DELETE FROM employee WHERE eid=%s",(self.var_emp_id.get(),))
                        db.commit()
                        messagebox.showinfo("Delete","Employee Deleted Sucessfully",parent=self.root)
                        self.clear()
            
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set(''),
        self.var_emp_name.set(''),
        self.var_emp_email.set(''),
        self.var_emp_gender.set(''),
        self.var_emp_contact.set(''),
        self.var_emp_dob.set(''),
        self.var_emp_doj.set(''),
        self.var_emp_pass.set(''),
        self.var_emp_utype.set('Admin'),
        self.txt_address.delete('1.0',END),
        self.var_emp_salary.set('')
        self.var_emp_searchtext.set(''),
        self.var_emp_searchby.set('Select')
        self.show()

    def search(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_emp_searchby.get()=='Select':
                messagebox.showerror('Error','Select Search by Option',parent=self.root)
            elif self.var_emp_searchby.get()=='':
                messagebox.showerror("Error",'Search input should be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM employee WHERE" + self.var_emp_searchby.get() +"LIKE '%"+self.var_emp_searchtext.get()+"%'")
                rows = mycursor.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)



        


if __name__=='__main__':
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()