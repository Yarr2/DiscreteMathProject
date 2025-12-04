class Graph:
    def __init__(self, vertices : list):
        self.vertices = vertices
        self.number_of_vertices = len(vertices)
        self.matrix = []
        for _ in vertices:
            temp = []
            for _ in vertices:
                temp.append(0)
            self.matrix.append(temp)

    def add_edge(self,vertice_1,vertice_2) -> bool:
        if not(vertice_1 in self.vertices and vertice_2 in self.vertices):
            return False
        self.matrix[vertice_1][vertice_2] = 1
        self.matrix[vertice_2][vertice_1] = 1
        return True

    def remove_edge(self,vertice_1,vertice_2):
        if not (vertice_1 in self.vertices and vertice_2 in self.vertices):
            return False
        self.matrix[vertice_1][vertice_2] = 0
        self.matrix[vertice_2][vertice_1] = 0
        return True

    def add_vertice(self,vertice):
        self.vertices.append(vertice)
        self.number_of_vertices += 1

