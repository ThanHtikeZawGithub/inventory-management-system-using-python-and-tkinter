from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import ttk,messagebox
from employee import employeeClass
from supplier import SupplierClass
from category import category
from product import products
from sales import SaleClass
import os
import time

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("Inventory Management System | Developed by ThanHtikeZaw")
        self.root.config(bg='white')
        #--title---
        self.icon = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\logo1.PNG')
        self.icon = self.icon.resize((140, 70),Image.ANTIALIAS)
        self.icon = ImageTk.PhotoImage(self.icon)

        title = Label(self.root,text='Inventory Management System',image=self.icon,compound='left',font=('Time New Roman', 40, 'bold'),bg='#010c48',fg='white',anchor='w',padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #button logout

        btn_logout = Button(self.root,text='Logout',command=self.logout,font=('Time New Roman',15,'bold'),bg='white',fg='#010c48')
        btn_logout.place(x=1150,y=10,width=150,height=50)
        
        #clock
        self.lbl_clock = Label(self.root,text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS',font=('Time New Roman', 15, 'bold'),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #left menu
        #image
        self.MenuLogo = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\Lmenu.PNG')
        self.MenuLogo = self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        #frame
        Leftmenu = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Leftmenu.place(x=0,y=102,width=200,height=585)
        #image location
        lbl_menulogo = Label(Leftmenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        btn_menu = Label(Leftmenu,text='Menu',font=('Time New Roman',20,'bold'),bg='#009688',fg='black').pack(side=TOP,fill=X)
        btn_employee = Button(Leftmenu,text='Employees',command=self.employee,font=('Time New Roman',20,'bold'),bg='white', bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_supplier = Button(Leftmenu,text='Supplier',command=self.supplier,font=('Time New Roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_category = Button(Leftmenu,text='Category',command=self.category,font=('Time New Roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_products = Button(Leftmenu,text='Products',command=self.product,font=('Time New Roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_sales = Button(Leftmenu,text='Sales',command=self.sale,font=('Time New Roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_exit = Button(Leftmenu,text='Exit',font=('Time New Roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(fill=X)

        #content
        self.lbl_employee = Label(self.root,text='Total Employee\n[0]',bd=5,relief=RIDGE,bg='#33bbf9',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root,text='Total Suppliers\n[0]',bd=5,relief=RIDGE,bg='#ff5722',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category = Label(self.root,text='Total Category\n[0]',bd=5,relief=RIDGE,bg='#009688',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text='Total Product\n[0]',bd=5,relief=RIDGE,bg='#607d8b',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text='Total Sales\n[0]',bd=5,relief=RIDGE,bg='#ffc107',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #footer
        lbl_footer = Label(self.root,text='IMS-Inventory Management System | Developed by ThanHtikeZaw\n For any Technical Issue Contact: yukihirasouma741@gmail.com',font=('Time New Roman', 10, 'bold'),bg='#4d636d',fg='white')
        lbl_footer.pack(side=BOTTOM,fill=X)

        self.update_content()

#====================================================================================================

    def employee(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = SupplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = category(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = products(self.new_win)

    def sale(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = SaleClass(self.new_win)

    def update_content(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            mycursor.execute('SELECT * FROM product')
            product = mycursor.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')

            mycursor.execute('SELECT * FROM supplier')
            supplier = mycursor.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            mycursor.execute('SELECT * FROM category')
            category = mycursor.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            mycursor.execute('SELECT * FROM employee')
            employee = mycursor.fetchall()
            self.lbl_employee.config(text=f'Total Product\n[{str(len(employee))}]')

            bill=str(len(os.listdir('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\bill')))
            self.lbl_sales.config(text=f'Total Sales\n[{bill}]')

            time_=time.strftime('%I:%M:%S')
            date_=time.strftime('%d-%m-%Y')

            self.lbl_clock.config(text=f'Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}')
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system('python C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\login.py')
    
if __name__=='__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()