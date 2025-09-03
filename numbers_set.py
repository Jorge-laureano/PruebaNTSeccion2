import random

class NumbersSet:
    def __init__(self):
        self.numbers = list(range(1, 101))
        self.extracted = None

    def extract(self, num=None):
        """Extrae un número específico o aleatorio del conjunto."""
        if num:
            if not isinstance(num, int) or num < 1 or num > 100:
                raise ValueError("El número debe estar entre 1 y 100")
            self.extracted = num
        else:
            self.extracted = random.choice(self.numbers)
        return self.extracted

    def missing_number(self):
        """Devuelve el número faltante."""
        return self.extracted

    def get_grid(self):
        """Devuelve los 100 números y marca el faltante."""
        grid = []
        for n in self.numbers:
            if n == self.extracted:
                grid.append(f"[{n}]")  # Marca el número faltante
            else:
                grid.append(str(n))
        return grid
