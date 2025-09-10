import re

class Strings:
    def es_palindromo(self, texto):
        texto_limpio = "".join(filter(str.isalnum, texto)).lower()
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        return "".join(reversed(texto))

    def contar_vocales(self, texto):
        return sum(1 for char in texto.lower() if char in "aeiouáéíóú")

    def contar_consonantes(self, texto):
        vocales = "aeiouáéíóú"
        return sum(1 for char in texto.lower() if char.isalpha() and char not in vocales)

    def es_anagrama(self, texto1, texto2):
        t1_limpio = sorted(re.sub(r'[^a-zA-Z]', '', texto1.lower()))
        t2_limpio = sorted(re.sub(r'[^a-zA-Z]', '', texto2.lower()))
        return t1_limpio == t2_limpio

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())

    def es_numero_entero(self, texto):
        return texto.lstrip("+-").isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if 'a' <= char <= 'z':
                resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        return [i for i in range(len(texto)) if texto.startswith(subcadena, i)]
