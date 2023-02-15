import sqlite3
from sqlite_utils import Database

class Storage():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.create_db_tables()
        
        
    def create_db_tables(self):
        try:
            cur = self.conn.cursor()
            user_table = ("""
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """)
            products_table = (""" 
            CREATE TABLE IF NOT EXISTS products(
                title TEXT NOT NULL,
                price INTEGER NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                createdBy TEXT,
                slug TEXT
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
            self.conn.close()


    def register_user(self, username, password, email):
        #inserted_user = {}
            cur = self.conn.cursor()
            # name = input('Username:')
            # password = input('Password:') 
            # email = input('Email:')
            cur.execute('INSERT INTO users (username, password, email VAUES (?, ?, ?))',
            (username, password, email))
            self.conn.commit()
            #cur.close()

        

    # def update_user():
    #     return update_user

    # def delete_user():
    #     return delete_user

    # def create_products():
    #     return create_products

    # def update_product():
    #     return update_product

    # def delete_products():
    #     return delete_products