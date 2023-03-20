import mysql.connector

def create_db():
    db=mysql.connector.connect(
        host ='localhost',
        user = 'root',
        passwd = 'Thanhtikezaw1998@',
        database = 'ims'
        )
    mycursor = db.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTO_INCREMENT,name text,email text,gender text,contact text,dob text,doj text,passwd text,utype text,address text,salary text)')
    db.commit()

    mycursor.execute('CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTO_INCREMENT,name text, contact text, description text)')
    db.commit()

    mycursor.execute('CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTO_INCREMENT,name text)')
    db.commit()

    mycursor.execute('CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTO_INCREMENT,category text,supplier text, name text, price text,quantity text,status text)')
    db.commit()


create_db()
