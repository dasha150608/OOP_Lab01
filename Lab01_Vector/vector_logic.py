import math

class Vector:
    def __init__(self, components):
        self.comp = list(components)
    def display(self):
        print(self.comp)
    def dim(self):
        return len(self.comp)
    def length(self):
        return math.sqrt(sum(x**2 for x in self.comp))
    def avg(self):
        return sum(self.comp)/len(self.comp) if self.comp else 0
    def mx(self):
        return max(self.comp) if self.comp else 0
    def mn(self):
        return min(self.comp) if self.comp else 0

def solve(file):
    vectors = []
    with open(file, 'r') as f:
        for line in f:
            if line.strip():
                vectors.append(Vector(map(float, line.split())))
    if not vectors: return
    v1 = max(vectors, key=lambda v: (v.dim(), -v.length()))
    v2 = max(vectors, key=lambda v: (v.length(), -v.dim()))
    avg_l = sum(v.length() for v in vectors) / len(vectors)
    count = sum(1 for v in vectors if v.length() > avg_l)
    v5 = max(vectors, key=lambda v: (v.mx(), -v.mn()))
    v6 = min(vectors, key=lambda v: (v.mn(), -v.mx()))
    print(f"1:{v1.comp}\n2:{v2.comp}\n3:{avg_l:.2f}\n4:{count}\n5:{v5.comp}\n6:{v6.comp}")
solve('input01.txt')
