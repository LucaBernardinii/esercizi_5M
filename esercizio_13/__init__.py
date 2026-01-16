import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'video_canali.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    app.teardown_appcontext(db.close_db)
    
    @app.cli.command('init-db')
    def init_db_command():
        """Inizializza il database."""
        db.init_db()
        print('Database inizializzato.')

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import main
    app.register_blueprint(main.bp)
    # --------------------------------

    return app