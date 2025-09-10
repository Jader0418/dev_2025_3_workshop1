class Data:
    def invertir_lista(self, lista):
        nueva = []
        for elemento in lista:
            nueva.insert(0, elemento)
        return nueva

    def buscar_elemento(self, lista, elemento):
        try:
            return lista.index(elemento)
        except ValueError:
            return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        elementos_vistos = {}
        for elemento in lista:
            if elemento not in elementos_vistos:
                elementos_vistos[elemento] = True
                resultado.append(elemento)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        from itertools import chain
        return sorted(chain(lista1, lista2))

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        n = len(lista)
        k = k % n
        return lista[n-k:] + lista[:n-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_actual = 0
        for num in lista:
            suma_actual += num
        suma_total = sum(range(1, n + 1))
        return suma_total - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        if not conjunto1:
            return True
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []
        class Pila:
            def push(self, elemento):
                pila.append(elemento)
            def pop(self):
                return pila.pop() if pila else None
            def peek(self):
                return pila[-1] if pila else None
            def is_empty(self):
                return not pila
        return Pila()

    def implementar_cola(self):
        from collections import deque
        cola = deque()
        class Cola:
            def enqueue(self, elemento):
                cola.append(elemento)
            def dequeue(self):
                return cola.popleft() if cola else None
            def peek(self):
                return cola[0] if cola else None
            def is_empty(self):
                return not cola
        return Cola()

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [list(fila) for fila in zip(*matriz)] 