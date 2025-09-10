class Logica:
    def AND(self, a, b):
        return a and b

    def OR(self, a, b):
        if not a:
            return b
        return True

    def NOT(self, a):
        return not a

    def XOR(self, a, b):
        return a != b

    def NAND(self, a, b):
        return not a or not b

    def NOR(self, a, b):
        if a or b:
            return False
        return True

    def XNOR(self, a, b):
        return a == b
    
    def implicacion(self, a, b):
        if a and not b:
            return False
        return True

    def bi_implicacion(self, a, b):
        if a:
            return b
        return not b