def calc_house_point(a: int, b: int, d: int) -> int:
    """
    Вася строит дом.

    Мальчик Вася живёт на координатной прямой. На этой прямой в точке A
    располагается школа, а в точке B — любимый Васин компьютерный клуб. 
    Также в точках …,−d,0,d,…,k⋅d,…, где k — произвольное целое число,
    а d — чётное натуральное число, расположены киоски с мороженым. 
    Вася хочет построить дом в некоторой точке с целой координатой. 
    При этом, ему хочется, чтобы расстояние от дома до школы и от дома 
    до компьютерного клуба было одинаковым. Если это вдруг невозможно, 
    то он хочет, чтобы сумма этих расстояний была как можно меньше, 
    а также чтобы расстояния отличались как можно меньше друг от друга.
    Если под Васин дом подходит несколько вариантов точек, то он выберет ту,
    расстояние от которой до ближайшего киоска с мороженым минимально. 
    Помогите Васе выбрать точку, где строить дом, а также выведите расстояние 
    до ближайшего киоска с мороженым. Вася может строить дом в точке, где уже 
    есть другие строения.

    Входные данные:
    В единственной строке входных данных заданы три числа — A, B и d. 
    Гарантируется, что A и B — целые числа, по модулю не превышающие 
    2*10^9, A≠B. d — чётное натуральное число, 2≤d≤2⋅10^9.

    Выходные данные:
    В единственной строке выходных данных выведите два целых числа — 
    координату точки, где Васе необходимо построить дом, и расстояние 
    до ближайшего киоска с мороженым.
"""
    points = ((a + b) // 2, (a + b) // 2 + (a + b) % 2)
    distances = [0] * 2

    for i in range(2):
        distances[i] = min((points[i] % d), d - (points[i] % d))

    shortest_distance = min(distances)
    best_point = points[distances.index(shortest_distance)]

    return best_point, shortest_distance


def revers_numbers(n: int, data: list) -> int:
    """
    Обратное число
    В этой задаче нужно ответить на 1≤t≤105 запросов. Каждый запрос 
    состоит из двух целых чисел 2≤p≤109 и 0<a<p, число p является простым.
    На каждый запрос нужно вывести в отдельной строке целое число 0<b<p такое, 
    что (a⋅b−1) ⋮ p.

    Входные данные:
    В первой строке дано целое число t — количество запросов.
    В следующих t строках даны по два числа pi и ai, i=1,…,t.

    Выходные данные:
    Выведите t целых чисел (каждое число в отдельной строке) — ответы на запросы.
    """

    for i in range(n):
        print(pow(data[i][1], data[i][0] - 2, data[i][0]))


def least_common_multiple(a: int, b: int) -> int:
    """
    НОК
    Напишите программу, которая вычисляет наименьшее общее кратное двух чисел.

    Входные данные:
    Входная строка содержит два натуральных числа, разделённые пробелом, 
    — a и b. Гарантируется, что ответ не превосходит 2⋅10^9.

    Выходные данные:
    Программа должна вывести одно натуральное число: НОК заданных чисел.
    """
    composition = a * b
    while b > 0:
        a, b = b, a % b

    return composition // a


def reduce_fraction(a: int, b: int) -> tuple:
    """
    Дана дробь a/b. Требуется её сократить, то есть записать это же число
    в виде c/d, где c — целое число, d — натуральное число 
    и d минимальное возможное.
    """
    primaries = (a, b)
    while b > 0:
        a, b = b, a % b

    return (primaries[0]//a, primaries[1]//a)


#a, b = map(int, input().split())
#print(*calc_house_point(a, b, d))


print(reduce_fraction(30, 15))