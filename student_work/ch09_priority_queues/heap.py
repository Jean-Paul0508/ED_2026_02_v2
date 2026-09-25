class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i // 2] > self.arreglo[i]:
            self.arreglo[i // 2], self.arreglo[i] = (
                self.arreglo[i],
                self.arreglo[i // 2],
            )
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        min_val = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            i = 1
            n = len(self.arreglo) - 1
            while 2 * i <= n:
                hijo_izq = 2 * i
                hijo_der = 2 * i + 1
                menor = i

                if (
                    hijo_izq <= n
                    and self.arreglo[hijo_izq] < self.arreglo[menor]
                ):
                    menor = hijo_izq
                if (
                    hijo_der <= n
                    and self.arreglo[hijo_der] < self.arreglo[menor]
                ):
                    menor = hijo_der

                if menor != i:
                    self.arreglo[i], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[i],
                    )
                    i = menor
                else:
                    break

        return min_val

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1
        for i in range(n // 2, 0, -1):
            curr = i
            while 2 * curr <= n:
                hijo_izq = 2 * curr
                hijo_der = 2 * curr + 1
                menor = curr

                if (
                    hijo_izq <= n
                    and self.arreglo[hijo_izq] < self.arreglo[menor]
                ):
                    menor = hijo_izq
                if (
                    hijo_der <= n
                    and self.arreglo[hijo_der] < self.arreglo[menor]
                ):
                    menor = hijo_der

                if menor != curr:
                    self.arreglo[curr], self.arreglo[menor] = (
                        self.arreglo[menor],
                        self.arreglo[curr],
                    )
                    curr = menor
                else:
                    break
