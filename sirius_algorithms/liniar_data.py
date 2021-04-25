from collections import deque
from math import ceil
from random import choice

class Stack(list):

    def __init__(self, *values):
        if not values:
            pass
        else:
            for i in values:
                self.push(i)

    def push(self, x):
        self.append(x)

    @property
    def back(self):
        return self[-1]  if self.size > 0 else 'error'

    @property
    def size(self):
        return len(self)


class MinStack(Stack):

    def __init__(self, *values):
        self.__min = []
        if not values:
            pass
        else:
            super().__init__(*values)

    def push(self, x):
        self.append(x)
        self.__min.append(self.__min[-1] 
                            if self.__min and x > self.__min[-1] 
                            else x)

    @property
    def min(self):
        return self.__min[-1] if self.size else 'error'

    def pop(self):
        self.__min.pop()
        return super().pop()

    def clear(self):
        self.__min.clear()
        super().clear()


class Queue:
    
    def __init__(self, *values):
        self._stack_in = Stack(*values)
        self._stack_out = Stack()

    def push(self, n):
        self._stack_in.push(n)

    def pop(self):
        if self._stack_in or self._stack_out:
            if not self._stack_out:
                while self._stack_in.size != 0:
                    self._stack_out.push(self._stack_in.pop())
            return self._stack_out.pop()
        else: 
            return 'error'

    @property
    def front(self):
        if self._stack_in or self._stack_out:
            if not self._stack_out:
                while self._stack_in.size != 0:
                    self._stack_out.push(self._stack_in.pop())
            return self._stack_out.back
        else: 
            return 'error'

    @property
    def size(self):
        return self._stack_in.size + self._stack_out.size

    def clear(self):
        self._stack_in.clear()
        self._stack_out.clear()

    def __str__(self):
        return str(self._stack_out[::-1] + self._stack_in)

    def __repr__(self):
        return str(self._stack_out[::-1] + self._stack_in)

    def __bool__(self):
        return bool(self.size)


class MinQueue(Queue):

    def __init__(self, *values):
        super().__init__()
        self._stack_in = MinStack(*values)
        self._stack_out = MinStack()

    @property
    def min(self):
        if self._stack_in and self._stack_out:
            return min(self._stack_in.min, self._stack_out.min)
        elif self._stack_in:
            return self._stack_in.min
        elif self._stack_out:
            return self._stack_out.min
        else:
            return 'error'


def analyze_brackets(brackets: str) -> str:
    """
    Правильная скобочная последовательность.

    Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных
    скобок. Программа должна определить, является ли данная скобочная 
    последовательность правильной.

    Пустая последовательность является правильной. Если A правильная, 
    то последовательности (A), [A], {A} правильные. Если A и B правильные 
    последовательности, то последовательность AB правильная.

    Входные данные:
    В единственной строке записана скобочная последовательность, 
    содержащая не более 100000 скобок.

    Выходные данные:
    Если данная скобочная последовательность правильная, 
    то программа должна вывести строку yes, иначе — строку no.
    """
    right = False
    st = Stack()
    bracket_dict = {
                    ')': '(',
                    ']': '[',
                    '}': '{',
                    }

    for bracket in brackets:
        if bracket in ('(', '[', '{'):
            st.push(bracket)
        else:
            if st.back == bracket_dict[bracket]:
                st.pop()
            else:
                st.push(bracket)
                break
       

    if st.size == 0:
        right = True

    return 'yes' if right else 'no'

