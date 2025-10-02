import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

try:
    # Eseguo DDL per creare la tabella se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Esami (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricola INTEGER NOT NULL,
            corso TEXT NOT NULL,
            voto INTEGER,
            FOREIGN KEY (matricola) REFERENCES Studenti(Matricola)
        )
    """)
            

    # 4. Esecuzione Query DML (parametrizzata)
    # Il segnaposto per SQLite è '?'
    cursor.executemany(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        [(101, 'Mario', 'Rossi'),
        (102, 'Luca', 'Bianchi')]
    )

    cursor.executemany(
        "INSERT INTO Esami (matricola, corso, voto) VALUES (?, ?, ?)",
        [(101,'Matematica', 28),
         (102,"Informatica", 30),
         (101,"Fisica", 27)]
    )

    # 5. Conferma delle modifiche
    conn.commit()

    cursor.execute("SELECT Matricola, Nome, Cognome FROM Studenti")
    studenti = cursor.fetchall()
    print("Elenco studenti:")
    for s in studenti:
        print(s)

    cursor.execute("SELECT corso, voto FROM Esami WHERE matricola = ?", (101,))
    esami_101 = cursor.fetchall()
    print("\nEsami sostenuti da studente 101:")
    for e in esami_101:
        print(e)

    cursor.execute("""
        SELECT Studenti.Matricola, Studenti.Nome, Studenti.Cognome, COUNT(Esami.id) as num_esami
        FROM Studenti
        LEFT JOIN Esami ON Studenti.Matricola = Esami.matricola
        GROUP BY Studenti.Matricola
    """)
    esami_per_studente = cursor.fetchall()
    print("\nNumero di esami sostenuti per ciascuno studente:")
    for r in esami_per_studente:
        print(r)

finally:
    # 6. Chiusura Connessione
    conn.close()