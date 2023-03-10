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


def get_restaurant_details(conn, name):
    try:
        c = conn.cursor()
        c.execute(f"SELECT * FROM Restaurants WHERE Name = '{name}'")
        restaurant = c.fetchone()
        c.execute(f"SELECT * FROM Revenue WHERE Name = '{name}'")
        revenue = c.fetchone()
        if restaurant and revenue:
            print(f"Details for {name}:")
            print(f"Name: {restaurant[0]}")
            print(f"Brand: {restaurant[1]}")
            print(f"Address: {restaurant[2]}")
            print(f"Owner: {restaurant[3]}")
            print(f"Quarter1 Revenue: {revenue[1]}")
            print(f"Quarter2 Revenue: {revenue[2]}")
            print(f"Total Revenue: {revenue[3]}")
        else:
            print(f"No details found for {name}")
    except sqlite3.Error as e:
        print(f"Error getting details for {name}: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    get_restaurant_details(conn, "BK120")
    conn.close()

#zmieniam wlasciciela restuarcji, operacji modyfikacja recordu

def modify_restaurant_owner(conn, name, new_owner):
    try:
        c = conn.cursor()
        c.execute(f"UPDATE Restaurants SET Owner = '{new_owner}' WHERE Name = '{name}'")
        conn.commit()
        print(f"{c.rowcount} record(s) updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating record for {name}: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    modify_restaurant_owner(conn, "BK120", "Johny Walker")
    conn.close()

#usuwam record oodnosnie wybranej restauracji

def delete_restaurant(conn, name):
    try:
        c = conn.cursor()
        c.execute(f"DELETE FROM Restaurants WHERE Name = '{name}'")
        conn.commit()
        print(f"{c.rowcount} record(s) deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting records for {name}: {e}")

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    delete_restaurant(conn, "Mc130")
    conn.close()