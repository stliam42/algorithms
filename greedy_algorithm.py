"""
Жадные алгоритмы. 
Задача сводится к оптимальному решению, а не к лучшему.
Общее решение состоит в том, чтобы взять самый ценный вариант. 
После этого берется следущий по ценности вариант.

Пример с заполнением рюкзака: берем самый ценный доступный предмет и кладём его в рюкзак. 
Повторяем, пока в рюкзаке не закончится место.
Возможно, что решение не будет лучшим, но будет стремиться к локальной оптимизации.

Приближенные алгоритмы применяются для NP-полных задач, для которых 
не существует известных быстрых решений.
"""


# Задача о подборе радиостанций для вещания в наибольшем кол-ве штатов.
# В данной задаче мы выбираем станцию, которая покрывает наибольшее кол-во штатов и заносим её в список используемых. 
# Поступаем так, пока не покроем все необходимые штаты.

# Штаты, где необходимо вести радиовещание.
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

# Доступные радиостанции со штатами, в которых они вещают.
stations = {
            'kone': {'id', 'nv', 'ut'},
            'ktwo': {'wa', 'id', 'mt'},
            'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'},
            'kfive': {'ca', 'az'},
            }


def get_best_station_set(states_needed, stations):
    """ Функция, которая находит оптимальный набор радиостанций, 
    которые будут покрывать все необходимые штаты."""

    # Создаём пустое множество, в которое войдут нужные станции
    final_stations = set()

    # Пока есть непокрытые штаты:
    while states_needed:
        best_station = None
        states_covered = {}

        # Для каждой станции получаем зону её покрытия: 
        # пересечение необходимых штатов и штатов радиостанции.
        # В ходе цикла находится станция, покрывающая наибольшее 
        # кол-во еще не покрытых штатов.
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station

            # Если кол-во штатов, которые покрывает текущая радиостанция больше, 
            # чем кол-во штатов, которые покрывает предыдущая, то занести покрываемые 
            # ей штаты в список покрываемых и назначить её "лучшей" станцией.

            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station

        # После нахождения "лучшей" станции она заносится в список требуемых станций,
        # а покрываемые ей штаты будут вычеркнуты из списка непокрытых.
        # Когда будут покрыты все штаты - функция вернет список требуемых станций
        final_stations.add(best_station)
        states_needed -= states_covered

    return final_stations

print(get_best_station_set(states_needed, stations))