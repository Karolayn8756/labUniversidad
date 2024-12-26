from clases.universidad import Universidad
from clases.estudiante import Estudiante
from clases.curso import Curso
from clases.profesor import Profesor

# Instancia de la universidad
universidad = Universidad("PUCE MANABI")

# Instancias de profesores
profesor_juan = Profesor("Karolayn Perez", 20, "Femenino", "202020202", "Matemáticas")
profesor_maria = Profesor("Emilia Lopez", 19, "Femenino", "202020203", "Física")
profesor_pedro = Profesor("Eduardo Ramirez", 20, "Masculino", "202020204", "Química")

# Instancias de cursos
curso_matematicas = Curso("Matemáticas", "MAT101", profesor_juan)
curso_fisica = Curso("Física", "FIS101", profesor_maria)
curso_quimica = Curso("Química", "QUI101", profesor_pedro)

# Agregar cursos a la universidad
universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

# Impresiones
print("\nInformación de la universidad:")
print(universidad)

# Instancia de estudiante
estudiante_carlos = Estudiante("Carlos Perez", 20, "Masculino", "202010101", "Ingeniería en Sistemas Informáticos")

print("\nInformación del estudiante:")
print(estudiante_carlos)

print("\nInformación del profesor Juan:")
print(profesor_juan)

print("\nInformación del curso de Matemáticas:")
print(curso_matematicas)
