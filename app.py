from __future__ import annotations
from abc import ABC, abstractmethod


# Estoy considerando tres estados: encendido, apagado y dormido
# Dependiendo del estado, el bot puede hablar o no



class Contexto:

    estado_bot = None

    def __init__(self, estado):
        self.transicion(estado)

    def transicion(self, nuevo_estado):
        self.estado_bot = nuevo_estado
        self.estado_bot.contexto = self

    def encender(self):
        self.estado_bot.encender()
    
    def apagar(self):
        self.estado_bot.apagar()

    def dormir(self):
        self.estado_bot.dormir()

    def hablar(self):
        self.estado_bot.hablar()


class Estado(ABC):

    @property
    def context(self):
        return self.contexto

    @context.setter
    def context(self, context):
        self.context = contexto

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Encender(Estado):

    def hablar(self):
        print("El bot está hablando!")
    
    def dormir(self):
        print("El bot va a dormir zzzz")
        self.contexto.transicion(Dormir())
    
    def apagar(self):
        print("El bot se va a apagar :(")
        self.contexto.transicion(Apagar())

    def encender(self):
        pass
    
class Apagar(Estado):
    def hablar(self):
        print("El bot no puede hablar porque está apagado!!")
    
    def encender(self):
        print("El bot se está prendiendo")
        self.contexto.transicion(Encender())
    
    def dormir(self):
        print("El bot no puede dormir porque está apagado!!")

    def apagar(self):
        pass

class Dormir(Estado):
    def hablar(self):
        print("El bot se despertó y habló!!")
        self.contexto.transicion(Encender())
    
    def encender(self):
        print("El bot se está prendiendo")
        self.contexto.transicion(Encender())
    
    def apagar(self):
        print("El bot se apagó!!")

    def dormir(self):
        pass


if __name__ == "__main__":
    contexto = Contexto(Encender())
    contexto.hablar()
    