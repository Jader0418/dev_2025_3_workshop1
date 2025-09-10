import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        j1 = jugador1.lower()
        j2 = jugador2.lower()
        reglas = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}
        opciones = reglas.keys()
        
        if j1 not in opciones or j2 not in opciones:
            return "invalid"
        if j1 == j2:
            return "empate"
        if reglas.get(j1) == j2:
            return "jugador1"
        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        return "correcto" if intento == numero_secreto else "muy alto" if intento > numero_secreto else "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        lineas_ganadoras = (
            [(i, 0) for i in range(3)], [(i, 1) for i in range(3)], [(i, 2) for i in range(3)],
            [(0, j) for j in range(3)], [(1, j) for j in range(3)], [(2, j) for j in range(3)],
            [(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]
        )
        
        for linea in lineas_ganadoras:
            x, y = linea[0]
            if tablero[x][y] != " " and all(tablero[x][y] == tablero[i][j] for i, j in linea):
                return tablero[x][y]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return random.choices(colores_disponibles, k=longitud)

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if tablero[desde_fila][desde_col] == tablero[hasta_fila][hasta_col] and tablero[hasta_fila][hasta_col] != " ":
            return False
        
        es_horizontal = desde_fila == hasta_fila
        es_vertical = desde_col == hasta_col
        
        if es_horizontal:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
        elif es_vertical:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
        else:
            return False

        return True