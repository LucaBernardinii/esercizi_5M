import os
import sqlite3
from flask import Flask

def get_db(app):
    """Ritorna la connessione al database SQLite."""
    conn = sqlite3.connect(
        os.path.join(app.instance_path, 'video_app.sqlite')
    )
    conn.row_factory = sqlite3.Row  # Ritorna i dati come dizionari
    return conn

def init_db(app):
    """Inizializza il database con lo schema SQL."""
    db = get_db(app)
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as f:
        db.executescript(f.read())
    db.commit()
    db.close()

def create_app():
    """Factory function per creare l'app Flask."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Configurazione di base
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'video_app.sqlite'),
    )
    
    # Assicuriamo che la cartella instance esista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Inizializzare il database al primo avvio
    if not os.path.exists(app.config['DATABASE']):
        init_db(app)
    
    # Registriamo il blueprint principale
    from . import main
    app.register_blueprint(main.bp)
    
    return app
