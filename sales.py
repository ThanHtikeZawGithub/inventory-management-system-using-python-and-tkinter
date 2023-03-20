from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import os



class SaleClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x520+220+130')
        self.root.title("Inventory Management System | Suppliers")
        self.root.config(bg='white')
        self.root.focus_force()

        self.bill_list = []

        self.var_invoice=StringVar()

        title = Label(self.root,text='View Customer Bills',font=('goudy old style',20),bg='#0f4d7d',fg='white')
        title.pack(side=TOP, fill=X, padx=10,pady=2)

        lbl_sale_invoice = Label(self.root,text='Invoice No.',font=('goudy old style',15),bg='white')
        lbl_sale_invoice.place(x=50,y=80)
        txt_sale_invoice = Entry(self.root,textvariable=self.var_invoice,font=('goudy old style',15),bg='lightyellow')
        txt_sale_invoice.place(x=180,y=80,height=30)

        search_but = Button(self.root,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',fg='white')
        search_but.place(x=400,y=80,width=100,height=30)

        clear_but = Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#33bbf9',fg='white')
        clear_but.place(x=520,y=80,width=100,height=30)

        sale_frame = Frame(self.root,bd=3,relief=RIDGE)
        sale_frame.place(x=50,y=120,width=220,height=350)

        scrolly = Scrollbar(sale_frame,orient=VERTICAL)
        self.sale_list = Listbox(sale_frame,font=('goudy old style',15),bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command= self.sale_list.yview)
        self.sale_list.pack(fill=BOTH,expand=1)
        self.sale_list.bind('<ButtonRelease-1>',self.get_data)
#====Bill Area================
        bill_frame = Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=300,y=120,width=390,height=350)

        title2 = Label(bill_frame,text='Customer Bill Area',font=('goudy old style',15),bg='orange')
        title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area = Text(bill_frame ,bg='lightyellow',yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command= self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        self.billPhoto = Image.open('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\images\\mancity.PNG')
        self.billPhoto = self.billPhoto.resize((300,300),Image.ANTIALIAS)
        self.billPhoto = ImageTk.PhotoImage(self.billPhoto)
        lbl_image = Label(self.root,image=self.billPhoto)
        lbl_image.place(x=750,y=120)

        self.show()

    def show(self):
        del self.bill_list[:]
        self.sale_list.delete(0,END)
        for i in os.listdir('C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\bill'):
            if i.split('.')[-1]=='txt':    #bill1.txt <---- txt
                self.sale_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self,ev):
        index_ = self.sale_list.curselection()
        file_name = self.sale_list.get(index_)
        print(file_name)
        fp = open(f'C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=='':
            messagebox.showerror('Error','Invoice No. should be required',parent=self.root)
        else:
            # print(self.bill_list,self.var_invoice.get())
            if self.var_invoice.get() in self.bill_list:
                fp=open(f"C:\\Users\\ZarMaNi\\Desktop\\python\\IMS\\bill/{self.var_invoice.get()}.txt",'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)


if __name__=='__main__':
    root = Tk()
    obj = SaleClass(root)
    root.mainloop()