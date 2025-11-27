class Graph:
    def __init__(self, vertices : list, edges : list):
        self.number_of_vertices = len(vertices)
        self.matrix = []
        for _ in vertices:
            temp = []
            for _ in vertices:
                temp.append(0)
            self.matrix.append(temp)