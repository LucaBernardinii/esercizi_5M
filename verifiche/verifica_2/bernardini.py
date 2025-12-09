import requests

BASE_URL = "http://localhost:3000"

try:
    #1. Analisi Sviluppatore
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    response.raise_for_status()
    projects = response.json()

    print("Progetti sviluppatore 1:")
    for project in projects:
        print(f"Nome progetto: {project["name"]}, budget: {project["budget"]}")

    #2. Calcolo Carico di Lavoro
    active_projects = [project for project in projects if project["status"] == "active"]
    for project in active_projects:
        response = requests.get(f"{BASE_URL}/tasks?project_id={project["id"]}")
        response.raise_for_status()
        tasks = response.json()

    hours = sum(tasks["hours_hestimated"] for task in tasks)
    print(f"Somma delle ore: {hours}")

    #3. Assegnazione Nuovo Task
    active_project1 = active_projects[0]
    new_task = {"id": 505, "project_id": active_project1["id"], "description": "Code Review Finale", "is_done": False, "hours_hestimated": 3}

    response = requests.post(f"{BASE_URL}/tasks/{new_task}")
    response.raise_for_status()
    tasks = response.json()
    
    #4. Pulizia
    response = requests.get(f"{BASE_URL}/tasks")
    response.raise_for_status()
    tasks = response.json()

    completed_tasks = [task for task in tasks if task["is_done"]]
    completed_task1 = completed_tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{completed_task1}")
    response.raise_for_status()
    tasks = response.json()
    print(f"ID task eliminato: {completed_task1["id"]}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")