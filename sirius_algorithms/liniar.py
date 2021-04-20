def max_fraction(n: int, a: tuple) -> tuple:
    """
    Отношение.

    Дан массив a1,a2,…an. Необходимо выбрать в нём два элемента ai и aj 
    такие, что i<j, и отношение aj/ai максимально и больше 1.

    Входные данные:
    В первой строке задано целое число 2 ≤n≤ 100 000 — количество
    элементов в массиве.
    Во второй строке заданы n целых положительных чисел 
    ai(1 ≤i≤n, 1 ≤ai≤ 5000).

    Выходные данные:
    Выведите два числа — индексы элементов i и j. Если ответов
    несколько, то выведите любой из них.
    Если ответа нет, то выведите два нуля, разделённых пробелом.
    """
    ibest = 0
    jbest = 1
    imin = 0

    for j in range(2, n):
        if a[j-1] < a[imin]:
            imin = j - 1
        if a[j] / a[imin] > a[jbest] / a[ibest]:
            ibest = imin
            jbest = j

    return (ibest+1, jbest+1) if a[jbest] / a[ibest] > 1.0 else (0, 0)


def rob_the_bank(n: int, k: int, a: tuple) -> tuple:
    """
    Клиппи и Мерлин грабят банк.

    Клиппи и Мерлин решили грабить банк, который представляет собой N 
    расположенных в ряд банковских ячеек, пронумерованных последовательно 
    числами от 1 до N.

    С помощью своего друга Ровера, который работал в банке сторожевым 
    псом, они добыли ключи от всех ячеек, а также узнали, как много 
    ценностей хранится в каждой ячейке.

    Чтобы не вызывать лишних подозрений, Клиппи и Мерлин решили ограбить
    всего две ячейки — по одной на каждого. Также, чтобы охрана банка 
    не почуяла неладного, они решили работать далеко друг от друга — 
    между ними должно быть не меньше K банковских ячеек.

    Входные данные:
    В первой строке вводятся два числа — N ( 2 ≤N≤ 105) и K (0 ≤K<N− 1) 
    соответственно. В второй строке вводятся N чисел ai(0 ≤ai≤ 109) — 
    стоимости хранимых ценностей в ячейках от 1 до N соответственно.

    Выходные данные:
    Выведите два числа в возрастающем порядке — номера ячеек, которые
    нужно ограбить, чтобы суммарно украсть как можно более дорогие ценности,
    не вызвав при этом лишних подозрений. Если вариантов несколько, выберите 
    тот, в котором меньший номер вскрываемой ячейки был бы как можно ближе 
    к единице, чтобы в экстренном случае покинуть банк как можно скорее. 
    Если и таких вариантов несколько, выберите тот, в котором и больший номер
    вскрываемой ячейки был бы как можно меньше.
"""
    ibest = 0
    jbest = k + 1
    imax = 0
    for j in range(k + 2, n):
        if a[j-(k+1)] > a[imax]:
            imax = j - (k + 1)
        if a[j] + a[imax] > a[jbest] + a[ibest]:
            ibest = imax
            jbest = j

    return (ibest, jbest)


