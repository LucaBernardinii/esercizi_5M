import sqlite3
from app.models import Game, Partita

class GamesRepository:
    def __init__(self, db_path='instance/board_games.sqlite'):
        self.db_path = db_path
    
    def get_all(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM giochi')
        rows = cursor.fetchall()
        conn.close()
        
        games = [Game(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        return games
    
    def get_by_id(self, game_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM giochi WHERE id = ?', (game_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Game(row[1], row[2], row[3], row[4], row[0])
        return None
    
    def add(self, game):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)',
                      (game.nome, game.numero_giocatori_massimo, game.durata_media, game.categoria))
        conn.commit()
        conn.close()
    
    def get_partite_by_game(self, game_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM partite WHERE gioco_id = ? ORDER BY data DESC', (game_id,))
        rows = cursor.fetchall()
        conn.close()
        
        partite = [Partita(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        return partite
    
    def add_partita(self, partita):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (?, ?, ?, ?)',
                      (partita.gioco_id, partita.data, partita.vincitore, partita.punteggio_vincitore))
        conn.commit()
        conn.close()