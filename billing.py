from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import time
import os
import tempfile

class billing:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("Inventory Management System | Developed by ThanHtikeZaw")
        self.root.config(bg='white')
        self.cart_list = []
        self.chk_print=0
        #--title---
        self.icon1 = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\logo1.PNG')
        self.icon1 = self.icon1.resize((140, 70),Image.ANTIALIAS)
        self.icon1 = ImageTk.PhotoImage(self.icon1)

        title = Label(self.root,text='Inventory Management System',image=self.icon1,compound='left',font=('Time New Roman', 40, 'bold'),bg='#010c48',fg='white',anchor='w',padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #button logout

        btn_logout = Button(self.root,text='Logout',command=self.logout,font=('Time New Roman',15,'bold'),bg='white',fg='#010c48')
        btn_logout.place(x=1150,y=10,width=150,height=50)

        self.lbl_clock = Label(self.root,text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS',font=('Time New Roman', 15, 'bold'),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Product Frame=======
        self.var_search=StringVar()

        ProductFrame1 = Frame(self.root, bd=4,relief=RIDGE,bg='white')
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        cTitle = Label(ProductFrame1, text='All Products',font=('goudy old style',20,'bold'),bg='#262626',fg='white')
        cTitle.pack(side=TOP,fill=X)

        ProductFrame2 = Frame(ProductFrame1, bd=4,relief=RIDGE,bg='white')
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search = Label(ProductFrame2,text='Search Product | By Name',font=('times new roman',15,'bold'),bg='white',fg='green')
        lbl_search.place(x=2,y=5)

        lbl_name = Label(ProductFrame2,text='Product Name',font=('times new roman',15,'bold'),bg='white')
        lbl_name.place(x=2,y=45)

        lbl_search = Label(ProductFrame2,font=('times new roman',15,'bold'),bg='white')
        lbl_search.place(x=125,y=47,width=150,height=22)

        txt_search = Entry(ProductFrame2 ,textvariable=self.var_search,font=('times new roman',15,'bold'),bg='white')
        txt_search.place(x=125,y=47,width=150,height=22)

        btn_search = Button(ProductFrame2 ,text='Search',command=self.search,font=('times new roman',15,'bold'),bg='#2196f3',fg='white',cursor='hand2')
        btn_search.place(x=280,y=45,width=100,height=25)

        btn_show_all = Button(ProductFrame2 ,text='Show All',command=self.show,font=('times new roman',15,'bold'),bg='#083531',fg='white',cursor='hand2')
        btn_show_all.place(x=285,y=10,width=100,height=25)

        CustomerFrame = Frame(ProductFrame1,bd=3,relief=RIDGE)
        CustomerFrame.place(x=2,y=140,width=398,height=385)

        scrolly = Scrollbar(CustomerFrame,orient=VERTICAL)
        scrollx = Scrollbar(CustomerFrame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(CustomerFrame,columns=('pid','name','price','quantity','status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)


        self.productTable.heading('pid',text='P ID')
        self.productTable.heading('name',text='Name')
        self.productTable.heading('price',text='Price')
        self.productTable.heading('quantity',text='Quantity')
        self.productTable.heading('status',text='Status')

        self.productTable['show'] = 'headings'

        self.productTable.column('pid', width=20)
        self.productTable.column('name',width=100)
        self.productTable.column('price',width=70)
        self.productTable.column('quantity',width=100)
        self.productTable.column('status',width=40)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind('<ButtonRelease-1>',self.get_data)

        lbl_note = Label(ProductFrame1,text='Note:Enter 0 Quantity to remove product from the Cart',font=('goudy old style',12),bg='white',fg='red')
        lbl_note.pack(side=BOTTOM,fill=X)
#==============Customer Frame==========
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root,bd=4,relief=RIDGE,bg='white')
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle = Label(CustomerFrame, text='Customer Details',font=('goudy old style',15,'bold'),bg='lightgray')
        cTitle.pack(side=TOP,fill=X)

        lbl_name = Label(CustomerFrame,text='Name',font=('times new roman',13,'bold'),bg='white')
        lbl_name.place(x=5,y=35)

        txt_name = Entry(CustomerFrame ,textvariable=self.var_cname,font=('times new roman',13,'bold'),bg='lightyellow')
        txt_name.place(x=80,y=35,width=180)

        lbl_contact = Label(CustomerFrame,text='Contact No.',font=('times new roman',13,'bold'),bg='white')
        lbl_contact.place(x=270,y=35)

        txt_contact = Entry(CustomerFrame ,textvariable=self.var_contact,font=('times new roman',13,'bold'),bg='lightyellow')
        txt_contact.place(x=380,y=35,width=140)

        Cal_Cart_Frame = Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
#========= Calculator Frame================
        self.var_cal_input = StringVar()

        Cal_Frame = Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg='white')
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        self.txt_cal_input = Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE)
        self.txt_cal_input.grid(row=0,columnspan=4)

        btn_7 = Button(Cal_Frame,text='7',command=lambda:self.get_input('7'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_7.grid(row=1,column=0)
        btn_8 = Button(Cal_Frame,text='8',command=lambda:self.get_input('8'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_8.grid(row=1,column=1)
        btn_9 = Button(Cal_Frame,text='9',command=lambda:self.get_input('9'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_9.grid(row=1,column=2)
        btn_sum = Button(Cal_Frame,text= '+',command=lambda:self.get_input('+'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_sum.grid(row=1,column=3)

        btn_4 = Button(Cal_Frame,text='4',command=lambda:self.get_input('4'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_4.grid(row=2,column=0)
        btn_5 = Button(Cal_Frame,text='5',command=lambda:self.get_input('5'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_5.grid(row=2,column=1)
        btn_6 = Button(Cal_Frame,text='6',command=lambda:self.get_input('6'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_6.grid(row=2,column=2)
        btn_sub = Button(Cal_Frame,text= '-',command=lambda:self.get_input('-'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_sub.grid(row=2,column=3)

        btn_1 = Button(Cal_Frame,text='1',command=lambda:self.get_input('1'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_1.grid(row=3,column=0)
        btn_2 = Button(Cal_Frame,text='2',command=lambda:self.get_input('2'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_2.grid(row=3,column=1)
        btn_3 = Button(Cal_Frame,text='3',command=lambda:self.get_input('3'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_3.grid(row=3,column=2)
        btn_mul = Button(Cal_Frame,text= '*',command=lambda:self.get_input('*'),font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_mul.grid(row=3,column=3)

        btn_0 = Button(Cal_Frame,text='0',command=lambda:self.get_input('0'),font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2')
        btn_0.grid(row=4,column=0)
        btn_c = Button(Cal_Frame,text='C',command=self.clear_cal,font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2')
        btn_c.grid(row=4,column=1)
        btn_eq = Button(Cal_Frame,text='=',command=self.perform_cal,font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2')
        btn_eq.grid(row=4,column=2)
        btn_div = Button(Cal_Frame,text= '/',command=lambda:self.get_input('/'),font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2')
        btn_div.grid(row=4,column=3)



    #======== Cart Frame=================
        Cart_Frame = Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)

        self.cartTitle = Label(Cart_Frame, text='Cart Total Product: [0]',font=('goudy old style',15,'bold'),bg='lightgray')
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly = Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx = Scrollbar(Cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_Frame,columns=('pid','name','price','quantity'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)


        self.CartTable.heading('pid',text='P ID')
        self.CartTable.heading('name',text='Name')
        self.CartTable.heading('price',text='Price')
        self.CartTable.heading('quantity',text='Quantity')

        self.CartTable['show'] = 'headings'

        self.CartTable.column('pid', width=20)
        self.CartTable.column('name',width=100)
        self.CartTable.column('price',width=90)
        self.CartTable.column('quantity',width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind('<ButtonRelease-1>',self.get_data_cart)

#==============Add Cart Widgets Frame===================
        self.var_pid = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_stock = StringVar()

        AddCartWidgetFrame = Frame(self.root,bd=4,relief=RIDGE,bg='white')
        AddCartWidgetFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name = Label(AddCartWidgetFrame,text='Product Name',font=('times new roman',15),bg='white')
        lbl_p_name.place(x=5,y=5)
        txt_p_name = Entry(AddCartWidgetFrame,textvariable=self.var_name,font=('times new roman',15),bg='lightgray')
        txt_p_name.place(x=5,y=35,width=190,height=22)

        lbl_p_price = Label(AddCartWidgetFrame,text='Price Pre Qty',font=('times new roman',15),bg='white')
        lbl_p_price.place(x=215,y=5)
        txt_p_price = Entry(AddCartWidgetFrame,textvariable=self.var_price,font=('times new roman',15),bg='lightgray')
        txt_p_price.place(x=215,y=35,width=150,height=22)

        lbl_p_qty = Label(AddCartWidgetFrame,text='Quantity',font=('times new roman',15),bg='white')
        lbl_p_qty.place(x=390,y=5)
        txt_p_qty = Entry(AddCartWidgetFrame,textvariable=self.var_quantity,font=('times new roman',15),bg='lightgray')
        txt_p_qty.place(x=390,y=35,width=120,height=22)

        self.lbl_instock = Label(AddCartWidgetFrame,text='In Stock',font=('times new roman',15),bg='white')
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart = Button(AddCartWidgetFrame ,text='Clear',font=('times new roman',15,'bold'),bg='lightgray',cursor='hand2')
        btn_clear_cart.place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(AddCartWidgetFrame ,text='Add | Update',command=self.add_update_cart,font=('times new roman',15,'bold'),bg='orange',cursor='hand2')
        btn_add_cart.place(x=340,y=70,width=170,height=30)

        #============Billing Area======================
        billFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=390,height=410)

        bTitle = Label(billFrame, text='Customer Bill Area',font=('goudy old style',15,'bold'),bg='red',fg='white')
        bTitle.pack(side=TOP,fill=X)

        scrolly = Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area = Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
    


        #========billing buttons===========

        billMenuFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=390,height=140)

        self.lbl_amt = Label(billMenuFrame,text='Bill Amount\n[0]',font=('goudy old style',12,'bold'),bg='#3f51b5',fg='white')
        self.lbl_amt.place(x=2,y=5,width=120,height=70)

        self.lbl_dis = Label(billMenuFrame,text='Discount\n[5]',font=('goudy old style',12,'bold'),bg='#8bc34a',fg='white')
        self.lbl_dis.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay = Label(billMenuFrame,text='Net Pay\n[0]',font=('goudy old style',12,'bold'),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

        btn_print = Button(billMenuFrame,text='Print',command=self.print_bill,cursor='hand2',font=('goudy old style',12,'bold'),bg='#3f51b5',fg='white')
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all = Button(billMenuFrame,text='Clear All',command=self.clear_all,cursor='hand2',font=('goudy old style',12,'bold'),bg='#8bc34a',fg='white')
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate = Button(billMenuFrame,text='Generate/Save Bill',command=self.generate_bill,cursor='hand2',font=('goudy old style',12,'bold'),bg='#607d8b',fg='white')
        btn_generate.place(x=246,y=80,width=160,height=50)

        footer = Label(self.root,text='IMS-Inventory Management System | Developed by ThanHtikeZaw\nFor any technical issue contact email:yukihira741@gmail.com',font=('times new roman',11),bg='#4d636d',fg='white')
        footer.pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()
        
        

        #===========All Functions=========================

    def get_input(self,num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            # self.productTable=ttk.Treeview(CustomerFrame,columns=('pid','name','price','quantity','status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            mycursor.execute("SELECT pid,name,price,quantity,status FROM product WHERE status='Active'")
            rows = mycursor.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)

    def search(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            
            if self.var_search.get()=='':
                messagebox.showerror("Error",'Search input should be required',parent=self.root)
            else:
                mycursor.execute("SELECT pid,name,price,quantity,status FROM product WHERE name LIKE '%"+self.var_search.get()+"%' AND status='Active")
                rows = mycursor.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_price.set(row[2]),
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])

    def get_data_cart(self,ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_price.set(row[2]),
        self.var_quantity.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]"),
        self.var_stock.set(row[4])
        
    def add_update_cart(self):
        if self.var_pid.get() =='':
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_quantity.get()=='':
            messagebox.showerror('Error','Quantity is Required',parent=self.root)
        
        elif int(self.var_quantity.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error','Not enough quantity from the stock',parent=self.root)
        else:
            # price_cal =int(self.var_quantity.get()) *float(self.var_price.get())
            # price_cal = float(price_cal)
            price_cal = self.var_price.get()
            
            cart_data = [self.var_pid.get(),self.var_name.get(),price_cal,self.var_quantity.get(),self.var_stock.get()]
#===========update cart===============
            present ='no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present ='yes'
                    break
                index_+=1
            if present=='yes':
                op = messagebox.askyesno('Confirm','Product already present\nDo you want to Update| Remove from the list',parent=self.root)
                if op == True:
                    if self.var_quantity.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2] = price_cal
                        self.cart_list[index_][3] = self.var_quantity.get()
            else:
                self.cart_list.append(cart_data)
                

            self.show_cart()
            self.bill_update()
            
    def bill_update(self):
        self.bill_amt = 0
        self.net_pay =0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt = self.bill_amt + (float(row[2]) * int(row[3]))

        self.discount=(self.bill_amt*5)/100
        self.net_pay = self.bill_amt -self.discount
        self.lbl_amt.config(text=f'Bill Amount(Ks.)\n[{str(self.bill_amt)}]')
        self.lbl_net_pay.config(text=f"Net Pay(Ks.)\n[{str(self.net_pay)}]")
        self.cartTitle.config(text= f'Cart Total Product: [{str(len(self.cart_list))}]')


    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f'Customer Details are required',parent=self.root)
        elif len(self.cart_list) ==0:
            messagebox.showerror("Error",f"Please Add product to the Cart",parent=self.root)
        else:
            #======Bill top======
            self.bill_top()
            #======Bill middle===
            self.bill_middle()
            #=====Bill bottom========
            self.bill_bottom()

            fp=open(f'C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved','Bill has been generated/save in backend',parent=self.root)
            self.chk_print=1
            
    
    def bill_top(self):
        self.invoice = int(time.strftime('%H%M%S'))+int(time.strftime('%d%m%Y'))
        bill_top_temp =f'''
\t\tThz-Inventory
\t Phone No. 7626*****, Magway-04011
{str('='*45)}
 Customer Name : {self.var_cname.get()}
 Ph no : {self.var_contact.get()}
 Bill no : {str(self.invoice)}\t\t\tDate: {str(time.strftime('%d/%m/%Y'))}
{str('='*45)}
 Product Name\t\t  Quantity\t\tPrice
{str('='*45)}         
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str('='*45)}  
 Bill Amount\t\t\t\tKs {self.bill_amt}
 Discount\t\t\t\tKs {self.discount}
 Net Pay\t\t\t\tKs {self.net_pay}
{str('='*45)}\n
 Total Payment\t\t\t\tKs {self.net_pay}  
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                quantity=int(row[4])-int(row[3])
                if int(quantity)==int(row[4]):
                    status='Inactive'
                else:
                    status='Active'
                
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,'\n'+name+'\t\t\t'+row[3]+'\tKs '+price)

                mycursor.execute('UPDATE product SET quantity=%s,status=%s WHERE pid=%s',(
                                    quantity,
                                    status,
                                    pid
                                    ))
                db.commit()
            db.close()
            self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)
        

    def clear_cart(self):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(''),
        self.var_name.set(''),
        self.var_price.set(''),
        self.lbl_instock.config(text="In Stock")
        self.var_stock.set('')
        self.var_quantity.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.clear_cart()
        self.show()
        self.show_cart
        self.cartTitle.config(text='Total Product [0]')
        self.chk_print=0

    def update_date_time(self):
        time_=time.strftime('%I:%M:%S')
        date_=time.strftime('%d-%m-%Y')

        self.lbl_clock.config(text=f'Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}')
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print','Please wait while printing',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print','Please Generate bill,to print the receipt',parent=self.root)


            messagebox.showerror("Print",'Generate bill ,to print the receipt',parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system('python C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\login.py')
           


    





if __name__=='__main__':
    root = Tk()
    obj = billing(root)
    root.mainloop()