class Boxeador:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        self.categoria = self.get_categoria()

    def get_categoria(self):
        categorias = {
            (48, 51): "Mosca",
            (51, 54): "Gallo",
            (54, 57): "Pluma",
            (57, 60): "Ligero",
            (60, 66): "Walter",
            (66, 69): "Medio",
            (69, 75): "Semi pesado",
            (75, 91): "Pesado",
            (91, 100): "Super pesado",
        }
        for rango, categoria in categorias.items():
            if rango[0] <= self.peso <= rango[1]:
                return categoria
        raise ValueError(f"Peso {self.peso} no está en ninguna categoría")

def generar_enfrentamientos(boxeadores):
    enfrentamientos = []
    for categoria in set(boxeador.categoria for boxeador in boxeadores):
        boxeadores_categoria = [boxeador for boxeador in boxeadores if boxeador.categoria == categoria]
        import random
        random.shuffle(boxeadores_categoria)
        for i in range(0, len(boxeadores_categoria), 2):
            if i + 1 < len(boxeadores_categoria):
                enfrentamientos.append((boxeadores_categoria[i].nombre, boxeadores_categoria[i + 1].nombre))
    return enfrentamientos

# Ejemplo de uso
boxeadores = [
    Boxeador("Juan Pérez", 52),
    Boxeador("Ana González", 63),
    Boxeador("Pedro López", 72),
    Boxeador("María Martínez", 50),
    Boxeador("Carlos García", 85),
]

for boxeador in boxeadores:
    print(f"{boxeador.nombre} - Categoría: {boxeador.categoria}")

print("\n--- Enfrentamientos ---")

for enfrentamiento in generar_enfrentamientos(boxeadores):
    print(f"{enfrentamiento[0]} vs {enfrentamiento[1]}")
