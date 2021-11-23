class Edge:
    def __init__(self, vertex1_value, vertex2_value, weight):
        self.vertex1 = vertex1_value
        self.vertex2 = vertex2_value
        self.weight = weight


class Graph:
    def __init__(self):
        self.edges = []
        self.__found_dist = False
        self.distance_dict = {}
        self.start_point = None

    def add_to_the_graph(self, v1, v2, w=0):
        if not self.edges:
            self.distance_dict[v1] = 0
            self.start_point = v1
            self.distance_dict[v2] = float("inf")
        else:
            if (v1 != self.start_point) and (v2 != self.start_point):
                self.distance_dict[v1] = float("inf")
                self.distance_dict[v2] = float("inf")
        self.edges.append(Edge(v1, v2, w))

    def relaxation(self):
        for i in range(len(self.edges)-1):
            for edge in self.edges:
                if self.distance_dict.get(edge.vertex1) != float("inf") and self.distance_dict.get(edge.vertex1) + edge.weight < self.distance_dict.get(edge.vertex2):
                    self.distance_dict[edge.vertex2] = self.distance_dict[edge.vertex1] + edge.weight

        for edge in self.edges:
            if self.distance_dict.get(edge.vertex1) != float("inf") and self.distance_dict[edge.vertex1] + edge.weight < self.distance_dict[edge.vertex2]:
                raise Exception("Graph has a negative-weight cycle")
        self.__found_dist = True

    def print_all_distances(self):
        if self.__found_dist:
            print(self.distance_dict)
            return self.distance_dict


if __name__ == '__main__':
    graph = Graph()
    print("Bellman–Ford algorithm: result")

    graph.add_to_the_graph(5, 6, -5)
    graph.add_to_the_graph(4, 2, -2)
    graph.add_to_the_graph(3, 8, -1)
    graph.add_to_the_graph(1, 2, -2)
    graph.add_to_the_graph(6, 4, -5)
    graph.add_to_the_graph(6, 1, -3)

    graph.relaxation()
    a = graph.print_all_distances()

