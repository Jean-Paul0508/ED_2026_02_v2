import matplotlib.pyplot as plt


class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        ih = len(self.arreglo) - 1
        ip = ih // 2
        while self.arreglo[ip] > self.arreglo[ih]:
            self.arreglo[ip], self.arreglo[ih] = self.arreglo[ih], self.arreglo[ip]
            ih = ip
            ip = ip // 2
        if imagen:
            self.mostrar()

    def _bajar(self, ip):
        while 2*ip < len(self.arreglo):
            im = 2*ip
            if 2*ip + 1 < len(self.arreglo) and self.arreglo[2*ip + 1] < self.arreglo[im]:
                im = 2*ip + 1
            if self.arreglo[ip] > self.arreglo[im]:
                self.arreglo[ip], self.arreglo[im] = self.arreglo[im], self.arreglo[ip]
                ip = im
            else:
                break

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            return None
        minimo = self.arreglo[1]
        valor = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = valor
            self._bajar(1)
        if imagen:
            self.mostrar()
        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        for ip in range(len(lista) // 2, 0, -1):
            self._bajar(ip)
        if imagen:
            self.mostrar()

    def mostrar(self):
        a = self.arreglo
        n = len(a) - 1
        niveles = max(n.bit_length(), 1)
        fig, ax = plt.subplots(figsize=(max(4, 0.7 * 2 ** (niveles - 1)), 1.3 * niveles))
        pos = {}
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1
            pos[i] = ((i - 2 ** nivel + 0.5) / 2 ** nivel, -nivel)
        for i in range(2, n + 1):
            (x1, y1), (x2, y2) = pos[i // 2], pos[i]
            ax.plot([x1, x2], [y1, y2], color='black', zorder=1)
        for i in range(1, n + 1):
            x, y = pos[i]
            ax.text(x, y, str(a[i]), ha='center', va='center', zorder=2,
                    bbox=dict(boxstyle='circle', fc='lightblue', ec='black'))
        ax.set_ylim(-niveles + 0.4, 0.6)
        ax.set_xlim(0, 1)
        ax.axis('off')
        plt.show()
        
