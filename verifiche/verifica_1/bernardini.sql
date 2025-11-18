-- database: ./esercizi_5M/bernardini.sqlite

-- Use the ▷ button in the top right corner to run the entire file.

CREATE TABLE Prodotto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    prezzo REAL
);

CREATE TABLE Ordine (
    id INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    cliente_nome TEXT
);

CREATE TABLE OrdineProdotto (
    id INTEGER PRIMARY KEY,
    ordine_id INTEGER,
    prodotto_id INTEGER,
    quantita INTEGER,
    FOREIGN KEY (ordine_id) REFERENCES Ordine(id),
    FOREIGN KEY (prodotto_id) REFERENCES Prodotto(id)
);

INSERT INTO Prodotto (id, nome, prezzo) VALUES 
(1, 'Notebook', 12.5),
(2, 'Penna a sfera', 1.2),
(3, 'Zaino', 28.0),
(4, 'Agenda', 7.5),
(5, 'Quaderno', 5.0);

INSERT INTO Ordine (id, data, cliente_nome) VALUES
(1, '2025-10-01', 'Anna Verdi'),
(2, '2025-10-02', 'Marco Neri'),
(3, '2025-10-03', 'Anna Verdi');

INSERT INTO OrdineProdotto (id, ordine_id, prodotto_id, quantita) VALUES
(1, 1, 1, 2),
(2, 1, 2, 5),
(3, 2, 3, 1),
(4, 3, 4, 2),
(5, 3, 2, 3);

--Query 1
SELECT *
FROM Prodotto
WHERE prezzo < 10;

--Query 2
SELECT *
FROM Prodotto
ORDER BY nome ASC;

-- Query 3
SELECT cliente_nome, COUNT(*) AS num_ordini
FROM Ordine
GROUP BY cliente_nome;

--Query 4
SELECT avg(prezzo) AS prezzo_medio
FROM Prodotto;

-- Query 5
SELECT OrdineProdotto.prodotto_id, OrdineProdotto.quantita AS quantita_venduta
FROM OrdineProdotto
JOIN Prodotto
ON OrdineProdotto.prodotto_id = Prodotto.id
GROUP BY Prodotto.nome;

--Query 6
SELECT OrdineProdotto.prodotto_id, OrdineProdotto.quantita AS quantita_venduta
FROM OrdineProdotto
LEFT JOIN Prodotto
ON OrdineProdotto.prodotto_id = Prodotto.id
GROUP BY Prodotto.nome;