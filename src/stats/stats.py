import math
from collections import Counter

class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        return (numeros_ordenados[n // 2] + numeros_ordenados[(n - 1) // 2]) / 2

    def moda(self, numeros):
        if not numeros:
            return None
        
        counts = Counter(numeros)
        max_count = max(counts.values())
        
        for numero in numeros:
            if counts[numero] == max_count:
                return numero
        return None

    def desviacion_estandar(self, numeros):
        if len(numeros) < 2:
            return 0.0

        n = len(numeros)
        promedio = sum(numeros) / n
        varianza = sum((x - promedio) ** 2 for x in numeros) / n
        return math.sqrt(varianza)
    
    def varianza(self, numeros):
        if not numeros:
            return 0.0

        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)

    def rango(self, numeros):
        if not numeros:
            return 0
        
        numeros_copia = sorted(numeros)
        return numeros_copia[-1] - numeros_copia[0]
