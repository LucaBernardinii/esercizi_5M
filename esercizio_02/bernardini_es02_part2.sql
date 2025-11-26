-- query basate su esercizio 02
SELECT nome, regione
FROM APICOLTORE
JOIN APIARIO ON APICOLTORE.id = APIARIO.id_apicoltore
GROUP BY regione

SELECT COUNT(codice_apiario) as NumeroApiari, regione
FROM APIARIO
GROUP BY regione;

SELECT quantita, anno, Nome
FROM PRODUZIONE
JOIN MIELE ON MIELE.id = PRODUZIONE.id_miele
JOIN TIPOLOGIA ON TIPOLOGIA.id = MIELE.id_tipologia
WHERE anno = 2023
GROUP BY TIPOLOGIA.Nome;