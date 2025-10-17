erDiagram
    NEGOZIO {
        str id PK
        str indirizzo
        str citta
    }

    DIPENDENTE {
        str id PK
        str nome
        str negozio FK
    }

    ALBUM {
        str id PK
        str titolo
        float prezzo
    }

    VENDITA {
        str id PK
        date data
        str negozio FK
        float importo_totale
    }

    RIGA_VENDITA {
        str id PK
        str vendita FK
        str album FK
        int quantita
        float prezzo_unitario
    }

NEGOZIO ||--o{ DIPENDENTE : "lavorano"
ARTISTA ||--o{ ALBUM : "pubblica"
NEGOZIO ||--o{ VENDITA : "effettua"
VENDITA ||--o{ RIGA_VENDITA : "contiene"