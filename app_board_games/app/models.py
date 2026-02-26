class Game:
    def __init__(self, nome, numero_giocatori_massimo, durata_media, categoria, id=None):
        self.id = id
        self.nome = nome
        self.numero_giocatori_massimo = numero_giocatori_massimo
        self.durata_media = durata_media
        self.categoria = categoria


class Partita:
    def __init__(self, gioco_id, data, vincitore, punteggio_vincitore, id=None):
        self.id = id
        self.gioco_id = gioco_id
        self.data = data
        self.vincitore = vincitore
        self.punteggio_vincitore = punteggio_vincitore