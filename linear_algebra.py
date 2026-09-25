from .basic import abs_val, sqrt


class Vector:
    def __init__(self, components):
        self.data = list(components)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Размеры не совпадают")
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.data])
    __rmul__ = __mul__

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self):
        return sqrt(self.dot(self))

    def cross(self, other):
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross только для 3D-векторов")
        a, b = self.data, other.data
        return Vector([
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ])

    def __repr__(self):
        return f"Vector({self.data})"


class Matrix:
    def __init__(self, rows):
        self.rows = [list(r) for r in rows]
        self.n = len(self.rows)
        self.m = len(self.rows[0]) if self.n else 0

    def __getitem__(self, i):
        return self.rows[i]

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError("Несовместимые размеры")
        result = [[0] * other.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                result[i][j] = sum(self.rows[i][k] * other.rows[k][j]
                                   for k in range(self.m))
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.rows[i][j] for i in range(self.n)]
                       for j in range(self.m)])

    def det(self):
        if self.n != self.m:
            raise ValueError("Определитель только для квадратных матриц")
        if self.n == 1:
            return self.rows[0][0]
        if self.n == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        result = 0
        for j in range(self.n):
            minor = [[self.rows[i][k] for k in range(self.n) if k != j]
                     for i in range(1, self.n)]
            result += ((-1) ** j) * self.rows[0][j] * Matrix(minor).det()
        return result

    def __repr__(self):
        return "Matrix(\n  " + "\n  ".join(str(r) for r in self.rows) + "\n)"