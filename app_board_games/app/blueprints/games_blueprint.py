from flask import Blueprint, render_template, request, redirect, url_for
from app.repository.games_repository import GamesRepository
from app.models import Game, Partita

games_bp = Blueprint('games', __name__)
repo = GamesRepository()

@games_bp.route('/')
def index():
    games = repo.get_all()
    return render_template('index.html', games=games)

@games_bp.route('/add', methods=['POST'])
def add_game():
    nome = request.form.get('nome')
    numero_giocatori_massimo = request.form.get('numero_giocatori_massimo')
    durata_media = request.form.get('durata_media')
    categoria = request.form.get('categoria')
    
    game = Game(nome, numero_giocatori_massimo, durata_media, categoria)
    repo.add(game)
    
    return redirect(url_for('games.index'))

@games_bp.route('/gioco/<int:game_id>')
def view_game(game_id):
    game = repo.get_by_id(game_id)
    if not game:
        return redirect(url_for('games.index'))
    
    partite = repo.get_partite_by_game(game_id)
    return render_template('game_detail.html', game=game, partite=partite)

@games_bp.route('/gioco/<int:game_id>/add_partita', methods=['POST'])
def add_partita(game_id):
    game = repo.get_by_id(game_id)
    if not game:
        return redirect(url_for('games.index'))
    
    data = request.form.get('data')
    vincitore = request.form.get('vincitore')
    punteggio_vincitore = request.form.get('punteggio_vincitore')
    
    partita = Partita(game_id, data, vincitore, punteggio_vincitore)
    repo.add_partita(partita)
    
    return redirect(url_for('games.view_game', game_id=game_id))