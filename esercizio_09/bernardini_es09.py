import requests
import json

url = "https://jsonplaceholder.typicode.com"
user_id = 1
timeout = 10

try:
    posts_resp = requests.get(f"{url}/posts", params={"userId": user_id}, timeout=timeout)
    posts_resp.raise_for_status()
    posts = posts_resp.json()
    print("--- Post dell'utente 1 ---")

    if not posts:
        print("Nessun post trovato per l'utente 1.")

    for p in posts:
        print(f"ID Post: {p['id']}, Titolo: {p['title']}")

    first_post = posts[0]
    post_id = first_post["id"]

    comments_resp = requests.get(f"{url}/posts/{post_id}/comments", timeout=timeout)
    comments_resp.raise_for_status()
    comments = comments_resp.json()
    print("\n--- Commenti per il primo post ---")

    for c in comments:
        print(f"- {c['name']}: {c['body']}")

    nuovo_commento = {
        "postId": post_id,
        "name": "Nuovo Commentatore",
        "email": "nuovo@example.com",
        "body": "Questo è un commento aggiunto tramite API!"
    }

    create_resp = requests.post(f"{url}/comments", json=nuovo_commento, timeout=timeout)
    create_resp.raise_for_status()
    created = create_resp.json()
    print("\n--- Nuovo Commento Creato ---")
    print(json.dumps(created, indent=4, ensure_ascii=False))

except requests.exceptions.HTTPError as http_err:
    print(f"Errore HTTP: {http_err}")

except requests.exceptions.RequestException as req_err:
    print(f"Errore durante la richiesta: {req_err}")

except ValueError as val_err:
    print(f"Errore nel parsing della risposta JSON: {val_err}")