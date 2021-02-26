from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class Encender(Command):

    def __init__(self):
        pass
    
    def execute(self):
        print("El bot se encendió!")

class Apagar(Command):
    def __init__(self):
        pass
    
    def execute(self):
        print("El bot se apagó! :(")

class Dormir(Command):
    def __init__(self):
        pass
    
    def execute(self):
        print("El bot se durmió!")

class Hablar(Command):
    def __init__(self, payload):
        self.payload = payload
    
    def execute(self):
        print("El bot dice: {}".format(self.payload))

class Invoker:

    def execute(self, command):
        
        if isinstance(command, Command):
            command.execute()
        else:
            print("No conozco ese comando :(")
 

if __name__ == "__main__":

    invoker = Invoker()

    invoker.execute(Hablar("Holaaa"))