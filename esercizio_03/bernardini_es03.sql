-- database: ./bernardini_es03.sqlite

CREATE TABLE APICOLTORE (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE TIPOLOGIA (
    id INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descrizione VARCHAR(100) NOT NULL
);

CREATE TABLE MIELE (
    id INT PRIMARY KEY,
    denominazione VARCHAR(500) NOT NULL,
    id_tipologia INT NOT NULL,
    FOREIGN KEY (id_tipologia) REFERENCES TIPOLOGIA(id)
);

CREATE TABLE APIARIO (
    codice_apiario INT PRIMARY KEY,
    numero_arnie INT NOT NULL,
    localita VARCHAR(500) NOT NULL,
    comune VARCHAR(500) NOT NULL,
    provincia VARCHAR(500) NOT NULL,
    regione VARCHAR(500) NOT NULL,
    id_apicoltore INT,
    FOREIGN KEY (id_apicoltore) REFERENCES APICOLTORE(id)
);

CREATE TABLE PRODUZIONE (
    id INT PRIMARY KEY,
    anno INT NOT NULL,
    quantita FLOAT NOT NULL,
    codice_apiario INT,
    id_miele INT,
    FOREIGN KEY (id_miele) REFERENCES MIELE(id),
    FOREIGN KEY (codice_apiario) REFERENCES APIARIO(codice_apiario)
);

INSERT INTO APICOLTORE (id,nome) VALUES 
(1, "Mario Rossi"),
(2, "Laura Bianchi"),
(3, "Giuseppe Verdi");

INSERT INTO TIPOLOGIA (id, Nome, Descrizione) VALUES 
(1, "Millefiori", "Miele da fiori misti"),
(2, "Acacia", "Miele di acacia puro");

INSERT INTO MIELE (id, denominazione, id_tipologia) VALUES 
(1, "Miele Primavera", 1),
(2, "Miele Estate", 2);

INSERT INTO APIARIO (codice_apiario, numero_arnie, localita, comune, provincia, regione, id_apicoltore) VALUES 
(1, 10, "Collina Verde", "Siena", "SI", "Toscana", 1),
(2, 15, "Valle Fiorita", "Arezzo", "AR", "Toscana", 2);

INSERT INTO PRODUZIONE (id, anno, quantita, codice_apiario, id_miele) VALUES 
(1, 2023, 100.5, 1, 1),
(2, 2023, 85.3, 2, 2);


SELECT anno, SUM(quantita) AS quantita_totale
FROM PRODUZIONE
GROUP BY anno;


SELECT codice_apiario, AVG(quantita) AS produzione_media
FROM PRODUZIONE
GROUP BY codice_apiario;


SELECT id_miele, COUNT(*) AS numero_produzioni, SUM(quantita) AS produzione_totale
FROM PRODUZIONE
GROUP BY id_miele;


SELECT id_miele, SUM(quantita) AS produzione_totale
FROM PRODUZIONE
WHERE anno = 2024
GROUP BY id_miele;


SELECT anno, MAX(quantita) AS produzione_massima, MIN(quantita) AS produzione_minima
FROM PRODUZIONE
GROUP BY anno;


SELECT codice_apiario, SUM(quantita) AS produzione_totale
FROM PRODUZIONE
GROUP BY codice_apiario
HAVING SUM(quantita) > 200;


SELECT TIPOLOGIA.id AS typology_id, SUM(quantita) AS produzione_totale
FROM PRODUZIONE
JOIN MIELE ON PRODUZIONE.id_miele = MIELE.id
JOIN TIPOLOGIA ON MIELE.id_tipologia = TIPOLOGIA.id
GROUP BY TIPOLOGIA.id;


SELECT id_tipologia, COUNT(*) AS numero_mieli
FROM MIELE
GROUP BY id_tipologia;


SELECT APIARIO.id_apicoltore AS beekeeper_id, SUM(quantita) AS produzione_totale
FROM PRODUZIONE
JOIN APIARIO ON PRODUZIONE.codice_apiario = APIARIO.codice_apiario
GROUP BY APIARIO.id_apicoltore;


SELECT APIARIO.codice_apiario, SUM(quantita) / APIARIO.numero_arnie AS produzione_media_per_arnia
FROM PRODUZIONE
JOIN APIARIO ON PRODUZIONE.codice_apiario = APIARIO.codice_apiario
GROUP BY APIARIO.codice_apiario;


SELECT anno, COUNT(*) AS numero_produzioni
FROM PRODUZIONE
WHERE quantita > 100
GROUP BY anno;


SELECT id_miele, anno, SUM(quantita) AS somma_quantita
FROM PRODUZIONE
GROUP BY id_miele, anno;