import sqlite3

connection = sqlite3.connect('cable.db')
c = connection.cursor()


c.execute('''

        CREATE TABLE cb_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        date_of_birth TEXT,
        permission_level TEXT
        
        
        );
    ''')
    
c.execute('''
        CREATE TABLE user_info(
        info_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        phone_number TEXT,
        address TEXT,
        FOREIGN KEY (user_id) REFERENCES cb_user(id)
        );
        
    ''')
    
c.execute('''
        INSERT INTO cb_user (username, password, first_name, last_name, date_of_birth, permission_level) 
        VALUES ('admin','pword', 'vince','chiodo', '12/16/2005', 'admin'),
        ('user1','pword1','rich','piana', '1/1/95', 'customer'), ('user2', 'pword2', 'paul', 'frank', '2/2/90','customer');
    
    
    ''')

c.execute('''
        INSERT INTO user_info (user_id, phone_number, address) 
        VALUES (1, '1234', 'nyc'),
        (1, '5678', 'philly'), (2, '9999', 'la');
    
    
    ''')

connection.commit()
connection.close()
    
print("Database Created and Seeded")
