import random


class Novela:

    def __init__(self, titulo, origen):
        self.id = random.randint(0, 1000000)
        self.titulo = titulo
        self.origen = origen

    def __str__(self):
        return f"\n\t|| Novela ||" \
               f"\n\t Título: {self.titulo}\n" \
               f"\t Origen: {self.origen}\n"
