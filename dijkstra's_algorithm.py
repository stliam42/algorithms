"""Алгоритм Дейкстры по поиску кратчайшего расстояния в взвешенном графе."""

INF = float('inf')

graph = {'start': {'a': 5, 'b': 2},
         'a': {'d': 3, 'e': 2},
         'b': {'c': 1, 'd': 5, 'e': 7},
         'c': {'a': 1, 'e': 4, 'g': 4},
         'd': {'c': 5, 'h': 5, 'i': 6},
         'e': {'f': 3, 'g': 3},
         'f': {'h': 2, 'fin': 6},
         'g': {'f': 2, 'i': 6},
         'h': {'i': 6, 'fin': 4},
         'i':{'fin': 2},
         'fin': {},
         }


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
        """Создание таблицы кратчайших расстояний.
        Для узлов, в которые можно перейти из начала задаётся вес.
        Для всех остальных узлов вес задаётся равным беспонечности."""
        self.costs = {}
        for node in self.graph:
            if node == 'start':
                continue
            elif node in self.graph['start']:
                self.costs[node] = self.graph['start'][node]
            else:
                self.costs[node] = INF

    def __create_parents(self):
        """Создание таблицы родителей.
        Для узлов, к котороым можно перейти из начала задаётся родитель.
        Остальные остаются пустыми."""
        self.parents = {}
        for node in self.graph['start']:
            self.parents[node] = 'start'

    def search(self):
        """ Поиск кратчайшего пути. """
        # Получаем самый "дешевый" узел, для работы в цикле.
        node = self.__find_lowest_cost_node(self.costs)

        # Пока есть необработанные узлы:
        while node is not None:
            # Получаем стоимость узла и его соседей.
            cost = self.costs[node]
            neighbors = self.graph[node]

            # Для всех соседей проверяем, является ли путь 
            # через выбранный узел кратчайшим.
            # Если да - меняем стоимость соседнего узла и 
            # заносим текущий узел, как его родителя.
            for i in neighbors.keys():
                new_cost = cost + neighbors[i]
                if self.costs[i] > new_cost:
                    self.costs[i] = new_cost
                    self.parents[i] = node

            # Помечаем узел, как обработанный и получаем новый узел.
            self.processed.append(node)
            node = self.__find_lowest_cost_node(self.costs)

        # После обработки всех узлов получаем кратчайший маршрут.
        self.__get_shortest_route()

    def __find_lowest_cost_node(self, costs: dict) -> str:
        """ Находит узел с наименьшей стоимостью из необработанных. """
        lowest_cost = INF
        lowest_cost_node = None
        # Для каждого узла вычисляется стоимость и происходит проверка, обработан он или нет.
        # Если стоимость текущего узла меньше, чем предыдущего - минимум обновляется.
        # После прохождения всех узлов мы гарантированно получаем еще 
        # необработанный узел с минимальной стоимостью.
        for node in costs:
            cost = costs[node]
            if node not in self.processed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node

    def __get_shortest_route(self):
        """Создаёт список с кратчайшим марштуром и стоимостью."""
        while True:
            try:
                # Поочередно получаем родителей узлов и 
                # заносим их в кратчайший путь.
                node = self.parents[self.shortest_route[-1]]
                self.shortest_route.append(node)
            except:
                # После того, как дошли до старта 
                # (будет возбуждено исключание, ибо у старта нет родителя), 
                # разворачиваем список, так как ты двигались от конца к началу.
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
