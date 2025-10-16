    erDiagram
    AZIENDA_VINICOLA {
        str partita_iva PK
        str nome
        str via
        str numero_civico
        str comune
        str provincia
        str regione
    }
    
    VIGNETO {
        str id PK
        str nome
        float superficie_ettari
        str localita
        str comune
        str classe_di_esposizione
        int numero_filari
    }
    
    BLOCCHI_VIGNETO {
        str id PK
        float superficie_ettari
        str classe_di_esposizione
        dict vitigni
    }
    
    VITIGNO {
        str nome_scientifico
        str nome_comune
        str colore_bacca
        str origine_genetica
    }

    ETICHETTA {
        str id PK
        str nome
        int annata
        str tipologia
    }

%% 1 a 1
ETICHETTA ||--|| AZIENDA_VINICOLA : "prodotta_da"
ETICHETTA ||--|| VIGNETO : "proviene_da"
ETICHETTA ||--|| VITIGNO : "associata_a"
VIGNETO }|--|| AZIENDA_VINICOLA : "appartengono_a"
VITIGNO }|--|| BLOCCHI_VIGNETO : "coltivati_in"
BLOCCHI_VIGNETO }|--|| VIGNETO : "parte_di"