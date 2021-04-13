"""Алгоритм Дейкстры по поиску кратчайшего расстояния в взвешенном графе."""

INF = float('inf')
graph = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['d'] = 3
graph['a']['e'] = 2

graph['b'] = {}
graph['b']['c'] = 1
graph['b']['d'] = 5
graph['b']['e'] = 7

graph['c'] = {}
graph['c']['a'] = 1
graph['c']['e'] = 4
graph['c']['g'] = 4

graph['d'] = {}
graph['d']['c'] = 5
graph['d']['h'] = 5
graph['d']['i'] = 6

graph['e'] = {}
graph['e']['f'] = 3
graph['e']['g'] = 3

graph['f'] = {}
graph['f']['h'] = 2
graph['f']['fin'] = 6

graph['g'] = {}
graph['g']['f'] = 2
graph['g']['i'] = 6

graph['h'] = {}
graph['h']['i'] = 1
graph['h']['fin'] = 4

graph['i'] = {}
graph['i']['fin'] = 2

graph['fin'] = {}


class Dijkstra:
    def __init__(self, graph:dict):
        # Создание графа
        self.graph = graph

        # Таблица крат. расстояний
        self.__create_costs()

        # Создание таблицы родителей
        self.__create_parents()

        # Список обработанных узлов
        self.processed = []

        # Самый "дешевый" путь
        self.shortest_route = ['fin']

    def __create_costs(self):
        """Создание таблицы кратчайших расстояний"""
        self.costs = {}
        self.costs['fin'] = INF
        for node in self.graph:
            if node == 'start':
                continue
            elif node in self.graph['start']:
                self.costs[node] = self.graph['start'][node]
            else:
                self.costs[node] = INF

    def __create_parents(self):
        """Создание таблицы родителей"""
        self.parents = {}
        for node in self.graph['start']:
            self.parents[node] = 'start'

    def search(self):
        """ Поиск кратчайшего пути. """
        node = self.__find_lowest_cost_node(self.costs)
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for i in neighbors.keys():
                new_cost = cost + neighbors[i]
                if self.costs[i] > new_cost:
                    self.costs[i] = new_cost
                    self.parents[i] = node
            self.processed.append(node)
            node = self.__find_lowest_cost_node(self.costs)
        self.__get_shortest_route()

    def __find_lowest_cost_node(self, costs: dict) -> str:
        """ Находит узел с наименьшей стоимостью из необработанных. """
        lowest_cost = INF
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if node not in self.processed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def __get_shortest_route(self):
        """Создаёт список с кратчайшим марштуром и стоимостью"""
        while True:
            try:
                node = self.parents[self.shortest_route[-1]]
                self.shortest_route.append(node)
            except:
                self.shortest_route.reverse()
                break


    def show_result(self):
        """ Печатает результаты. """
        print("Стоимости:")
        print(self.costs)
        print("Родители:")
        print(self.parents)
        print('Самый короткий путь:')
        print(self.shortest_route)
        print("Стоимость:")
        print(self.costs['fin'])


dijkstra = Dijkstra(graph)
dijkstra.show_result()
dijkstra.search()
dijkstra.show_result()
