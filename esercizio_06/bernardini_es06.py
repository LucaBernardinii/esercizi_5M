import sqlite3
from typing import List, Tuple

def create_tables():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Autori (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                cognome TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Libri (
                id INTEGER PRIMARY KEY,
                titolo TEXT NOT NULL,
                autore_id INTEGER,
                anno INTEGER,
                genere TEXT,
                FOREIGN KEY (autore_id) REFERENCES Autori(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prestiti (
                id INTEGER PRIMARY KEY,
                libro_id INTEGER,
                utente TEXT NOT NULL,
                data_prestito TEXT,
                data_restituzione TEXT,
                FOREIGN KEY (libro_id) REFERENCES Libri(id)
            )
        """)
        conn.commit()

    finally:
        conn.close()

def insert_data():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    try:
        # Inserimento autori
        cursor.executemany(
            "INSERT INTO Autori (id, nome, cognome) VALUES (?, ?, ?)",
            [(1, 'Marco', 'Rossi'),
             (2, 'Lucia', 'Bianchi'),
             (3, 'Alessandro', 'Verdi')]
        )

        # Inserimento libri
        cursor.executemany(
            "INSERT INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
            [(1, 'Il mistero del castello', 1, 2020, 'Giallo'),
             (2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza'),
             (3, 'La cucina italiana', 2, 2019, 'Cucina'),
             (4, 'Storia antica', 3, 2021, 'Storia'),
             (5, 'Romanzo Moderno', 3, 2022, 'Narrativa'),
             (6, 'Il ritorno del castello', 1, 2023, 'Giallo')]
        )

        # Inserimento prestiti
        cursor.executemany(
            "INSERT INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
            [(1, 1, 'Mario Rossi', '2023-10-01', '2023-10-15'),
             (2, 3, 'Luca Bianchi', '2023-10-05', None),
             (3, 2, 'Alessandro Verdi', '2023-10-07', '2023-10-20'),
             (4, 5, 'Mario Rossi', '2023-10-10', None)]
        )

        conn.commit()

    finally:
        conn.close()


def elenco_libri():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN)"""
    cursor.execute("""
        SELECT Libri.titolo, Libri.anno, Autori.nome, Autori.cognome
        From Libri
        JOIN Autori ON Libri.autore_id = Autori.id
    """)
    return cursor.fetchall()

def elenco_prestiti():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN)"""
    cursor.execute("""
        SELECT Libri.titolo, Prestiti.utente, Prestiti.data_prestito
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
    """)
    return cursor.fetchall()

def libri_post_2020():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Libri pubblicati dopo il 2020"""
    cursor.execute("""
        SELECT Libri.titolo
        From Libri
        WHERE Libri.anno > 2020
    """)
    return cursor.fetchall()

def prestiti_per_utente():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Numero di prestiti per ciascun utente (usa GROUP BY)"""
    cursor.execute("""
        SELECT Prestiti.utente, COUNT(*) as numero_prestiti
        FROM Prestiti
        GROUP BY Prestiti.utente
    """)
    return cursor.fetchall()

def libri_ordinati_per_genere_e_per_anno():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Libri ordinati per genere e poi per anno (usa ORDER BY multiplo)"""
    cursor.execute("""
        SELECT Libri.titolo, Libri.genere, Libri.anno
        FROM Libri
        ORDER BY Libri.genere, Libri.anno
    """)
    return cursor.fetchall()

def prestiti_restituiti():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Prestiti restituiti (dove data_restituzione non è NULL)"""
    cursor.execute("""
        SELECT Libri.titolo, Prestiti.utente, Prestiti.data_restituzione
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
        WHERE Prestiti.data_restituzione IS NOT NULL
    """)
    return cursor.fetchall()

def autori_e_numero_libri():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    """Autori e numero di libri, inclusi quelli senza libri (usa LEFT JOIN e GROUP BY)"""
    cursor.execute("""
        SELECT Autori.nome, Autori.cognome, COUNT(Libri.id) as numero_libri
        FROM Autori
        LEFT JOIN Libri ON Autori.id = Libri.autore_id
        GROUP BY Autori.id
    """)
    return cursor.fetchall()

if __name__ == "__main__":
    try:
        conn = sqlite3.connect('libreria.db')
        cursor = conn.cursor()
        create_tables()
        insert_data()
        print("Elenco Libri:", elenco_libri())
        print("Elenco Prestiti:", elenco_prestiti())
        print("Libri post 2020:", libri_post_2020())
        print("Prestiti per utente:", prestiti_per_utente())
        print("Libri ordinati per genere e anno:", libri_ordinati_per_genere_e_per_anno())
        print("Prestiti restituiti:", prestiti_restituiti())
        print("Autori e numero di libri:", autori_e_numero_libri())
    finally:
        conn.close()
        print("\nConnessione chiusa.")