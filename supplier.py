from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector
class SupplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x520+220+130')
        self.root.title("Inventory Management System | Suppliers")
        self.root.config(bg='white')
        self.root.focus_force()
        #===========================================
        #All variables=========
        self.var_sup_searchtext = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_sup_name = StringVar()
        self.var_sup_contact = StringVar()
        
        

        #list in search (option)
        lbl_search =Label(self.root,text='Invoice No.', font=('goudy old style',15,'bold'))
        lbl_search.place(x=680,y=80, width=100)
        
        txt_search = Entry(self.root,textvariable=self.var_sup_searchtext,font=('goudy old style',15),bg='lightyellow')
        txt_search.place(x=800,y=80, width=150,height=30)
        txt_but = Button(self.root,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',fg='white')
        txt_but.place(x=960,y=80,width=100,height=30)

        #title
        title = Label(self.root,text='Supplier Details',font=('goudy old style',20),bg='#0f4d7d',fg='white')
        title.place(x=50,y=10,width=1000, height=40)

        #content

        #row 1
        lbl_supplier_invoice = Label(self.root,text='Invoice',font=('goudy old style',15),bg='white')
        lbl_supplier_invoice.place(x=50,y=80)
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice,font=('goudy old style',15),bg='white')
        txt_supplier_invoice.place(x=180,y=80)

        lbl_name = Label(self.root,text='Name',font=('goudy old style',15),bg='white')
        lbl_name.place(x=50,y=130)
        lbl_name = Entry(self.root,textvariable=self.var_sup_name,font=('goudy old style',15),bg='white')
        lbl_name.place(x=180,y=130)

        lbl_contact = Label(self.root,text='Contact',font=('goudy old style',15),bg='white')
        lbl_contact.place(x=50,y=180)
        txt_contact = Entry(self.root,textvariable=self.var_sup_contact,font=('goudy old style',15),bg='white')
        txt_contact.place(x=180,y=180)

        lbl_desc = Label(self.root,text='Description',font=('goudy old style',15),bg='white')
        lbl_desc.place(x=50,y=230)
        self.txt_desc = Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txt_desc.place(x=180,y=230,width=470,height=100)
 

        #save button
        save_but = Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white',cursor='hand2')
        save_but.place(x=180,y=335,width=110,height=28)
        update_but = Button(self.root,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2')
        update_but.place(x=300,y=335,width=110,height=28)
        clear_but = Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#f44336',fg='white',cursor='hand2')
        clear_but.place(x=420,y=335,width=110,height=28)
        delete_but = Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#607d8b',fg='white',cursor='hand2')
        delete_but.place(x=540,y=335,width=110,height=28)


        #Supplier Details======

        sup_frame = Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=680,y=120,width=380,height=350)

        scrolly = Scrollbar(sup_frame,orient=VERTICAL)
        scrollx = Scrollbar(sup_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(sup_frame,columns=('invoice','name','contact','description'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)


        self.supplierTable.heading('invoice',text='Invoice')
        self.supplierTable.heading('name',text='Name')
        self.supplierTable.heading('contact',text='Contact')
        self.supplierTable.heading('description',text='Description')

        self.supplierTable['show'] = 'headings'

        self.supplierTable.column('invoice', width=90)
        self.supplierTable.column('name',width=100)
        self.supplierTable.column('contact',width=100)
        self.supplierTable.column('description',width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind('<ButtonRelease-1>',self.get_data)

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
            if self.var_sup_invoice.get() == '':
                messagebox.showerror('Error','Invoice No. must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM supplier WHERE invoice=%s ",(self.var_sup_invoice.get(),))
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror('Error','This Invoice Number already assinged, try different ID')
                else:
                    mycursor.execute('INSERT INTO supplier (invoice,name,contact,description) VALUES(%s,%s,%s,%s)',(    
                                        self.var_sup_invoice.get(),
                                        self.var_sup_name.get(),
                                        self.var_sup_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        ))
                    db.commit()
                    messagebox.showinfo('Success','Supplier Added Successfully',parent=self.root)
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
            mycursor.execute('SELECT * FROM supplier')
            rows = mycursor.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_sup_name.set(row[1]),
        self.var_sup_contact.set(row[2]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),
        

    def update(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.var_sup_invoice.get() == '':
                messagebox.showerror('Error',' Invoice Number must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM supplier WHERE invoice=%s ",(self.var_sup_invoice.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Invoice Number',parent=self.root)
                else:
                    mycursor.execute('UPDATE supplier SET name=%s,contact=%s,description=%s WHERE invoice=%s',(    
                                        self.var_sup_name.get(),
                                        self.var_sup_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_sup_invoice.get()
                                        ))
                    db.commit()
                    messagebox.showinfo('Success','Supplier Updated Successfully',parent=self.root)
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
            if self.var_sup_invoice.get() == '':
                messagebox.showerror('Error','Invoice Number must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM supplier WHERE invoice=%s ",(self.var_sup_invoice.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Invoice Number',parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm",'Do u really want to delete?',parent=self.root)
                    if op == True:
                        mycursor.execute("DELETE FROM supplier WHERE invoice=%s ",(self.var_sup_invoice.get(),))
                        db.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Sucessfully",parent=self.root)
                        self.clear()
            
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set(''),
        self.var_sup_name.set(''),
        self.var_sup_contact.set(''),
        self.txt_desc.delete('1.0',END),
        self.var_sup_searchtext.set(''),
        self.var_sup_searchby.set('Select')
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
            if self.var_sup_searchtext.get() == '':
                messagebox.showerror("Error",'Search input should be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM supplier WHERE invoice = '%"+self.var_sup_searchtext.get()+"%'")
                rows = mycursor.fetchall()
                if len(rows) != 0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)



        


if __name__=='__main__':
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()