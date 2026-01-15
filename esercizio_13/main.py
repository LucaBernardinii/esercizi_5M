import os
import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for
from . import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Home page - lista dei canali"""
    app = __import__('flask').current_app
    db = get_db(app)
    canali = db.execute('SELECT * FROM canali').fetchall()
    db.close()
    return render_template('index.html', canali=canali)

@bp.route('/canale/<int:canale_id>')
def canale_dettaglio(canale_id):
    """Visualizza un canale e i suoi video"""
    app = __import__('flask').current_app
    db = get_db(app)
    
    canale = db.execute('SELECT * FROM canali WHERE id = ?', (canale_id,)).fetchone()
    video = db.execute('SELECT * FROM video WHERE canale_id = ?', (canale_id,)).fetchall()
    
    db.close()
    
    if canale is None:
        return "Canale non trovato", 404
    
    return render_template('canale.html', canale=canale, video=video)

@bp.route('/nuovo-canale', methods=['GET', 'POST'])
def nuovo_canale():
    """Crea un nuovo canale"""
    if request.method == 'POST':
        nome = request.form['nome']
        numero_iscritti = request.form.get('numero_iscritti', 0, type=int)
        categoria = request.form['categoria']
        
        app = __import__('flask').current_app
        db = get_db(app)
        db.execute(
            'INSERT INTO canali (nome, numero_iscritti, categoria) VALUES (?, ?, ?)',
            (nome, numero_iscritti, categoria)
        )
        db.commit()
        db.close()
        
        return redirect(url_for('main.index'))
    
    return render_template('nuovo_canale.html')

@bp.route('/nuovo-video/<int:canale_id>', methods=['GET', 'POST'])
def nuovo_video(canale_id):
    """Aggiunge un nuovo video a un canale"""
    app = __import__('flask').current_app
    db = get_db(app)
    
    canale = db.execute('SELECT * FROM canali WHERE id = ?', (canale_id,)).fetchone()
    if canale is None:
        db.close()
        return "Canale non trovato", 404
    
    if request.method == 'POST':
        titolo = request.form['titolo']
        durata = request.form['durata']
        immagine = request.form.get('immagine', '')
        
        db.execute(
            'INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (?, ?, ?, ?)',
            (canale_id, titolo, durata, immagine)
        )
        db.commit()
        db.close()
        
        return redirect(url_for('main.canale_dettaglio', canale_id=canale_id))
    
    db.close()
    return render_template('nuovo_video.html', canale=canale)
