from random import randint

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


def get_prefix_sum(a: list) -> list:
    prefix_sum = [0] * (len(a) + 1)

    for i in range(1, len(a) + 1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]

    return prefix_sum


def get_list_of_next_smaller_number_index(items: list) -> list:
    """
    Функция находит индексы меньших ближайщих элементов в направлении слева направо.
    a - входной список,
    inf - конструктивная бесконечность, должна быть меньше 
    меньшего элемента в массиве.
    Функция возвращает список.
    """
    
    inf = float('inf')
    items_with_barriers = [-inf] + items + [-inf]
    answer = [0] * (len(items) + 2)
    st = Stack(0)

    for i in range(1, len(items) + 2):
        while items_with_barriers[i] < items_with_barriers[st.back]:
            answer[st.pop()] = i - 1
        else:
            st.push(i)

    return answer[1:-1]


def line_land(n: int, a: tuple) -> list:
    """
    Великое Лайнландское переселение.

    Лайнландия представляет собой одномерный мир, являющийся прямой,
    на котором распологается N городов, последовательно пронумерованных
    от 0 до N− 1. Направление в сторону от первого города к нулевому 
    названо западным, а в обратную — восточным.

    Когда в Лайнландии неожиданно начался кризис, все жители одномерного
    мира стали испытывать глубокое смятение. По всей Лайнландии стали 
    ходить слухи, что на востоке живётся лучше, чем на западе.

    Так и началось Великое Лайнландское переселение. Обитатели мира 
    целыми городами отправились на восток, покинув родные улицы, 
    и двигались до тех пор, пока не приходили в город, в котором 
    средняя цена проживания была меньше, чем в родном.

    Входные данные:
    В первой строке дано одно число N (2 ≤N≤ 105) — количество городов
    в Лайнландии. Во второй строке даны N чисел ai (0 ≤ai≤ 109) — 
    средняя цена проживания в городах с нулевого по (N− 1)-й соответственно.

    Выходные данные:
    Для каждого города в порядке с нулевого по (N− 1)-й выведите номер
    города, в который переселятся его изначальные жители. Если жители 
    города не остановятся в каком-либо другом городе, отправившись в 
    Восточное Бесконечное Ничто, выведите −1.
"""
    inf = 1
    a = [-inf] + list(a) + [-inf]
    answer = [0] * (n + 2)
    st = Stack(0)
    for i in range(1, n + 2):
        while a[i] < a[st.back]:
            answer[st.pop()] = (i - 1) if i != (n + 1) else -1
        else:
            st.push(i)

    return answer[1:-1]


def get_greatest_rectangle_from_bar_graph(n: int, bars: tuple) -> int:
    """
    Гистограмма.

    Гистограмма является многоугольником, сформированным из 
    последовательности прямоугольников,выровненных на общей 
    базовой линии. Прямоугольники имеют равную ширину, но 
    могут иметь различные высоты. Например, фигура слева 
    показывает гистограмму, которая состоит из прямоугольников
    с высотами 2,1,4,5,1,3,3. Все прямоугольники на этом 
    рисунке имеют ширину, равную 1.

    Обычно гистограммы используются для представления дискретных
    распределений, например, частоты символов в текстах. Отметьте,
    что порядок прямоугольников очень важен. Вычислите область 
    самого большого прямоугольника в гистограмме, который также 
    находится на общей базовой линии. На рисунке справа 
    заштрихованная фигура является самым большим выровненным 
    прямоугольником на изображенной гистограмме.

    Входные данные:
    В первой строке входных данных записано число n (0<n≤106) — 
    количество прямоугольников гистограммы. Далее на той же 
    строке следуют n целых чисел h1, ..., hn, где 0≤hi≤10^9. 
    Эти числа обозначают высоты прямоугольников гистограммы 
    слева направо. Ширина каждого прямоугольника равна 1.

    Выходные данные:
    Выведите площадь самого большого прямоугольника в гистограмме. 
    Помните, что этот прямоугольник должен быть на общей базовой линии.
    """
    inf = -1
    bars = [inf] + list(a) + [inf]
    right = [0] * (n + 2)
    left = [0] * (n + 2)

    stack_right =  Stack(0)
    stack_left = Stack(0)

    answer = [0] * n
    for i in range(1, n + 2):
        while bars[i] < bars[stack_right.back]:
            right[stack_right.pop()] = i - 1
        else:
            stack_right.push(i)

    for j in range(n , -1, -1):
        while bars[j] < bars[stack_left.back]:
            left[stack_left.pop()] = j - 1
        else:
            stack_left.push(j)

    for i in range(1, n + 1):
        answer[i-1] = bars[i] * (right[i] - left[i] - 1)

    return max(answer)


