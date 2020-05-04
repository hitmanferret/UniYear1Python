class Vector(object):
    def __init__(self, data = None):
        if data != None:
            self._vector = [float(i) for i in data]
        else:
            self._vector = []

    def __str__(self):
        string_vector = "<"
        if self._vector == []:
            string_vector = "<>"
        else:
            for i in self._vector:
                if i < len(self._vector):
                    string_vector += (str(i) + ", ")
                else:
                    string_vector += (str(i) + ">")
        return string_vector

    def dim(self):
        dimension = len(self._vector)
        return dimension

    def get(self, index):
        return self._vector[index]
    
    def set(self, index, value):
        self._vector[index] = value
    
    def scalar_product(self, scalar):
        if self._vector == []:
            scalar_vector = []
        else:
            scalar_vector = [(i * scalar) for i in self._vector]
        return Vector(scalar_vector)

    def add(self, other_vector):
        if isinstance(other_vector, Vector):
            if len(self._vector) == len(other_vector._vector):
                add_vector = []
                for i in range(len(self._vector)):
                    add_vector.append(self._vector[i] + other_vector._vector[i])
                return Vector(add_vector)
            else:
                raise ValueError
        else:
            raise TypeError

    def equals(self, other_vector):
        if isinstance(other_vector, Vector):
            if other_vector._vector == self._vector:
                return True
            else:
                return False
        else:
            return False
        