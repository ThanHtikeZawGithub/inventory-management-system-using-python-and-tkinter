from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector



class category:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x520+220+130')
        self.root.title("Inventory Management System | Suppliers")
        self.root.config(bg='white')
        self.root.focus_force()

        #================variables========
        self.category_id = StringVar()
        self.name = StringVar()

        lbl_title=Label(self.root,text='Manage Product Category',font=('goudy old style',30),bg='#184a45',fg='white',bd=3,relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10,pady=2)

        lbl_name=Label(self.root,text='Enter Category Name',font=('goudy old style',30),bg='white')
        lbl_name.place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.name,font=('goudy old style',18),bg='lightyellow')
        txt_name.place(x=50,y=170,width=300)

        btn_add=Button(self.root,text='Add',command=self.add,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2')
        btn_add.place(x=360,y=170,width=150,height=30)

        btn_del=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='red',fg='white',cursor='hand2')
        btn_del.place(x=520,y=170,width=150,height=30)



        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=680,y=100,width=380,height=100)

        scrolly = Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)

        self.catTable=ttk.Treeview(cat_frame,columns=('cid','name'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.catTable.xview)
        scrolly.config(command=self.catTable.yview)


        self.catTable.heading('cid',text='C ID')
        self.catTable.heading('name',text='Name')
        

        self.catTable['show'] = 'headings'

        self.catTable.column('cid', width=90)
        self.catTable.column('name',width=100)
        self.catTable.pack(fill=BOTH,expand=1)
        self.catTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()

        #===images========

        self.image1 = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\chicken.PNG')
        self.image1 = self.image1.resize((300,300),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.image1)

        self.lbl_image1 = Label(self.root,image=self.image1)
        self.lbl_image1.place(x=50,y=220)

        self.image2 = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\burger.PNG')
        self.image2 = self.image2.resize((300,300))
        self.image2 = ImageTk.PhotoImage(self.image2)

        self.lbl_image2 = Label(self.root,image=self.image2)
        self.lbl_image2.place(x=580,y=220)

        #=======fucntions===============

    def add(self):
        db = mysql.connector.connect(
                host ='localhost',
                user = 'root',
                passwd = 'Thanhtikezaw1998@',
                database = 'ims'
                )
        mycursor = db.cursor()
        try:
            if self.name.get() == '':
                messagebox.showerror('Error','Category name must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM category WHERE name=%s ",(self.name.get(),))
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror('Error','Category already present, try different one')
                else:
                    mycursor.execute('INSERT INTO category (name) VALUES(%s)',(self.name.get(),))  
                    db.commit()
                    messagebox.showinfo('Success','Category Added Successfully',parent=self.root)
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
            mycursor.execute('SELECT * FROM category')
            rows = mycursor.fetchall()
            self.catTable.delete(*self.catTable.get_children())
            for row in rows:
                self.catTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)

    
    def get_data(self):
        f = self.catTable.focus()
        content = (self.catTable.item(f))
        row = content['values']
        # print(row)
        self.category_id.set(row[0]),
        self.name.set(row[1])
        self.show()

    def delete(self):
        db = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = 'Thanhtikezaw1998@',
            database = 'ims'
            )
        mycursor = db.cursor()
        try:
            if self.name.get() == '':
                messagebox.showerror('Error','Category name must be required',parent=self.root)
            else:
                mycursor.execute("SELECT * FROM category WHERE name=%s ",(self.name.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error','Invalid Category Name',parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm",'Do u really want to delete?',parent=self.root)
                    if op == True:
                        mycursor.execute("DELETE FROM category WHERE name=%s ",(self.name.get(),))
                        db.commit()
                        messagebox.showinfo("Delete","Category Deleted Sucessfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.category_id.set(''),
        self.name.set('')
        self.show()
        
            
if __name__=='__main__':
    root = Tk()
    obj = category(root)
    root.mainloop()