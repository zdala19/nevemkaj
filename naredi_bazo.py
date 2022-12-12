import sqlite3 

db = sqlite3.connect("baza.db") #naredimo novv bazo db

with db as cursor:
    #to naredi transakcijo
    #ustvarili smo tabelo user kjer so emaili in imena
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS
                   user (uid INTEGER PRIMARY KEY,
                   email TEXT,
                   name TEXT)""")
    pass

#dodamo ljudi 1.način
folk = [
    ("abc@gmail.com", "ime1"),
    ("abc@gmail1.com", "ime2"),
    ("abc@gmail2.com", "ime3"),
    ("abc@gmail3.com", "ime4")
]

#with db as crusor:
#    for (email, name) in folk:
#        cursor.execute("""
#                       INSERT INTO user (email, name) 
#                         VALUES (?,?)""", (email, name))
#        pass 

#dodamo ljudi 2.način 

def napolni_uporabnike():
    with db as cursor:
        for (email, name) in folk:
            cursor.execute("""
                        INSERT INTO user (email, name) 
                            VALUES (:now_email, :user_name)""", {"now_email":email, "user_name":name})
            pass 

with db as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    print(cursor.fetchall()) #fetchall nam da vse ali fetchmany - skoraj isto
    cursor.execute("SELECT COUNT(*) FROM user")
    print(cursor.fetchone()) #fetchone vrne eno stvar in se pritoži, če želimo, da nam jih vrne več 
    pass