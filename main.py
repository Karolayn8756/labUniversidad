class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        super().__init__(nombre, edad, sexo)
        self.carnet = carnet
        self.carrera = carrera

    def __str__(self):
        return f"{super().__str__()}, Carnet: {self.carnet}, Carrera: {self.carrera}"
class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        super().__init__(nombre, edad, sexo)
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return f"{super().__str__()}, Código: {self.codigo}, Especialidad: {self.especialidad}"
class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def __str__(self):
        return f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor.nombre}"
class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        cursos_str = "\n".join([str(curso) for curso in self.cursos])
        return f"Universidad: {self.nombre}\nCursos:\n{cursos_str}"
# Crear la universidad
universidad = Universidad("Universidad de El Salvador")

# Crear los profesores
profesor_juan = Profesor("Juan Perez", 30, "Masculino", "202020202", "Matematicas")
profesor_maria = Profesor("Maria Lopez", 35, "Femenino", "202020203", "Fisica")
profesor_pedro = Profesor("Pedro Ramirez", 40, "Masculino", "202020204", "Quimica")

# Crear los cursos
curso_matematicas = Curso("Matematicas", "MAT101", profesor_juan)
curso_fisica = Curso("Fisica", "FIS101", profesor_maria)
curso_quimica = Curso("Quimica", "QUI101", profesor_pedro)

# Agregar los cursos a la universidad
universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

# Crear el objeto estudiante
estudiante_carlos = Estudiante("Carlos Perez", 20, "Masculino", "202010101", "Ingenieria en Sistemas Informaticos")
print(universidad)
print()
print(estudiante_carlos)
print()
print(profesor_juan)
print()
print(curso_matematicas)

# Crear un nuevo curso de Fisica y agregarlo a la universidad
curso_nuevo_fisica = Curso("Fisica", "FIS101", profesor_maria)
universidad.agregar_curso(curso_nuevo_fisica)

# Imprimir nuevamente la universidad con el nuevo curso agregado
print()
print(universidad)