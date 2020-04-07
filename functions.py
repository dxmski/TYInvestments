import sqlite3
import datetime as dt
import os
from sqlite3 import Error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "money.db")

conn = sqlite3.connect(db_path)

def create_table():
    try:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS money(
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            amount FLOAT NOT NULL,
            date_of_payment TEXT NOT NULL
        ); """)
        cur.close()
        print ("Table created successfully")
    except Error as e:
        print (e)
        
def insert_table():
    try:
        money = input('How much have you been paid? ')
        date_of_payment = input('When was the money sent? e.g \
            01/02/03 ')
        cur = conn.cursor()
        cur.execute("""INSERT INTO money(date, amount, date_of_payment)\
            VALUES (?, ?, ?)""", (dt.datetime.now().strftime("%x"),\
                 money, date_of_payment))
        conn.commit()
        conn.close()
        print ("Data inserted successfully")
    except Error as e:
        print (e)

def view_table():
    cur = conn.cursor()
    try:
        print("Printing all data from money.db")
        for row in cur.execute(""" SELECT * FROM `money`; """):
            print(row)       
    except Error as e:
        print(e)



















banner = r"""
 /$$$$$$$$/$$     /$$       /$$$$$$                                      /$$                                     /$$                  
|__  $$__|  $$   /$$/      |_  $$_/                                     | $$                                    | $$                  
   | $$   \  $$ /$$/         | $$  /$$$$$$$ /$$    /$$/$$$$$$  /$$$$$$$/$$$$$$  /$$$$$$/$$$$  /$$$$$$ /$$$$$$$ /$$$$$$  /$$$$$$$      
   | $$    \  $$$$/          | $$ | $$__  $|  $$  /$$/$$__  $$/$$_____|_  $$_/ | $$_  $$_  $$/$$__  $| $$__  $|_  $$_/ /$$_____/      
   | $$     \  $$/           | $$ | $$  \ $$\  $$/$$| $$$$$$$|  $$$$$$  | $$   | $$ \ $$ \ $| $$$$$$$| $$  \ $$ | $$  |  $$$$$$       
   | $$      | $$            | $$ | $$  | $$ \  $$$/| $$_____/\____  $$ | $$ /$| $$ | $$ | $| $$_____| $$  | $$ | $$ /$\____  $$      
   | $$      | $$           /$$$$$| $$  | $$  \  $/ |  $$$$$$$/$$$$$$$/ |  $$$$| $$ | $$ | $|  $$$$$$| $$  | $$ |  $$$$/$$$$$$$/      
   |__/      |__/          |______|__/  |__/   \_/   \_______|_______/   \___/ |__/ |__/ |__/\_______|__/  |__/  \___/|_______/       
 /$$$$$$$$                     /$$                /$$$$$$$$                       /$$                                                 
| $$_____/                    | $$               |__  $$__/                      | $$                                                 
| $$   /$$   /$$/$$$$$$$  /$$$$$$$ /$$$$$$$         | $$ /$$$$$$ /$$$$$$  /$$$$$$| $$   /$$ /$$$$$$  /$$$$$$                          
| $$$$| $$  | $| $$__  $$/$$__  $$/$$_____/         | $$/$$__  $|____  $$/$$_____| $$  /$$//$$__  $$/$$__  $$                         
| $$__| $$  | $| $$  \ $| $$  | $|  $$$$$$          | $| $$  \__//$$$$$$| $$     | $$$$$$/| $$$$$$$| $$  \__/                         
| $$  | $$  | $| $$  | $| $$  | $$\____  $$         | $| $$     /$$__  $| $$     | $$_  $$| $$_____| $$                               
| $$  |  $$$$$$| $$  | $|  $$$$$$$/$$$$$$$/         | $| $$    |  $$$$$$|  $$$$$$| $$ \  $|  $$$$$$| $$                               
|__/   \______/|__/  |__/\_______|_______/          |__|__/     \_______/\_______|__/  \__/\_______|__/      

"""
