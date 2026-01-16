import sqlite3
import os
from flask import g, current_app

def get_db():
    """Ritorna la connessione al database"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Chiude la connessione al database"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Inizializza il database eseguendo schema.sql"""
    db = get_db()
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path) as f:
        db.executescript(f.read())
    db.commit()
