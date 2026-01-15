#!/usr/bin/env python3
"""
Script per eseguire l'applicazione Flask
Uso: python run.py
"""

import os
import sys

# Aggiungiamo il percorso della cartella al path di Python
sys.path.insert(0, os.path.dirname(__file__))

from esercizio_13 import create_app

if __name__ == '__main__':
    app = create_app()
    # Debug=True per ricaricare automaticamente
    # host='0.0.0.0' per rendere accessibile da altri computer
    app.run(debug=True, host='127.0.0.1', port=5000)