def postfix_notation(string:str) -> int:
    """
    Постфиксная запись.

    В постфиксной записи (или обратной польской записи) операция записывается
    после двух операндов. Например, сумма двух чисел A и B записывается 
    как A B +. Запись B C + D ∗ обозначает привычное нам (B+C)∗D, а запись 
    A B C + D ∗ + означает A+(B+C)∗D. Достоинство постфиксной записи в том, 
    что она не требует скобок и дополнительных соглашений о приоритете 
    операторов для своего чтения — все операции выполняются подряд слева направо.

    Входные данные:
    В единственной строке записано выражение в постфиксной записи, содержащее 
    цифры и операции +, −, ∗. Цифры и операции разделяются пробелами. В конце 
    строки может быть произвольное количество пробелов.

    Выходные данные:
    Необходимо вывести значение записанного выражения. Гарантируется, 
    что результат по модулю не превосходит 2⋅109.
    """
    st = Stack()
    result = 0
    operation = {'+': lambda x, y: x + y,
                 '-': lambda x, y: y - x,
                 '*': lambda x, y: x * y}

    for item in string:
        if item in operation.keys():
            st.push(operation[item](int(st.pop()), int(st.pop())))
        else:
            st.push(item)

    return st.pop()
         
def sort_train(number_of_carriage: int,
               carriages: tuple):
    """
    Сортировка вагонов.

    К тупику со стороны пути 1 (см. рисунок) подъехал поезд. 
    Разрешается отцепить от поезда один или сразу несколько 
    первых вагонов и завезти их в тупик (при желании можно 
    даже завезти в тупик сразу весь поезд). После этого часть 
    из этих вагонов вывезти в сторону пути 2. После этого 
    можно завезти в тупик ещё несколько вагонов и снова часть 
    оказавшихся вагонов вывезти в сторону пути 2. И так далее 
    (так, что каждый вагон может лишь один раз заехать с пути 
    1 в тупик, а затем один раз выехать из тупика на путь 2). 
    Заезжать в тупик с пути 2 или выезжать из тупика на путь 1 
    запрещается. Нельзя с пути 1 попасть на путь 2, не заезжая в тупик.

    Известно, в каком порядке изначально идут вагоны поезда. Требуется 
    с помощью указанных операций сделать так, чтобы вагоны поезда шли по 
    порядку (сначала первый, потом второй и т.д., считая от головы поезда,
    едущего по пути 2 в сторону от тупика).

    Входные данные:
    В первой строке входных данных находится число N — количество вагонов 
    в поезде (1≤N≤2000). Во второй строке через пробел идут номера вагонов 
    в порядке от головы поезда, едущего по пути 1 в сторону тупика. 
    Вагоны пронумерованы натуральными числами от 1 до N, каждое из которых 
    встречается ровно один раз.

    Выходные данные:
    Если сделать так, чтобы вагоны шли в порядке от 1 до N, считая от головы 
    поезда, когда поезд поедет по пути 2 из тупика, можно, то выведите действия,
    которые нужно проделать с поездом, каждое в отдельной строке. 

    Каждое действие описывается двумя числами: 
    типом и количеством вагонов:
    если нужно завезти с пути 1 в тупик K вагонов, должно быть выведено 
    сначала число 1, а затем — число K (K≥1),
    если нужно вывезти из тупика на второй путь K вагонов, должно быть 
    выведено сначала число 2, а затем — число K (K≥1).

    Если возможно несколько последовательностей действий, приводящих 
    к нужному результату, выведите любую из них.

    Если выстроить вагоны по порядку невозможно, выведите одно число 0.
    """
    st = Stack()
    path2 = []
    ok = False
    go = True
    i = 0
    carriages_to_move = [0, 0]
    actions = []

    while go:
        if i < number_of_carriage:
            carriage = carriages[i]

            if st.size == 0 or carriage < st.back:
                st.push(carriage)
                i += 1

                if carriages_to_move[1]:
                    actions.append((2, carriages_to_move[1]))
                    carriages_to_move[1] = 0

                carriages_to_move[0] += 1

            elif carriage > st.back:
                if path2 and st.back - path2[-1] > 1:
                    break
                path2.append(st.pop())

                if carriages_to_move[0]:
                    actions.append((1, carriages_to_move[0]))
                    carriages_to_move[0] = 0

                carriages_to_move[1] += 1

        else:
            if st.size == 0:
                go = False
            elif not path2 or path2[-1] < st.back:
                if path2 and st.back - path2[-1] > 1:
                    break
                path2.append(st.pop())

                if carriages_to_move[0]:
                    actions.append((1, carriages_to_move[0]))
                    carriages_to_move[0] = 0

                carriages_to_move[1] += 1

            else:
               go = False
    else:
        actions.append((2, carriages_to_move[1]))
        ok = True if st.size == 0 else False

    return actions if ok else 0

