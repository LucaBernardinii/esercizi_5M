from flask import Blueprint, render_template, request, redirect, url_for, g
from .db import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Home page con lista di tutti i canali"""
    db = get_db()
    canali = db.execute(
        'SELECT id, nome, numero_iscritti, categoria FROM canali'
    ).fetchall()
    return render_template('index.html', canali=canali)

@bp.route('/canali/nuovo', methods=['GET', 'POST'])
def nuovo_canale():
    """Crea un nuovo canale"""
    if request.method == 'POST':
        nome = request.form['nome']
        numero_iscritti = request.form.get('numero_iscritti', 0, type=int)
        categoria = request.form['categoria']
        error = None

        if not nome:
            error = 'Il nome del canale è obbligatorio.'
        if not categoria:
            error = 'La categoria è obbligatoria.'

        if error is None:
            db = get_db()
            db.execute(
                'INSERT INTO canali (nome, numero_iscritti, categoria) VALUES (?, ?, ?)',
                (nome, numero_iscritti, categoria)
            )
            db.commit()
            return redirect(url_for('main.index'))

        return render_template('nuovo_canale.html', error=error)

    return render_template('nuovo_canale.html')

@bp.route('/canale/<int:canale_id>')
def dettagli_canale(canale_id):
    """Visualizza i dettagli di un canale e i suoi video"""
    db = get_db()
    canale = db.execute(
        'SELECT id, nome, numero_iscritti, categoria FROM canali WHERE id = ?',
        (canale_id,)
    ).fetchone()
    
    if canale is None:
        return "Canale non trovato", 404

    video = db.execute(
        'SELECT id, titolo, durata, immagine FROM video WHERE canale_id = ? ORDER BY id',
        (canale_id,)
    ).fetchall()

    return render_template('dettagli_canale.html', canale=canale, video=video)

@bp.route('/video/nuovo/<int:canale_id>', methods=['GET', 'POST'])
def nuovo_video(canale_id):
    """Aggiunge un nuovo video a un canale"""
    db = get_db()
    canale = db.execute(
        'SELECT id, nome FROM canali WHERE id = ?',
        (canale_id,)
    ).fetchone()

    if canale is None:
        return "Canale non trovato", 404

    if request.method == 'POST':
        titolo = request.form['titolo']
        durata = request.form.get('durata', 0, type=int)
        immagine = request.form.get('immagine', '')
        error = None

        if not titolo:
            error = 'Il titolo del video è obbligatorio.'
        if durata <= 0:
            error = 'La durata deve essere maggiore di 0 secondi.'

        if error is None:
            db.execute(
                'INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (?, ?, ?, ?)',
                (canale_id, titolo, durata, immagine)
            )
            db.commit()
            return redirect(url_for('main.dettagli_canale', canale_id=canale_id))

        return render_template('nuovo_video.html', canale=canale, error=error)

    return render_template('nuovo_video.html', canale=canale)

@bp.route('/about')
def about():
    return render_template('about.html')