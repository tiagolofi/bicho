
import random

class JogoBicho():
    def __init__(self, bicho: str):
        self.numero_sorteio = None
        self.bicho = bicho
        self.animais_jogo_do_bicho = {
            'Avestruz': [0, 1, 2, 3], 'Águia': [4, 5, 6, 7], 'Burro': [8, 9, 10, 11], 'Borboleta': [12, 13, 14, 15], 'Cachorro': [16, 17, 18, 19], 
            'Cabra': [20, 21, 22, 23], 'Carneiro': [24, 25, 26, 27], 'Camelo': [28, 29, 30, 31], 'Cobra': [32, 33, 34, 35], 'Coelho': [36, 37, 38, 39],
            'Cavalo': [40, 41, 42, 43], 'Elefante': [44, 45, 46, 47], 'Galo': [48, 49, 50, 51], 'Gato': [52, 53, 54, 55], 'Jacaré': [56, 57, 58, 59],
            'Leão': [60, 61, 62, 63], 'Macaco': [64, 65, 66, 67], 'Porco': [68, 69, 70, 71], 'Pavão': [72, 73, 74, 75], 'Peru': [76, 77, 78, 79],
            'Touro': [80, 81, 82, 83], 'Tigre': [84, 85, 86, 87], 'Urso': [88, 89, 90, 91], 'Veado': [92, 93, 94, 95], 'Vaca': [96, 97, 98, 99]
        }

    def sorteio(self):
        self.numero_sorteio = random.randint(0, 99)

    def __call__(self):
        self.sorteio()
        if self.numero_sorteio in self.animais_jogo_do_bicho.get(self.bicho):
            return {'aposta': self.bicho, 'numero_sorteado': self.numero_sorteio, 'resultado': 'ganho'}    
        return {'aposta': self.bicho, 'numero_sorteado': self.numero_sorteio, 'resultado': 'perda'}