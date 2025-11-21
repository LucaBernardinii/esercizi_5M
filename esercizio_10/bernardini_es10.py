import requests

def get_todos_by_user(user_id):
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={1}"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nel recupero dei todos: {e}")
        return None
    
def primo_todo_incompleto(todos):
    if not todos:
        print("Nessun todo disponibile.")
        return None

    for todo in todos:
        if not todo.get("completed", True):
            todo_id = todo.get("id")
            if todo_id is None:
                print("Todo trovato ma manca l'id.")
                return None

            updated = {**todo, "completed": True}
            try:
                response = requests.put(
                    f"https://jsonplaceholder.typicode.com/todos/{todo_id}",
                    json=updated
                )
                response.raise_for_status()
                print(f"Todo {todo_id} marcato come completato.")
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Errore nell'aggiornamento del todo: {e}")
                return None

    print("Non ci sono todos incompleti.")
    return None