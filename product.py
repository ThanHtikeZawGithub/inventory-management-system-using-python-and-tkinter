from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class products:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x520+220+130')
        self.root.title("Inventory Management System | Products")
        self.root.config(bg='white')
        self.root.focus_force()

        self.var_p_searchby = StringVar()
        self.var_p_searchtext = StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stat = StringVar()


        SearchFrame= LabelFrame(self.root,text='Search Employee',bg='white')
        SearchFrame.place(x=480,y=15,width=600, height=70)
 
        #list in search (option)
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_p_searchby, values=('Select','Category','Supplier','Name','Price','Quantity'),state='randomly', justify=CENTER, font=('goudy old style',15,'bold'))
        cmb_search.place(x=10,y=10, width=180) 
        cmb_search.current(0)

        txt_search = Entry(SearchFrame,textvariable=self.var_p_searchtext,font=('goudy old style',15),bg='lightyellow')
        txt_search.place(x=200,y=10)
        txt_but = Button(SearchFrame,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',fg='white')
        txt_but.place(x=410,y=10,width=150,height=30)

        title = Label(self.root,text='Manage Product Details',font=('goudy old style',15),bg='#0f4d7d',fg='white')
        title.place(x=10,y=10,width=450)

        DetailFrame= LabelFrame(self.root,bg='white')
        DetailFrame.place(x=10,y=38,width=451,height=450)
#=============variables location================
        lbl_cat = Label(self.root,text='Category',font=('goudy old style',20),bg='white')
        lbl_cat.place(x=30,y=70)
        cmb_cat = ttk.Combobox(self.root,textvariable=self.var_cat,values=self.cat_list,font=('goudy old style',15,'bold'))
        cmb_cat.place(x=180,y=75,width=200)
        cmb_cat.current(0)

        lbl_sup = Label(self.root,text='Supplier',font=('goudy old style',20),bg='white')
        lbl_sup.place(x=30,y=120)
        cmb_sup = ttk.Combobox(self.root,textvariable=self.var_sup,values=self.sup_list,font=('goudy old style',15,'bold'))
        cmb_sup.place(x=180,y=125,width=200)
        cmb_sup.current(0)

        lbl_name = Label(self.root,text='Name',font=('goudy old style',20),bg='white')
        lbl_name.place(x=30,y=170)
        lbl_name = Entry(self.root,textvariable=self.var_pname,font=('goudy old style',15),bg='lightyellow')
        lbl_name.place(x=180,y=175)

        lbl_price = Label(self.root,text='Price',font=('goudy old style',20),bg='white')
        lbl_price.place(x=30,y=230)
        lbl_price = Entry(self.root,textvariable=self.var_price,font=('goudy old style',15),bg='lightyellow')
        lbl_price.place(x=180,y=235)

        lbl_qty = Label(self.root,text='Quantity',font=('goudy old style',20),bg='white')
        lbl_qty.place(x=30,y=280)
        lbl_qty = Entry(self.root,textvariable=self.var_qty,font=('goudy old style',15),bg='lightyellow')
        lbl_qty.place(x=180,y=285)

        lbl_stat = Label(self.root,text='Status',font=('goudy old style',20),bg='white')
        lbl_stat.place(x=30,y=330)
        cmb_stat = ttk.Combobox(self.root,textvariable=self.var_stat,values=('Select','Active','Inactive'),font=('goudy old style',15,'bold'))
        cmb_stat.place(x=180,y=335,width=200)
        cmb_stat.current(0)

        save_but = Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white',cursor='hand2')
        save_but.place(x=15,y=400,width=90,height=30)
        update_but = Button(self.root,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2')
        update_but.place(x=125,y=400,width=90,height=30)
        clear_but = Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#f44336',fg='white',cursor='hand2')
        clear_but.place(x=245,y=400,width=90,height=30)
        delete_but = Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#607d8b',fg='white',cursor='hand2')
        delete_but.place(x=355,y=400,width=90,height=30)


        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=110,width=600,height=378)

        scrolly = Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame,orient=HORIZONTAL)

        self.pTable=ttk.Treeview(p_frame,columns=('pid','category','supplier','name','price','quantity','status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.pTable.xview)
        scrolly.config(command=self.pTable.yview)


        self.pTable.heading('pid',text='P ID')
        self.pTable.heading('category',text='Category')
        self.pTable.heading('supplier',text='Supplier')
        self.pTable.heading('name',text='Name')
        self.pTable.heading('price',text='Price')
        self.pTable.heading('quantity',text='Quantity')
        self.pTable.heading('status',text='Status')
        

        self.pTable['show'] = 'headings'

        self.pTable.column('pid', width=90)
        self.pTable.column('category',width=100)
        self.pTable.column('supplier',width=100)
        self.pTable.column('name',width=100)
        self.pTable.column('price',width=100)
        self.pTable.column('quantity',width=100)
        self.pTable.column('status',width=100)
        self.pTable.pack(fill=BOTH,expand=1)
        self.pTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()

    def fetch_cat_sup(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        self.cat_list.append('Empty')
        self.sup_list.append('Empty')
        try:
            mycursor.execute('SELECT name FROM category ')
            cat = mycursor.fetchall()
            if len(cat) >0:
                del self.cat_list[:]
                self.cat_list.append('Select')
                for i in cat:
                    self.cat_list.append(i[0])
            mycursor.execute('SELECT name from supplier')
            sup=mycursor.fetchall()
            if len(sup) >0:
                del self.sup_list[:]
                self.sup_list.append('Select')
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)



    def add(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_cat.get() == 'Empty' or self.var_sup.get()=='Select' or self.var_pname.get()=='':
                messagebox.showerror('Error','All Field must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM product WHERE name=%s ",(self.var_pname.get(),))
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror('Error','Product already assinged, try different ID')
                else:
                    mycursor.execute('INSERT INTO product (category,supplier,name,price,quantity,status) VALUES(%s,%s,%s,%s,%s,%s)',(    
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_pname.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_stat.get(),                     
                                        ))
                    db.commit()
                    messagebox.showinfo('Success','Product Added Successfully',parent=self.root)
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
            mycursor.execute('SELECT * FROM product')
            rows = mycursor.fetchall()
            self.pTable.delete(*self.pTable.get_children())
            for row in rows:
                self.pTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)


    def get_data(self,ev):   # <-------what the fuck is this ===ev====
        f = self.pTable.focus()
        content = (self.pTable.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_pname.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_stat.set(row[6])

    def update(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_pid.get()=='':
                messagebox.showerror('Error','Please select product from list',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM product WHERE pid=%s ",(self.var_pid.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error',"Product doesn't exist",parent=self.root)
                else:
                    mycursor.execute('UPDATE product SET category=%s,supplier=%s,name=%s,price=%s,quantity=%s,status=%s WHERE pid=%s',(    
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_pname.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_stat.get(),
                                        self.var_pid.get()
                                        ))   
                    db.commit()
                    messagebox.showinfo('Success','Product Updated Successfully',parent=self.root)
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
            if self.var_pid.get() == '':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM product WHERE pid=%s ",(self.var_pid.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Employee ID',parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm",'Do u really want to delete?',parent=self.root)
                    if op == True:
                        mycursor.execute("DELETE FROM product WHERE pid=%s",(self.var_pid.get(),))
                        db.commit()
                        messagebox.showinfo("Delete","Product Deleted Sucessfully",parent=self.root)
                        self.clear()
            
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_pid.set(''),
        self.var_cat.set(''),
        self.var_sup.set(''),
        self.var_pname.set(''),
        self.var_price.set(''),
        self.var_qty.set(''),
        self.var_stat.set('')
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
            if self.var_p_searchby.get()=='Select':
                messagebox.showerror('Error','Select Search by Option',parent=self.root)
            elif self.var_p_searchby.get()=='':
                messagebox.showerror("Error",'Search input should be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM product WHERE" + self.var_p_searchby.get() +"LIKE '%"+self.var_p_searchtext.get()+"%'")
                rows = mycursor.fetchall()
                if len(rows) != 0:
                    self.pTable.delete(*self.pTable.get_children())
                    for row in rows:
                        self.pTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)
        

if __name__=='__main__':
    root = Tk()
    obj = products(root)
    root.mainloop() 