def get_greatest_rectangle_with_width(n, bars: tuple) -> int:
    """
    Прямоугольники.

    Дана последовательность N прямоугольников различной ширины и высоты
    (wi,hi). Прямоугольники расположены, начиная с точки (0,0), 
    вправо на оси OX вплотную друг за другом. Требуется найти M — 
    площадь максимального прямоугольника (параллельного осям координат),
    который можно вырезать из этой фигуры.

    Формат входных данных:
    В первой строке задано число N (1≤N≤105). Далее идут N строк. 
    В каждой строке содержатся два числа: ширина и высота i-го 
    прямоугольника (1<wi≤3⋅10^4, 0≤hi≤3⋅10^4).

    Формат выходных данных:
    Выведите искомое число M.
    """
    WIDTH = 0
    HEIGHT = 1

    # Конструктивная бесконечность. Т.к. 
    # Все числа положительные, принимается "-1".
    inf = -1 

    # Массив с барьерными бесконечностями для 
    # вычисления индексов ближайщих меньших значений.
    bars = [(inf ,inf)] + list(a) + [(inf ,inf)]

    # Списки для индексов ближайщих меньших элементов 
    # для движения вправо и влево.
    right = [0] * (n + 2)
    left = [0] * (n + 2)

    # Стеки для работы с элементами
    stack_right =  Stack(0)
    stack_left = Stack(0)

    # Списки префиксных сумм и ответов.
    widths = [0] * (n + 2)
    answer = [0] * n

    # Считаем префиксные суммы ширин столбцов
    for i in range(1, n + 1):
        widths[i] = widths[i-1] + bars[i][WIDTH]
    # Находим индексы ближайших меньших элементов в 
    # направлении слева-направо
    for i in range(1, n + 2):
        while bars[i][HEIGHT] < bars[stack_right.back][HEIGHT]:
            right[stack_right.pop()] = i - 1
        else:
            stack_right.push(i)

    # Находим индексы ближайших меньших элементов в 
    # направлении справо-налево
    for j in range(n , -1, -1):
        while bars[j][HEIGHT] < bars[stack_left.back][HEIGHT]:
            left[stack_left.pop()] = j - 1
        else:
            stack_left.push(j)
    # Находим массив ответов путём перемножения высоты текущего столбца и 
    # суммы ширин ближайщих столбцов, которые не ниже текущего
    for i in range(1, n + 1):
        answer[i-1] = bars[i][HEIGHT] * (widths[right[i]] - widths[left[i] + 1])

    return max(answer) # Возвращаем самый большой прямоугольник из найденных.


def get_min_on_the_segment(number_of_elements: int,
                      window: int, 
                      items: list) -> list:
    """
    Минимум на отрезке.

    Рассмотрим последовательность целых чисел длины N. По ней с шагом 1
    двигается "окно" длины K, то есть сначала в "окне" видны первые 
    K чисел, на следующем шаге в "окне" уже будут находиться K чисел,
    начиная со второго, и так далее до конца последовательности. 
    Требуется для каждого положения "окна" определить минимум в нём.

    Использовать дерево отрезков запрещено.

    Входные данные:
    В первой строке входных данных содержатся два числа N и K 
    (1≤N≤150000, 1≤K≤10000, K≤N) — длины последовательности и "окна",
    соответственно. В следующей строке находятся N чисел — 
    сама последовательность.

    Выходные данные:
    Выходые данные должны содержать N−K+1 строк — минимумы для 
    каждого положения "окна".
    """
    min_list = get_list_of_next_smaller_number_index(items)
    results = [0] * (number_of_elements - window + 1)
    imin = 0

    for i in range(0, number_of_elements - window + 1):
        if imin < i:
            imin = i

        while min_list[imin] < i +  window:
              imin = min_list[imin]
        results[i] = imin

    return results #[items[i] for i in results]


def fortress(bars: list, gap: int) -> tuple:
    prefix_sum = get_prefix_sum(bars)
    min_segments = get_min_on_the_segment(len(bars), gap, bars)
    towers = [((prefix_sum[i+gap] - prefix_sum[i]) * bars[min_segments[i]])
             for i in range(0, len(bars) + 1 - gap)]

    defense = [0] * (len(bars) + 1)
    max_def_index = 0

    for i in range(gap, len(bars) + 1):
        defense[i] = max(defense[i-1], defense[i-gap] + towers[i-gap])
        if defense[i] > defense[max_def_index]:
            max_def_index = i
    
    answer = []
    defense = defense + [0]
    curr_def = defense[max_def_index]

    for i in range(len(defense) - 2, -1, -1):
        if defense[i] != defense[i+1] and defense[i+1] == curr_def:
            curr_def -= towers[i-gap+1]
            answer.append(i- gap + 2)

    return len(answer), answer[::-1]

#n, x = map(int, input().split())
#a = tuple(map(int, input().split()))
#n = 1
#a = [randint(1,10**6) for i in range(n)]
#gap = 1

#print(*fortress(a, gap), sep='\n')


n, gap = map(int, input().split())
a = list(map(int, input().split()))

answer = fortress(a, gap)

print(answer[0])
print(*answer[1])