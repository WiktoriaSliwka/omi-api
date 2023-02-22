import sqlite3
from settings import *
from flask import jsonify
import requests

class Storage():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.create_db_tables()

    def data():
        r = requests.get("https://api.storerestapi.com/products").json()
        data_dump = r['data']
        
       
        return data_dump
        
    
        
    def create_db_tables(self):
        try:
            cur = self.conn.cursor()
            user_table = ("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """)
            products_table = (""" 
            CREATE TABLE IF NOT EXISTS results(
                id INTEGER NOT NULL,
                title TEXT NOT NULL,
                price INTEGER NOT NULL,
                category TEXT NOT NULL,
                createdBy TEXT,
                createdById TEXT
            )
            """)
            cur.execute(user_table)
            self.conn.commit()
            print("User table created")
            cur.execute(products_table)
            self.conn.commit()
            print("product table created")
        except:
            print("Tables creation failed")
        finally:
            cur.close()


    def register_user(self, username, password, email):
            cur = self.conn.cursor()
            try:
                cur.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
                self.conn.commit()
            except sqlite3.IntegrityError:
                pass
                

                cur.close() 

    def getUsers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT username, password FROM users")
        users = cur.fetchall()
        cur.close()
        return users
       

    def findUser(self, username, password):
        cur = self.conn.cursor()
        try:
            res = cur.execute("SELECT * from users WHERE username = username AND password = password", {'username': username, 'password': password})
            return res.fetchone()
        except sqlite3.IntegrityError:
            pass
        cur.close()
        
   
    def getuserId(self):
        cur = self.conn.cursor()
        try:
            res = cur.execute("SELECT user_id from users")
            return res.fetchone()
        except sqlite3.IntegrityError:
            pass
        cur.close()
            
        



    # def update_user():
    #     return update_user

    # def delete_user():
    #     return delete_user
    

    data = data()
    
    def insert_products(self):
        cur = self.conn.cursor()
        for i in range(len(self.data)):
            try:
                cur.execute('INSERT INTO results (id, title, price, category, createdBy, createdById) VALUES (?,?,?,?,?,?)', (self.data[i]['_id'], self.data[i]['title'], self.data[i]['price'], self.data[i]['category']['name'], self.data[i]['createdBy']['name'], self.data[i]['createdBy']['_id']))
                self.conn.commit()
            except sqlite3.IntegrityError:
                pass
        cur.close()


    #def create_product():
    #    return create_products

    # def update_product():
    #     return update_product

    def delete_products(self, title):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM results where title = ?", (title))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass
            cur.close()
        
    
    
    

   
