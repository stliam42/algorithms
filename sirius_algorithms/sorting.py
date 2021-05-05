from random import randint
from datetime import datetime
import random


def timer(func):
    def wrapper(*arags, **kwargs):
        start = datetime.now()
        result = func(*arags, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timer
def selection_sort(list_: list, k: int) -> list:
    for i in range(k):
        imax = i
        for j in range(i+1, len(list_)):
            if list_[j] > list_[imax]:
                imax = j
        list_[imax], list_[i] =  list_[i], list_[imax]

    return list_


#@timer
def bubble_sort(a: list) -> list:
    n = len(a)
    a = a[:]
    unordered = True
    count = 0
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                unordered = True
                count += 1
        n -= 1

    return a, count


@timer
def find_sequence(n: int, k: int) -> list:
    a = list(range(1, n + 1))
    count = 0
    left_index = 0
    while k != 0:
        i = n - 1
        while i != left_index and k != 0:
            i -= 1
            k -= 1
            count += 1
        
        a.insert(i, a.pop())
        left_index += 1
    
    return a, count


def insertion_sort(a: list) -> list:
    for i in range(1, len(a)):
        b = a[:]
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
        if a != b:
            print(*a)


def sort_olympic_results(a: list):
    """
    Результаты олимпиады.
    Во время проведения олимпиады каждый из участников получил свой 
    идентификационный номер — натуральное число. Необходимо отсортировать
    список участников олимпиады по количеству набранных ими баллов от 
    больших баллов к меньшим, а при равенстве баллов — по возрастанию
    идентификационных номеров. Встроенные алгоритмы сортировки не использовать.

    Входные данные:
    На первой строке дано число N(1≤N≤1000) — количество участников.
    На каждой следующей строке даны идентификационный номер и набранное
    число баллов соответствующего участника. Все числа во входном файле 
    не превышают 10^5.

    Выходные данные:
    Выведите исходный список в порядке убывания баллов. Если у некоторых 
    участников одинаковые баллы, то их между собой нужно выводить в порядке
    возрастания идентификационных номеров.
    """
    for i in range(1, len(a)):
        b = a[:]
        temp = a[i]
        j = i - 1
        while j >= 0 and (a[j][1] < temp[1] or (a[j][0] >= temp[0] and a[j][1] == temp[1])):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

    return a


def count_sort(a: str) -> list:
    b = [0] * 10
    for symbol in a:
        if symbol.isdigit():
            b[int(symbol)] += 1
    
    answer = ''

    for i in range(9, -1, -1):
        answer += str(i) * b[i]

    return answer


def keyboard_is_broken(durability: list, pressing: list) -> list:
    keys = len(durability)
    press_for_key = [0] * keys
    broken_keys = [0] * keys

    for press in pressing:
        press_for_key[press - 1] += 1

    for key in range(keys):
        broken_keys[key] = 'yes' if press_for_key[key] > durability[key] else 'no'
            

    return broken_keys


def sort_socks(table_lenght: int, socks: list, points: list) -> list:
    """
    Носки.
    Имеется стол длины L. На столе разложено N носков так, что никакой 
    носок не вылезает за границы стола. Далее имеется умный мальчик Вася,
    который хочет (сугубо в корыстных целях) замерить толщину покрытия 
    стола носками в M точках. Конец носка также накрывает точку стола, 
    в которой он находится.

    Входные данные:
    В первой строке заданы L,N,M(1≤L≤10000,1≤N≤10000,1≤M≤100000).

    Далее идут N пар чисел l≤r от 1 до L — левые и правые концы носков,
    каждая в отдельной строке.

    Затем идут M чисел от 1 до L — интересующие Васю точки, каждое в 
    отдельной строке. Все числа целые.

    Выходные данные:
    Выведите M чисел — толщину носкового покрытия в каждой точке.
    """
    covering = [0] * table_lenght
    answer = []

    for sock in socks:
        for i in range(sock[0], sock[1] + 1):
            covering[i - 1] += 1

    for point in points:
        answer.append(covering[point - 1])
    
    return answer


def merge_sequences(point: int):
    """
    Объединение последовательностей.

    Даны две бесконечных возрастающих последовательности чисел A и B.
    i-ый член последовательности A равен i^2. i-ый член последовательности 
    B равен i^3.

    Требуется найти Cx, где C — возрастающая последовательность, 
    полученная при объединении последовательностей A и B. Если существует
    некоторое число, которое встречается и в последовательности A, и в 
    последовательности B, то в последовательность C это число попадает 
    в единственном экземпляре.

    Входные данные:
    В единственной строке входных данных дано натуральное число x(1≤x≤10^6).

    Выходные данные:
    Выведите Cx.
    """
    def power_generator(x):
        n = 1
        while n <= 10 ** 6:
            yield n ** x
            n += 1

    result = [1]
    square = power_generator(2)
    triple = power_generator(3)
    a = next(square)
    b = next(triple)
    while point != len(result):
        if result[-1] == a:
            a = next(square)
            continue
        if result[-1] == b:
            b = next(triple)
            continue
        if a >= b:
            result.append(b)
            b = next(triple)
        else:
            result.append(a)
            a = next(square)

    return result[-1]


def merge_sort(a: list) -> list:

    def merge(a: list, b: list) -> list:
        i = j = 0
        result = []
        while i != len(a) and j != len(b):
            if a[i] >= b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1

        result.extend(a[i:])
        result.extend(b[j:])
        return result

    if len(a) <= 1:
        return a

    k = len(a) // 2
    return merge(merge_sort(a[:k]), merge_sort(a[k:]))

    
def is_lists_the_same(a, b) -> str:
    return 'YES' if set(a) == set(b) else 'NO'


def sum_digits(n: int) -> int:
    x = str(n)
    sum = 0
    for digit in x:
        sum += int(digit)
    return sum


# DO ME
a = ['2','20','004','66']
a.sort(reverse=True)
print(a)

#n = int(input())
#a = list(map(int, input().split()))


#print(sorted(a, reverse=True, key=sum_digits))

#a = list(map(int, input().split()))
#a = [randint(0, 10 ** 1) for i in range(n)]
