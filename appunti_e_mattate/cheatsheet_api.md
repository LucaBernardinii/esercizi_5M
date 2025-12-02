### Schema Visivo
```
┌──────────────────────┐         ┌──────────────────────┐
│   TERMINALE 1        │         │   TERMINALE 2        │
│   (Server prof)      │         │   (Tuo codice)       │
├──────────────────────┤         ├──────────────────────┤
│ $ python server.py   │         │ $ python esercizio.py│
│                      │         │                      │
│ SERVER ATTIVO        │◄────────│ import requests      │
│ PORTA 3001           │ request │ requests.get()       │
│                      │────────►│                      │
│ ⚠️ NON CHIUDERE!     │ risposta│ print(risultati)     │
└──────────────────────┘         └──────────────────────┘
```

---

## 📚 SOLUZIONE DEL PROF - STILE DIRETTO (SENZA FUNZIONI)
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # 1. CERCA LIBRI DI UN AUTORE
    response = requests.get(f"{BASE_URL}/books?author_id=1")
    response.raise_for_status()
    books = response.json()
    
    # Prendi nome autore
    author_response = requests.get(f"{BASE_URL}/authors/1")
    author_response.raise_for_status()
    author = author_response.json()
    
    print(f"Libri di {author['name']}:")
    for book in books:
        print(f"  - {book['title']} ({book['pages']} pagine)")
    
    
    # 2. FILTRA PER DISPONIBILITÀ
    available_books = [book for book in books if book["available"]]
    
    print("\nLibri disponibili:")
    for book in available_books:
        print(f"  - {book['title']}")
    
    
    # 3. CONTA PAGINE TOTALI
    total_pages = sum(book["pages"] for book in available_books)
    print(f"\nPagine totali disponibili: {total_pages}")
    
    
    # 4. LIBRI PER GENERE
    response = requests.get(f"{BASE_URL}/books?genre_id=101")
    response.raise_for_status()
    fantasy_books = response.json()
    
    genre_response = requests.get(f"{BASE_URL}/genres/101")
    genre_response.raise_for_status()
    genre = genre_response.json()
    
    print(f"\nGenere: {genre['name']}")
    print(f"Numero di libri: {len(fantasy_books)}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")
```
---
## SOLUZIONE ALTERNATIVA
```python
import requests

# URL base - CONTROLLA LA PORTA nel messaggio del server!
BASE_URL = "http://localhost:3001"

# --- FUNZIONI GET ---

