range = 10000
max_jump_lenght = 10

def count_trajectories(range, max_jump_lenght):
    """ Функция считает кол-во траекторий для "кузнечика", 
    который может прыгать на целое число 
    клеток от 1 до n, до клетки m."""

    # Заготавливаем список длинной m.
    traj_matrix = [0] * (range + 1)

    # Заполняем первые значения для дальнейших расчетов. 
    # Кол-во заполняемых элементов равно максимальногй длинне прыжка.
    for i in range(1, max_jump_lenght + 1):
        traj_matrix[i] = 2**(i-1)

    # Считаем кол-во траекторий для каждой точки от максимальной 
    # длинны прыжка (ибо эти значения уже известны) до m включительно.
    # Первым циклом проходим по точкам, вторым ссумируем предыдущие n клеток, 
    # чтобы получить кол-во траекторий для текущей точки.
    for i in range(max_jump_lenght + 1, range + 1):
        for j in range(max_jump_lenght + 1):
            traj_matrix[i] += traj_matrix[i-j]

    return traj_matrix

print(count_trajectories(range, max_jump_lenght))