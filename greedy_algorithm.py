"""Жадные алгоритмы. Задача о подборе радиостанций для вещания в наибольшем кол-ве штатов."""

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {
            'kone': {'id', 'nv', 'ut'},
            'ktwo': {'wa', 'id', 'mt'},
            'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'},
            'kfive': {'ca', 'az'},
            }


def get_best_station_set(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = {}

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                final_stations.add(station)
                states_needed -= covered

    return final_stations

final_stations = get_best_station_set(states_needed, stations)

print(final_stations)