
def late(now: str, classes: str, bus: list) -> str:
    time_to_get_out = 0
    time_to_busstop = 5
    time_to_school = 15
    
    def get_time(time: str) -> int:
        time = tuple(map(int, time.split(":")))
        return time[0] * 60 + time[1]

    now = get_time(now)
    classes = get_time(classes)
    bus = [time for time in bus if time >= time_to_busstop]

    for way_time in bus:
        if classes - (now + way_time) >= time_to_school:
            time_to_get_out = way_time - time_to_busstop

    return ('Выйти через {} минут'.format(time_to_get_out)
           if time_to_get_out else 'Опоздание')


a = '12:00'
b = "12:40"
c = [0,1,4,6,10,15,25]

print(late(a,b,c))

a = '9:20'
b = "9:35"
c = [0,1,4,6,10,15,25]

print(late(a,b,c))
print(late('13:50', '14:30', [7, 17, 35, 48]))
print(late('9:00', '10:00', [5, 15, 25]))