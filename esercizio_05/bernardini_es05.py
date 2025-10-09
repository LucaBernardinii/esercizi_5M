import sqlite3

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


def query_libri_per_autore(autore_id):
    pass

def query_prestiti_per_utente(utente):
    pass

def query_libri_per_genere():
    pass

def query_autori_con_piu_libri():
    pass

def query_prestiti_non_restituiti():
    pass

if __name__ == "__main__":
    create_tables()
    insert_data()