class Drankard:

    def __init__(self, 
                 first_start: tuple,
                 second_start: tuple):

        self.first_player_deck = Queue(first_start)
        self.second_player_deck = Queue(second_start)

        self.play = True
        self.turns = 0

    def match(self):

        while self.play:
            if not self.first_player_deck or not self.second_player_deck or self.turns >= 10 ** 6:
                self.play = False
            else:
                self.turns += 1
                first_player_card = self.first_player_deck.pop()
                second_player_card = self.second_player_deck.pop()

                if first_player_card > second_player_card:
                    if first_player_card == 9 and second_player_card == 0:
                        self.second_player_deck.push(first_player_card)
                        self.second_player_deck.push(second_player_card)
                    else:
                        self.first_player_deck.push(first_player_card)
                        self.first_player_deck.push(second_player_card)
                else:
                    if first_player_card == 0 and second_player_card == 9:
                        self.first_player_deck.push(first_player_card)
                        self.first_player_deck.push(second_player_card)
                    else:
                        self.second_player_deck.push(first_player_card)
                        self.second_player_deck.push(second_player_card)
        else:
            self.results()

    def results(self):
        if self.first_player_deck:
            print('first {}'.format(self.turns))
        elif self.second_player_deck:
            print('second {}'.format(self.turns))
        else:
            print('botva')


def goblins_queue(numbers_of_goblins: int, goblin_actions: tuple):
    """
    Гоблины и шаманы.

    Гоблины Мглистых гор очень любях ходить к своим шаманам. Так как гоблинов
    много, к шаманам часто образуются очень длинные очереди. А поскольку 
    много гоблинов в одном месте быстро образуют шумную толку, которая мешает 
    шаманам проводить сложные медицинские манипуляции, последние решили 
    установить некоторые правила касательно порядка в очереди.

    Обычные гоблины при посещении шаманов должны вставать в конец очереди. 
    Привилегированные же гоблины, знающие особый пароль, встают ровно в ее 
    середину, причем при нечетной длине очереди они встают сразу за центром.

    Так как гоблины также широко известны своим непочтительным отношением 
    ко всяческим правилам и законам, шаманы попросили вас написать программу,
    которая бы отслеживала порядок гоблинов в очереди.

    Входные данные:
    В первой строке входных данный записано число N (1≤N≤10^5) — количество 
    запросов к программе. Следующие N строк содержат описание запросов в формате:

    "+ i" — гоблин с номером i (1≤i≤N) встает в конец очереди.
    "* i" — привилегированный гоблин с номером i встает в середину очереди.
    "-" — первый гоблин из очереди уходит к шаманам. Гарантируется, что на момент 
    такого запроса очередь не пуста.

    Выходные данные:
    Для каждого запроса типа "-" программа должна вывести номер гоблина, 
    который должен зайти к шаманам.
    """
    left = deque()
    right = deque()
    for action in goblin_actions:
        if action.startswith('+'):
            right.append(action.split()[1])
        elif action.startswith('*'):
            right.appendleft(action.split()[1])
        else:
            print(left.popleft())

        if len(right) > len(left):
            left.append(right.popleft())


n = 7
g = ('+ 1', '+ 2', '-', '* 3', '* 4', '-', '-')

n = int(input())
g = []
number = 1
req = 0
for i in range(n):
    action = choice(('+ {}'.format(number), '* {}'.format(number), '-') if len(g) - req > len(g)/2 else ('+ {}'.format(number), '* {}'.format(number)))
    number = number if action == '-' else number + 1
    if action == '-':
        req += 1
    g.append(action)

goblins_queue(n, g)
#n, x = map(int, input().split())
#a = tuple(map(int, input().split()))