def trade_the_stocks(number_of_days: int, 
                     init_money: int, 
                     price_of_buying: tuple, 
                     price_of_selling: tuple):
    """
    Торговля акциями.

    В настоящее время на бирже при торговле акциями активно применяются 
    компьютерные системы, которые упрощают и автоматизируют процесс покупки
    и продажи акций. Некоторые из них даже позволяют вести торговлю вообще 
    без участия человека.

    Разумеется, основным критерием, по которому такие системы оцениваются, 
    является прибыль, которую приносит торговля с их применением. Для того 
    чтобы её повысить, при построении этих систем применяются различные 
    математические методы и модели.

    Основной трудностью при создании таких систем является то, что они должны
    некоторым образом учитывать изменение стоимости акций в будущем, а также
    его прогнозировать. Ваша задача несколько проще — курсы продажи и покупки
    акций за весь период из N дней уже известны, необходимо лишь разработать
    оптимальную стратегию продаж и покупок. При этом для простоты будем считать,
    что за эти N дней купить акции можно не более одного раза и продать акции 
    можно также не более одного раза.

    Кроме этого, будем считать, что продажа и покупка будет осуществляться
    только с акциями одного типа. На начало этого периода вы располагаете 
    суммой в X рублей. Для каждого из дней известна цена ai 
    (от ask — цена предложения), по которой можно купить одну акцию, и цена bi,
    по которой можно одну акцию продать. При этом в соответствии с действующими
    правилами торгов на бирже разрешается продавать и покупать только целое число
    акций (например, если у вас есть 5 рублей, а акция стоит 2 рубля, то вы 
    можете купить не более двух акций). Требуется написать программу, которая
    по имеющимся данным о стоимости акций в каждый из дней, найдёт оптимальную
    стратегию покупки и продажи акций.

    Входные данные:
    Первая строка содержит целые числа N и X (1 ≤ N ≤ 100 000,1 ≤ X ≤ 10^6). 
    Вторая строка содержит N целых чисел a1, ..., aN. Третья строка 
    содержит N целых чисел b1, ..., bN(1 ≤ bi ≤ ai ≤ 1 000).

    Выходные данные:
    В первой строке выведите максимальную сумму, которой вы можете обладать 
    по окончании рассматриваемого периода. Во второй строке выведите 
    два числа — номер дня d1, в который следует купить акции, и номер дня d2,
    в который эти акции следует продать (должно выполняться неравенство d2 > d1).
    При этом подразумевается, что покупается столько акций, сколько их можно 
    купить на X рублей, а потом они все продаются. Если в найденной вами 
    стратегии продавать и покупать акции не требуется, то выведите во второй 
    строке "−1 −1". Если существует несколько вариантов оптимальной стратегии,
    то выведите любой из них.
"""
    if n == 1:
        return (init_money, (-1, -1))
    ibest = 0
    jbest = 1
    i_min_price_of_buying = 0

    for j in range(2, number_of_days):
        if price_of_buying[j-1] < price_of_buying[i_min_price_of_buying]:
            i_min_price_of_buying = j - 1
        if ((init_money // price_of_buying[i_min_price_of_buying]) * price_of_selling[j] > 
            (init_money // price_of_buying[ibest]) * price_of_selling[jbest]):
            jbest = j
            ibest = i_min_price_of_buying

    potential_profit = (init_money // price_of_buying[ibest] * 
                        price_of_selling[jbest])

    change = init_money % price_of_buying[ibest]
    total_money = potential_profit + change

    if total_money > init_money:
        return  (total_money, (ibest+1, jbest+1))
    else:
        return (init_money, (-1, -1))


def amount_of_consecutive(num_of_items: int, 
                          gap: int, 
                          required_sum: int, 
                          a: tuple) -> int:
    """
    Сумма подряд идущих.

    Дан массив целых чисел a[1],a[2],...,a[n] и натуральные числа k и m. 
    Укажите минимальное значение i, для которого a[i]+a[i+1]+...+a[i+k]=m 
    (то есть сумма k+1 подряд идущих элементов массива равна m). 
    Если такого значения нет, то выведите 0.

    Входные данные:
    На вход программе сначала подаются значения n, k и m 
    (m≤10^9, 0<k<n≤10^5, n — количество элементов в массиве). 
    В следующей строке входных данных расположены сами элементы
    массива — целые числа, по модулю не превосходящие 100.

    Выходные данные:
    Выведите ответ на задачу.
    """

    p = [0 for i in range(num_of_items + 1)]

    for i in range(1, num_of_items +1):
        p[i] = p[i-1] + a[i-1]
        if i >= k + 1:
            print(p[i] - p[i-k-1])
            if p[i] - p[i-k-1] == required_sum:
                return i - k
    return 0


def route_without_climbs(number_of_heels: int,
                         number_of_requests: int,
                         heels_heights: tuple,
                         routs: tuple):
    """
    Новый маршрут для трекинга.

    Сейчас самое время планировать новые трекинговые маршруты.

    Опишем холмистую местность массивом из n чисел. Высота i-го холма равна hi.
    Маршрут должен идти по k подряд идущим холмам (учитывая тот холм, 
    с которого маршрут будет начинаться). Немолодым туристам не очень нравится,
    когда приходится много раз подниматься в гору — переходить с более низкого 
    холма на более высокий.

    Помогите туристам определиться с выбором маршрута — напишите программу, 
    которая отвечает на запросы о количестве переходов с более низкого холма 
    на более высокий на данном маршруте.

    Входные данные:
    В первой строке даны натуральные числа n, m (2≤n,m≤2⋅10^5) — общее количество
    холмов и количество запросов соответственно.
    Во второй строке даны n целых чисел hi(1≤hi≤10^5) — высоты холмов.
    В следующих m строках записаны пары чисел lj и rj (1 ≤ li ≤ rj ≤ n) — запросы 
    на количество переходов с более низкого холма на более высокий на маршруте с 
    началом в холме lj и завершением в rj.

    Выходные данные:
    Выведите m чисел — ответы на запросы.
    """

    p = [0] * (n)

    for i in range(1, n):
        p[i] = p[i-1] + (1 if heels_heights[i] > heels_heights[i-1] else 0)

    for i in range(number_of_requests):
        print(p[routs[i][1] - 1] - p[routs[i][0] - 1])





#print(route_without_climbs(n, m, h, r))

#n, x = (map(int, input().split()))
#a = tuple(map(int, input().split()))
#b = tuple(map(int, input().split()))
