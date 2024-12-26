from .persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        super().__init__(nombre, edad, sexo)
        self.carnet = carnet
        self.carrera = carrera 

    def __str__(self):
        return f"{super().__str__()}, carnet:{self.carnet}, carrera:{self.carrera}"
    


   