import sqlite3

def create_restaurants_table(conn):
    sql = """CREATE TABLE Restaurants (
                Name TEXT,
                Brand TEXT,
                Address TEXT,
                Owner TEXT
            );"""
    try:
        c = conn.cursor()
        c.execute(sql)
        print("Table 'Restaurants' created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_restaurants_table(conn)
    conn.close()

    
def add_restaurant(conn, name, brand, address, owner):
    sql = """INSERT INTO Restaurants (Name, Brand, Address, Owner) VALUES (?, ?, ?, ?);"""
    try:
        c = conn.cursor()
        c.execute(sql, (name, brand, address, owner))
        conn.commit()
        print(f"Record added successfully: {name}, {brand}, {address}, {owner}")
    except sqlite3.Error as e:
        print(f"Error adding record: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    add_restaurant(conn, "BK120", "Burger King", "New York", "Jack Daniels")
    add_restaurant(conn, "Mc130", "McDonald", "Boston", "Cindy Crawford")
    conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    add_restaurant(conn, "BK122", "Burger King", "New Hempshire", "Johny Smith")
    add_restaurant(conn, "Mc133", "McDonald", "Kansas", "Sheryll Pim")
    conn.close()


# adding new table

def create_table_revenue(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE Revenue
                     (Name TEXT PRIMARY KEY,
                      Quarter1Revenue REAL,
                      Quarter2Revenue REAL,
                      Total REAL,
                      FOREIGN KEY(Name) REFERENCES Restaurants(Name))''')
        print("Revenue table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating Revenue table: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_table_revenue(conn)
    conn.close()

def add_revenue(conn, name, q1_rev, q2_rev):
    try:
        c = conn.cursor()
        total = q1_rev + q2_rev
        c.execute("INSERT INTO Revenue (Name, Quarter1Revenue, Quarter2Revenue, Total) VALUES (?, ?, ?, ?)", (name, q1_rev, q2_rev, total))
        conn.commit()
        print(f"Record added to Revenue table for {name}")
    except sqlite3.Error as e:
        print(f"Error adding record to Revenue table: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    add_revenue(conn, "BK120", 12000, 10000)
    conn.close()