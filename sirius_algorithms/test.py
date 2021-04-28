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

    return results

def fortress(bars: list, gap: int) -> tuple:
    """
    Башня.

    Петя в очередной раз купил себе набор из кубиков. 
    На этот раз он выстроил из них настоящую крепость — 
    последовательность из N столбиков, высота каждого 
    столбика составляет Ai кубиков.

    Вскоре ему стало интересно, насколько его крепость 
    защищена от жуликов и воров. Для этого он ввел понятие
    башни. Башней называется любая последовательность из 
    K столбиков подряд (где K — любимое число Пети). 
    Защищённость башни определяется как суммарная высота 
    всех столбиков этой башни (чем она больше, тем громаднее
    и ужаснее она кажется), умноженная на минимум высоты 
    столбиков башни (т.к. враги, очевидно, будут пытаться 
    проникнуть через самое слабое место башни). 
    Неприступность крепости определяется как сумма 
    защищённостей каждой из башен.

    Петя решил как можно скорее посчитать, какова же 
    неприступность его крепости. Однако вскоре он понял,
    что недостаточно знать высоту каждого из столбиков. 
    В зависимости от того, как сгруппировать столбики в башни,
    получится разный результат. В различных вариантах группировки
    часть столбиков могут не принадлежать ни одной из башен. 
    Разумеется, Петя выберет то разбиение на башни, при котором
    неприступность будет максимальна.

    Петя успешно справился со своей задачей, но теперь 
    Правительство Флатландии решило защитить свой горный курорт.
    Правительство уже построило крепость из кубиков (просто кубики
    были побольше). Теперь вы должны помочь Правительству посчитать
    неприступность этой крепости. Единственная трудность состоит 
    в том, что у Правительства было очень много денег, и поэтому 
    крепость была построена очень длинная.

    Входные данные:
    В первой строке содержатся число N — количество столбиков в 
    крепости и число K — любимое число Пети (1 ≤ K ≤ N ≤ 100 000).
    Далее в следующей строке содержатся N целых чисел, 
    обозначающих Ai (1 ≤ Ai ≤ 10^6).

    Выходные данные:
    В первой строке выведите число Q — количество башен в 
    оптимальном разбиении. Далее выведите Q чисел — номера 
    первых столбиков каждой башни.
    """
    prefix_sum = get_prefix_sum(bars)
    min_segments = get_min_on_the_segment(len(bars), gap, bars)
    towers = [((prefix_sum[i+gap] - prefix_sum[i]) * bars[min_segments[i]])
             for i in range(0, len(bars) + 1 - gap)]
    towers = towers
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
    
n, gap = map(int, input().split())
a = list(map(int, input().split()))

answer = fortress(a, gap)

print(answer[0])
print(*answer[1])