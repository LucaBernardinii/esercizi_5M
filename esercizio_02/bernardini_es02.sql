CREATE TABLE TIPOLOGIA (
    id INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Descrizione VARCHAR(50) NOT NULL,
)

CREATE TABLE MIELE (
    id INT PRIMARY KEY,
    denominazione VARCHAR(50) NOT NULL,
    id_tipologia INT,
    FOREIGN KEY (id_tipologia) REFERENCES TIPOLOGIA(id_tipologia)
)

CREATE TABLE PRODUZIONE (
    id INT PRIMARY KEY,
    anno INT NOT NULL,
    quantita FLOAT NOT NULL,
    codice_apiario INT,
    id_miele INT,
    FOREIGN KEY (id_miele) REFERENCES MIELE(id_miele)
    FOREIGN KEY (codice_apiario) REFERENCES APIARIO(codice_apiario)
)

CREATE TABLE APIARIO (
    codice_apiario INT PRIMARY KEY,
    numero_arnie INT NOT NULL,
    localita VARCHAR(50) NOT NULL,
    comune VARCHAR(50) NOT NULL,
    provincia VARCHAR(50) NOT NULL,
    regione VARCHAR(50) NOT NULL,
    id_apicoltore INT,
    FOREIGN KEY (id_apicoltore) REFERENCES APICOLTORE(id_apicoltore)
)

CREATE TABLE APICOLTORE (
    id INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
)

INSERT INTO APICOLTORE (id, nome) VALUES 
(1, 'Mario Rossi'),
(2, 'Laura Bianchi'),
(3, 'Giuseppe Verdi');

INSERT INTO TIPOLOGIA (id, Nome, Descrizione) VALUES 
(1, 'Millefiori', 'Miele da fiori misti'),
(2, 'Acacia', 'Miele di acacia puro');

INSERT INTO MIELE (id, denominazione, id_tipologia) VALUES 
(1, 'Miele Primavera', 1),
(2, 'Miele Estate', 2);

INSERT INTO APIARIO (codice_apiario, numero_arnie, localita, comune, provincia, regione, id_apicoltore) VALUES 
(1, 10, 'Collina Verde', 'Siena', 'SI', 'Toscana', 1),
(2, 15, 'Valle Fiorita', 'Arezzo', 'AR', 'Toscana', 2);

INSERT INTO PRODUZIONE (id, anno, quantita, codice_apiario, id_miele) VALUES 
(1, 2023, 100.5, 1, 1),
(2, 2023, 85.3, 2, 2);


SELECT * FROM APICOLTORE;
SELECT nome FROM APICOLTORE WHERE id = 1;
SELECT * FROM APIARIO WHERE regione = 'Lombardia';
SELECT codice_apiario, numero_arnie FROM APIARIO WHERE numero_arnie > 10;
SELECT codice_apiario, localita FROM APIARIO WHERE id_apicoltore = 2;
SELECT * FROM MIELE WHERE id_tipologia = 3;
SELECT denominazione FROM MIELE WHERE id = 5;
SELECT * FROM PRODUZIONE WHERE anno = 2024;
SELECT * FROM PRODUZIONE WHERE codice_apiario = 'A001';
SELECT * FROM PRODUZIONE WHERE id_miele = 3 AND anno = 2023;