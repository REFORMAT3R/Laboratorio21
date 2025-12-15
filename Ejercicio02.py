class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado")
        else:
            print(f"{self.titulo} no está disponible")

    def devolver(self):
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} | {self.autor} | {self.anio} | {estado}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamano_mb):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamano_mb = tamano_mb
    
    def prestar(self):
        print(f"{self.titulo} siempre està disponible")
    
    def mostrar_info(self):
        print(f"{self.titulo} | {self.autor} | {self.anio} | Digital | {self.formato} | {self.tamano_mb}MB")

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"{libro.titulo} ha sido agregado a la biblioteca")
    
    def listarLibros(self):
        print("Lista de libros")
        for libro in self.libros:
            libro.mostrar_info()
    
    def buscarPorAutor(self, autor):
        encontrado = False
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libro.mostrar_info()
                encontrado = True
        if not encontrado:
            print("No se pudo encontrar al autor")

    def prestarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print("Libro no encontrado")

biblioteca = Biblioteca()

#Libros fìsicos
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

# Libros digitales
digital1 = LibroDigital("Python Básico", "Juan Pérez", 2022, "PDF", 5)

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(digital1)

biblioteca.listarLibros()

biblioteca.prestarLibro("1984")

for i in range(5):
    biblioteca.prestarLibro("Python Básico")

# ✔ Intentar prestar un libro ya prestado
biblioteca.prestarLibro("1984")

biblioteca.buscarPorAutor("Juan Pérez")      