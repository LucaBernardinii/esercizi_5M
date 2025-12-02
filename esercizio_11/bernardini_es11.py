import requests

def main():
    base = 'https://jsonplaceholder.typicode.com'
    try:
        r = requests.get(f'{base}/posts', params={'userId': 1}, timeout=10)
        r.raise_for_status()
        posts = r.json()
    except requests.RequestException as e:
        print(f'Errore recupero post: {e}')
        return

    posts_info = []
    for p in posts:
        pid = p.get('id')
        title = p.get('title', '')
        try:
            rc = requests.get(f'{base}/posts/{pid}/comments', timeout=10)
            rc.raise_for_status()
            comments = rc.json()
        except requests.RequestException as e:
            print(f'Errore recupero commenti per post {pid}: {e}')
            comments = []
        posts_info.append({'id': pid, 'title': title, 'comments': comments})

    print("--- Post dell'utente 1 ---")
    for pi in posts_info:
        print(f"Post ID: {pi['id']}, Titolo: {pi['title']}, Commenti: {len(pi['comments'])}")

    if not posts_info:
        print('Nessun post trovato per l\'utente 1.')
        return

    selected = max(posts_info, key=lambda x: len(x['comments']))

    print('\n--- Post con più commenti ---')
    print(f"ID: {selected['id']}, Titolo: {selected['title']}, Commenti: {len(selected['comments'])}")

    print('\n--- Azione intrapresa ---')
    if len(selected['comments']) < 5:
        payload = {
            'postId': selected['id'],
            'name': 'Commento automatico',
            'email': 'auto@example.com',
            'body': 'Commento creato automaticamente perché il post aveva meno di 5 commenti.'
        }
        try:
            rp = requests.post(f'{base}/comments', json=payload, timeout=10)
            rp.raise_for_status()
            created = rp.json()
            print(f"Poiché il post ha meno di 5 commenti, creato nuovo commento ID: {created.get('id')}")
        except requests.RequestException as e:
            print(f'Errore creazione commento: {e}')
    else:
        if selected['comments']:
            oldest = min(selected['comments'], key=lambda c: c.get('id', float('inf')))
            cid = oldest.get('id')
            try:
                rd = requests.delete(f'{base}/comments/{cid}', timeout=10)
                if rd.status_code in (200, 204):
                    print(f"Poiché il post ha 5 o più commenti, eliminato il commento ID: {cid} (il più vecchio).")
                else:
                    print(f'Errore eliminazione commento ID {cid}: status {rd.status_code}')
            except requests.RequestException as e:
                print(f'Errore eliminazione commento: {e}')
        else:
            print('Il post ha 5 o più commenti ma non sono stati trovati commenti effettivi da eliminare.')

if __name__ == "__main__":
    main()