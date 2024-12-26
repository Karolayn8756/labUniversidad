from .curso import Curso

class Universidad(Curso):
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        cursos_str = "\n".join([str(curso) for curso in self.cursos])
        return f"Universidad: {self.nombre}\nCursos:\n{cursos_str}"

