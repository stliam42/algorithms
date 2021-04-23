class Stack:

    def __init__(self):
        self.__st = []

    def push(self, x):
        self.__st.append(x)

    def pop(self):
        return self.__st.pop() if self.size > 0 else 'error'

    @property
    def back(self):
        return self.__st[-1]  if self.size > 0 else 'error'

    @property
    def size(self):
        return len(self.__st)

    def clear(self):
        self.__st.clear()

    def __repr__(self):
        return str(self.__st)

    def __str__(self):
        return str(self.__st)


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

#n = int(input())
#train = tuple(map(int, input().split()))

n = 10
train = (1,9,6,3,4,5,2,8,7,10)

actions = sort_train(n,train)

if not actions:
    print(actions)
else:
    for action in actions:
        print(*action)

#n, x = map(int, input().split())
#a = tuple(map(int, input().split()))