"""Алгоритм Дейкстры по поиску кратчайшего расстояния в взвешенном графе."""

INF = float('inf')
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

class Dijkstra:
    def __init__(self, graph:dict):
        # Создание графа
        self.graph = graph

        # Создание таблицы кратчайших расстояний
        self.costs = {}
        for node in self.graph:
            if node == 'start':
                continue
            elif node in self.graph['start']:
                self.costs[node] = self.graph['start'][node]
            else:
                self.costs[node] = INF

        # Создание таблицы родителей
        self.parents = {}
        self.parents['a'] = 'start'
        self.parents['b'] = 'start'
        self.parents['in'] = None

        # Список обработанных узлов
        self.processed = []

    def search(self):
        """ Поиск кратчайшего пути. """
        node = self._find_lowest_cost_node(self.costs)
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for i in neighbors.keys():
                new_cost = cost + neighbors[i]
                if self.costs[i] > new_cost:
                    self.costs[i] = new_cost
                    self.parents[i] = node
            self.processed.append(node)
            node = self._find_lowest_cost_node(self.costs)

    def _find_lowest_cost_node(self, costs: dict) -> str:
        """ Находит узел с наименьшей стоимостью из необработанных. """
        lowest_cost = INF
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if node not in self.processed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def show_result(self):
        """ Печатает результаты. """
        print("Стоимости:")
        print(self.costs)
        print("Родители:")
        print(self.parents)

dijkstra = Dijkstra(graph)
dijkstra.show_result()
dijkstra.search()
dijkstra.show_result()