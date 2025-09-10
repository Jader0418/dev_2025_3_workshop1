class Magic:

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        if n in {0, 1}:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        
        secuencia = [0]
        if n > 1:
            secuencia.append(1)
            for _ in range(2, n):
                secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia
    
    def es_primo(self, n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        if n < 2:
            return []
        
        es_primo = [True] * (n + 1)
        es_primo[0] = es_primo[1] = False
        
        for p in range(2, int(n**0.5) + 1):
            if es_primo[p]:
                for i in range(p * p, n + 1, p):
                    es_primo[i] = False
        
        return [i for i, es in enumerate(es_primo) if es]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        
        suma = sum([i for i in range(1, int(n**0.5) + 1) if n % i == 0 for i in [i, n // i]])
        suma -= n + n*0.5 if n 0.5 == int(n*0.5) else 0

        return suma == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n <= 1:
            return 1
        
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        from math import gcd
        return gcd(a, b)

    def mcm(self, a, b):
        from math import gcd
        return abs(a * b) // gcd(a, b) if a and b else 0

    def suma_digitos(self, n):
        return sum(int(digito) for digito in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        s = str(n)
        return sum(int(digito)**len(s) for digito in s) == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        
        suma_objetivo = sum(matriz[0])
        
        filas_validas = all(sum(fila) == suma_objetivo for fila in matriz)
        columnas_validas = all(sum(matriz[fila][col] for fila in range(n)) == suma_objetivo for col in range(n))
        
        diagonal1 = sum(matriz[i][i] for i in range(n)) == suma_objetivo
        diagonal2 = sum(matriz[i][n - 1 - i] for i in range(n)) == suma_objetivo
        
        return filas_validas and columnas_validas and diagonal1 and diagonal2