def get_books_by_author(author_id):
    try:
        response = requests.get(f"{BASE_URL}/books?author_id={author_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_author(author_id):
    try:
        response = requests.get(f"{BASE_URL}/authors/{author_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_books_by_genre(genre_id):
    try:
        response = requests.get(f"{BASE_URL}/books?genre_id={genre_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_genre(genre_id):
    try:
        response = requests.get(f"{BASE_URL}/genres/{genre_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

# --- MAIN ---

def main():
    # 1. CERCA LIBRI DI UN AUTORE
    author_id = 1
    
    # Prendi info autore
    author = get_author(author_id)
    if author is None:
        return
    
    # Prendi libri dell'autore
    books = get_books_by_author(author_id)
    if books is None:
        return
    
    # Stampa libri
    print(f"Libri di {author['name']}:")
    for book in books:
        print(f"  - {book['title']} ({book['pages']} pagine)")
    
    
    # 2. FILTRA PER DISPONIBILITÀ
    libri_disponibili = []
    for book in books:
        if book['available']:
            libri_disponibili.append(book)
    
    # Stampa disponibili
    print("\nLibri disponibili:")
    for book in libri_disponibili:
        print(f"  - {book['title']}")
    
    
    # 3. CONTA PAGINE TOTALI
    pagine_totali = 0
    for book in libri_disponibili:
        pagine_totali += book['pages']
    
    # Stampa totale
    print(f"\nPagine totali disponibili: {pagine_totali}")
    
    
    # 4. LIBRI PER GENERE
    genre_id = 101
    
    # Prendi info genere
    genre = get_genre(genre_id)
    if genre is None:
        return
    
    # Prendi libri del genere
    books_genre = get_books_by_genre(genre_id)
    if books_genre is None:
        return
    
    # Stampa risultato
    print(f"\nGenere: {genre['name']}")
    print(f"Numero di libri: {len(books_genre)}")

if __name__ == "__main__":
    main()
```
---

## 🔥 TEMPLATE STILE PROF - TUTTO NEL TRY/EXCEPT

### Template Completo Base
```python
import requests

BASE_URL = "http://localhost:PORTA"  # Cambia PORTA

try:
    # PASSO 1: Prima richiesta GET
    response = requests.get(f"{BASE_URL}/RISORSA")
    response.raise_for_status()
    dati = response.json()
    
    # PASSO 2: Lavora con i dati
    print(f"Totale: {len(dati)}")
    
    # PASSO 3: Filtra se necessario
    filtrati = [item for item in dati if item['campo'] == valore]
    
    # PASSO 4: Stampa risultati
    for item in filtrati:
        print(f"  - {item['nome']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

### Template GET con Filtro
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # GET con filtro query parameter
    response = requests.get(f"{BASE_URL}/RISORSA?PARAM={valore}")
    response.raise_for_status()
    risultati = response.json()
    
    print(f"Trovati: {len(risultati)}")
    for item in risultati:
        print(f"  - {item['nome']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

### Template GET Singolo Elemento
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # GET elemento specifico
    response = requests.get(f"{BASE_URL}/RISORSA/{id}")
    response.raise_for_status()
    elemento = response.json()
    
    print(f"Nome: {elemento['nome']}")
    print(f"Dettagli: {elemento['info']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

### Template POST Creare
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Dati da inviare
    nuovo_elemento = {
        'campo1': 'valore1',
        'campo2': 'valore2'
    }
    
    # POST richiesta
    response = requests.post(f"{BASE_URL}/RISORSA", json=nuovo_elemento)
    response.raise_for_status()
    creato = response.json()
    
    print(f"Creato con ID: {creato['id']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

### Template PUT Aggiornare
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Dati da aggiornare
    aggiornamento = {
        'campo': 'nuovo_valore'
    }
    
    # PUT richiesta
    response = requests.put(f"{BASE_URL}/RISORSA/{id}", json=aggiornamento)
    response.raise_for_status()
    aggiornato = response.json()
    
    print(f"Aggiornato: {aggiornato['campo']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

### Template DELETE Eliminare
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # DELETE richiesta
    response = requests.delete(f"{BASE_URL}/RISORSA/{id}")
    response.raise_for_status()
    
    print(f"Eliminato elemento ID: {id}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## 🎯 OPERAZIONI COMUNI STILE PROF

### 1. List Comprehension (Filtrare)
```python
# Invece di:
filtrati = []
for item in lista:
    if item['campo'] == valore:
        filtrati.append(item)

# Usa (stile prof):
filtrati = [item for item in lista if item['campo'] == valore]

# ESEMPI:
# Filtra disponibili
disponibili = [book for book in books if book['available']]

# Filtra lunghi
lunghi = [book for book in books if book['pages'] > 300]

# Filtra non disponibili
non_disponibili = [book for book in books if not book['available']]
```

### 2. Sum con Generatore (Sommare)
```python
# Invece di:
totale = 0
for item in lista:
    totale += item['numero']

# Usa (stile prof):
totale = sum(item['numero'] for item in lista)

# ESEMPI:
# Somma tutte le pagine
totale_pagine = sum(book['pages'] for book in books)

# Somma pagine disponibili
pagine_disponibili = sum(book['pages'] for book in books if book['available'])

# Conta elementi (somma di 1)
num_disponibili = sum(1 for book in books if book['available'])
```

### 3. Len (Contare)
```python
# Conta tutti
totale = len(lista)

# Conta con condizione (usa list comprehension)
disponibili = len([book for book in books if book['available']])

# OPPURE (più efficiente):
disponibili = sum(1 for book in books if book['available'])
```

### 4. Loop For Semplice
```python
# Stampa tutti
for item in lista:
    print(f"  - {item['nome']}")

# Stampa con condizione
for item in lista:
    if item['valido']:
        print(f"  - {item['nome']}")

# ESEMPIO:
# Stampa titoli disponibili
for book in books:
    if book['available']:
        print(f"  - {book['title']}")
```

---

## 📝 ESEMPIO COMPLETO 1: Trova Libro Più Lungo (Stile Prof)
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Prendi tutti i libri
    response = requests.get(f"{BASE_URL}/books")
    response.raise_for_status()
    books = response.json()
    
    print(f"Totale libri: {len(books)}")
    
    # Filtra solo disponibili
    disponibili = [book for book in books if book['available']]
    print(f"Disponibili: {len(disponibili)}")
    
    # Prendi info autore
    author_response = requests.get(f"{BASE_URL}/authors/{piu_lungo['author_id']}")
    author_response.raise_for_status()
    author = author_response.json()
    
    # Stampa risultato
    print(f"\nLibro più lungo disponibile:")
    print(f"Titolo: {piu_lungo['title']}")
    print(f"Autore: {author['name']}")
    print(f"Pagine: {piu_lungo['pages']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## 📝 ESEMPIO COMPLETO 2: Statistiche per Genere (Stile Prof)
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Prendi tutti i generi
    response = requests.get(f"{BASE_URL}/genres")
    response.raise_for_status()
    genres = response.json()
    
    print("--- Statistiche per Genere ---")
    
    # Per ogni genere
    for genre in genres:
        # Prendi libri del genere
        books_response = requests.get(f"{BASE_URL}/books?genre_id={genre['id']}")
        books_response.raise_for_status()
        books = books_response.json()
        
        # Conta disponibili
        disponibili = sum(1 for book in books if book['available'])
        
        # Stampa
        print(f"\n{genre['name']}:")
        print(f"  Totale: {len(books)}")
        print(f"  Disponibili: {disponibili}")
        print(f"  Non disponibili: {len(books) - disponibili}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## 📝 ESEMPIO COMPLETO 3: Confronta Autori (Stile Prof)
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Info autore 1
    author1_response = requests.get(f"{BASE_URL}/authors/1")
    author1_response.raise_for_status()
    author1 = author1_response.json()
    
    books1_response = requests.get(f"{BASE_URL}/books?author_id=1")
    books1_response.raise_for_status()
    books1 = books1_response.json()
    
    # Info autore 2
    author2_response = requests.get(f"{BASE_URL}/authors/2")
    author2_response.raise_for_status()
    author2 = author2_response.json()
    
    books2_response = requests.get(f"{BASE_URL}/books?author_id=2")
    books2_response.raise_for_status()
    books2 = books2_response.json()
    
    # Confronto
    print("--- Confronto Autori ---")
    print(f"{author1['name']}: {len(books1)} libri")
    print(f"{author2['name']}: {len(books2)} libri")
    
    # Chi ha più libri?
    if len(books1) > len(books2):
        print(f"\n{author1['name']} ha più libri!")
    elif len(books2) > len(books1):
        print(f"\n{author2['name']} ha più libri!")
    else:
        print("\nHanno lo stesso numero!")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## 📝 ESEMPIO COMPLETO 4: Crea e Verifica (Stile Prof)
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # Conta libri iniziali
    response = requests.get(f"{BASE_URL}/books")
    response.raise_for_status()
    books_prima = response.json()
    print(f"Libri prima: {len(books_prima)}")
    
    # Crea nuovo libro
    nuovo_libro = {
        'title': '1984',
        'author_id': 1,
        'genre_id': 101,
        'pages': 328,
        'available': True
    }
    
    create_response = requests.post(f"{BASE_URL}/books", json=nuovo_libro)
    create_response.raise_for_status()
    creato = create_response.json()
    
    print(f"\nCreato: {creato['title']} (ID: {creato['id']})")
    
    # Verifica nuovo totale
    response = requests.get(f"{BASE_URL}/books")
    response.raise_for_status()
    books_dopo = response.json()
    print(f"Libri dopo: {len(books_dopo)}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## 📝 ESEMPIO COMPLETO 5: Aggiorna Primo Incompleto (Stile Prof)
```python
import requests

BASE_URL = "http://localhost:5000"

try:
    # Prendi todos utente 1
    response = requests.get(f"{BASE_URL}/todos?userId=1")
    response.raise_for_status()
    todos = response.json()
    
    print(f"Totale todos: {len(todos)}")
    
    # Conta completati
    completati = sum(1 for todo in todos if todo['completed'])
    print(f"Completati: {completati}")
    print(f"Incompleti: {len(todos) - completati}")
    
    # Trova primo incompleto
    incompleti = [todo for todo in todos if not todo['completed']]
    
    if len(incompleti) > 0:
        primo = incompleti[0]
        print(f"\nPrimo incompleto: {primo['title']}")
        
        # Aggiorna
        update_response = requests.put(
            f"{BASE_URL}/todos/{primo['id']}", 
            json={'completed': True}
        )
        update_response.raise_for_status()
        aggiornato = update_response.json()
        
        print(f"Aggiornato! Ora completato: {aggiornato['completed']}")
    else:
        print("\nNessun todo incompleto!")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```

---

## ⚡ RIFERIMENTO RAPIDO STILE PROF

### List Comprehension
```python
# Filtra
filtrati = [item for item in lista if condizione]

# Esempi:
disponibili = [b for b in books if b['available']]
lunghi = [b for b in books if b['pages'] > 300]
non_disp = [b for b in books if not b['available']]
```

### Sum con Generatore
```python
# Somma campo
totale = sum(item['campo'] for item in lista)

# Somma con condizione
totale = sum(item['campo'] for item in lista if condizione)

# Conta con condizione
count = sum(1 for item in lista if condizione)

# Esempi:
tot_pagine = sum(b['pages'] for b in books)
pag_disp = sum(b['pages'] for b in books if b['available'])
num_disp = sum(1 for b in books if b['available'])
```


### Richieste HTTP
```python
# GET
response = requests.get(f"{BASE_URL}/risorsa")
response.raise_for_status()
dati = response.json()

# GET con filtro
response = requests.get(f"{BASE_URL}/risorsa?param={valore}")

# POST
response = requests.post(f"{BASE_URL}/risorsa", json=dati)

# PUT
response = requests.put(f"{BASE_URL}/risorsa/{id}", json=dati)

# DELETE
response = requests.delete(f"{BASE_URL}/risorsa/{id}")
```

---

## 🚨 CHECKLIST FINALE

- ✅ `import requests` all'inizio
- ✅ `BASE_URL = "http://localhost:PORTA"` definito
- ✅ Tutto dentro `try/except`
- ✅ `response.raise_for_status()` dopo ogni richiesta
- ✅ `response.json()` per ottenere dati
- ✅ Usa list comprehension per filtrare: `[x for x in lista if condizione]`
- ✅ Usa `sum()` per sommare: `sum(x['campo'] for x in lista)`
- ✅ `except requests.exceptions.RequestException as e:` alla fine
- ✅ **2 TERMINALI APERTI: server + codice**

---

## 💡 FORMULE UTILI
```python
# Filtra
filtrati = [x for x in lista if x['campo'] == valore]

# Somma
totale = sum(x['numero'] for x in lista)

# Somma con filtro
totale = sum(x['numero'] for x in lista if x['valido'])

# Conta con filtro
count = sum(1 for x in lista if x['valido'])

# Conta tutti
count = len(lista)

# Percentuale
perc = (parte / totale) * 100

# Media
media = somma / len(lista)
```

---

## 🎯 SCHEMA COMPLETO STILE PROF
```python
import requests

BASE_URL = "http://localhost:3001"

try:
    # PASSO 1: Prima richiesta
    response = requests.get(f"{BASE_URL}/risorsa")
    response.raise_for_status()
    dati = response.json()
    
    print(f"Totale: {len(dati)}")
    
    # PASSO 2: Filtra (list comprehension)
    filtrati = [item for item in dati if item['campo'] == valore]
    print(f"Filtrati: {len(filtrati)}")
    
    # PASSO 3: Calcola (sum con generatore)
    totale = sum(item['numero'] for item in filtrati)
    print(f"Totale: {totale}")
    
    # PASSO 5: Seconda richiesta se necessario
    detail_response = requests.get(f"{BASE_URL}/dettaglio/{massimo['id']}")
    detail_response.raise_for_status()
    dettaglio = detail_response.json()
    
    # PASSO 6: Stampa risultato finale
    print(f"\nRisultato: {dettaglio['nome']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
```