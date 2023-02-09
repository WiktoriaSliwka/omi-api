import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_tables():
    try:
        conn = connect_to_db()
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
        conn.execute(user_table)
        conn.commit()
        print("User table created")
        conn.execute(products_table)
        conn.commit()
        print("product table created")
    except:
        print("Tables creation failed")
    finally:
        conn.close()


def add_user():
    #inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        name = input('Username:')
        password = input('Password:') 
        email = input('Email:')
        cur.execute("""INSERT INTO users (username, password, email VAUES (? ? ?))""",
        (name, password, email))
        conn.commit()
    except: 
        conn.rollback()
    finally:
        conn.close()

    return cur.lastrowid

def update_user():
    return update_user

def delete_user():
    return delete_user

def create_products():
    return create_products

def update_product():
    return update_product

def delete_products():
    return delete_products