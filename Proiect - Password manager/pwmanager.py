import sqlite3
import sys

import cryptocode

parola_master = 'ionela2002'


# Functie pentru verificarea parolei master
def verificare_parola(parola_introdusa_de_utilizaor):
    if parola_master != parola_introdusa_de_utilizaor:
        print("Parola master introdusa este incorecta!")
        return False
    return True


# Functie pentru criptarea parolei
def criptare_parola(parola):
    parola_criptata = cryptocode.encrypt(parola, parola_master)
    return parola_criptata


# Functie pentru decriptarea parolei
def decriptare_parola(parola_criptata):
    parola_decriptata = cryptocode.decrypt(parola_criptata, parola_master)
    return parola_decriptata


# Functie pentru adaugarea unei noi parole
def adaugare_parola(website, username, parola, cursor):
    cursor.execute("SELECT * FROM parole WHERE website=?", (website,))
    entry = cursor.fetchone()

    if entry:
        # Actualizare parola
        parola_criptata = criptare_parola(parola)
        cursor.execute("UPDATE parole SET username=?, parola=? WHERE website=?", (username, parola_criptata, website))
        print(f"Username-ul si parola pentru website-ul {website} au fost updatate cu succes!")
    else:
        # Adaugare parola noua
        parola_criptata = criptare_parola(parola)
        cursor.execute('INSERT INTO parole (website, username, parola) VALUES(?,?,?)',
                       (website, username, parola_criptata,))
        print(f"Username-ul si parola pentru website-ul {website} au fost adaugate cu succes!")


# Functie pentru obtinerea unei parole
def obtinere_parola(website, cursor):
    cursor.execute("SELECT * FROM parole WHERE website=?", (website,))
    entry = cursor.fetchone()

    if entry:
        parola_decriptata = decriptare_parola(entry[3])
        print(f"Parola pentru website-ul {website} este {parola_decriptata}")
    else:
        print(f"Nu exista o parola pentru {website}")


# Functie pentru stergerea unei parole
def stergere_parola(website, cursor):
    cursor.execute("SELECT * FROM parole WHERE website=?", (website,))
    entry = cursor.fetchone()

    if entry:
        cursor.execute("DELETE FROM parole WHERE website=?", (website,))
        print(f"Parola pentru website-ul {website} a fost stearsa cu succes!")
    else:
        print(f"Nu exista o parola pentru {website}")


# Functie pentru listarea tuturor parolelor
def listare_parole(cursor):
    cursor.execute("SELECT * FROM parole")
    entries = cursor.fetchall()

    if entries:
        print("Parolele stocate:")
        for entry in entries:
            id, website, username, parola_criptata = entry
            parola_decriptata = decriptare_parola(parola_criptata)
            print(f" Website-ul {website} are username-ul {username} si parola {parola_decriptata}")
    else:
        print("Nu exista parole stocate.")


# Functie pentru conectarea la baza de date
def conectare_la_baza_de_date():
    conn = sqlite3.connect('pwmanager.db')
    cursor = conn.cursor()

    query = '''
                CREATE TABLE IF NOT EXISTS parole (
                    id INTEGER PRIMARY KEY,
                    website TEXT,
                    username TEXT,
                    parola TEXT
                )
            '''
    cursor.execute(query)
    return conn, cursor


def main():
    parola_introdusa_de_utilizator = sys.argv[1]
    operatie = sys.argv[2]

    if verificare_parola(parola_introdusa_de_utilizator) == False:
        return False

    conn, cursor = conectare_la_baza_de_date()

    # Executare operatii în functie de argumentele primite
    if operatie == '-add':
        website, username, parola = sys.argv[3:]
        adaugare_parola(website, username, parola, cursor)
        conn.commit()
        conn.close()

    elif operatie == '-get':
        website = sys.argv[3]
        obtinere_parola(website, cursor)
        conn.commit()
        conn.close()

    elif operatie == '-remove':
        website = sys.argv[3]
        stergere_parola(website, cursor)
        conn.commit()
        conn.close()

    elif operatie == '-list':
        listare_parole(cursor)
        conn.commit()
        conn.close()

    else:
        print("Comanda invalida. Vezi instructiunile de utilizare.")
        conn.close()


if __name__ == "__main__":
    main()
