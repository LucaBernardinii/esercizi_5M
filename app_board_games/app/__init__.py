from flask import Flask
from app.repository.games_repository import GamesRepository

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chiave-segreta'
    
    from app.blueprints.games_blueprint import games_bp
    app.register_blueprint(games_bp)
    
    return app