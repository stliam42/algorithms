"""Алгоритм Дейкстры по поиску кратчайшего расстояния в взвешенном графе."""

inf = float('inf')

class Dijkstra:
    def __init__(self):
        # Создание графа
        self.graph = {}
        self.graph['start'] = {}
        self.graph['start']['a'] = 6
        self.graph['start']['b'] = 2
        self.graph['a'] = {}
        self.graph['a']['fin'] = 1
        self.graph['b'] = {}
        self.graph['b']['a'] = 3
        self.graph['b']['fin'] = 5
        self.graph['fin'] = {}

        # Создание таблицы кратчайших расстояний
        self.costs = {}
        self.costs['a'] = 6
        self.costs['b'] = 2
        self.costs['fin'] = inf

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
        lowest_cost = inf
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if node not in self.processed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def show_result(self):
        """ Печатает результаты. """
        print("Стоимости - " + str(self.costs))
        print("Родители - " + str(self.parents))

dijkstra = Dijkstra()
dijkstra.show_result()
dijkstra.search()
dijkstra.show_result()
