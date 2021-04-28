from random import randint

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
    START = 0
    END = 1

    for i in range(1, n):
        p[i] = p[i-1] + (1 if heels_heights[i] > heels_heights[i-1] else 0)

    for i in range(number_of_requests):
        print(p[routs[i][END] - 1] - p[routs[i][START] - 1])


def divided_by_three(number_of_items: int, items: tuple) -> tuple:
    """
    Сумма, делящаяся на три.

    Необходимо найти самый большой непрерывный фрагмент в массиве a1,a2...aN,
    сумма элементов которого делится на 3.

    Входные данные:
    В первой строке содержится число N≤100000. Во второй строке даны N чисел,
    по модулю не превосходящих 109, — элементы массива.

    Выходные данные:
    Выведите два числа — индексы начала и конца фрагмента. Если таких фрагментов
    несколько, то выведите фрагмент с минимальным индексом начала.

    Если ответа не существует, то выведите единственное число −1.
    """
    p = [0] * (number_of_items + 1)

    # Заготавливаем словарь с лучшими начальными и конечными индексами,
    # флагами регистрации значений и длинами фрагментов.
    # Индексы списков совпадают с остатками от деления: 
    # индекс 0 соответствует группе с остатком от деления по 
    # модулю 3 равным 0 и т.д.
    best = {'start': [0] * 3,
            'flags': [False] * 3,
            'end' : [-1] * 3,
            'lenght': [-1] * 3,
            'index': -1,
            'i': 0,
            'j': 0,
            }

    # Вычисляем остаток по модулю 3 от суммы элементов от 0 до i.
    for i in range(1, number_of_items + 1):
        p[i] = (p[i-1] + items[i-1]) % 3

        # Попутно регистрируем индексы первых появлений сумм, дающих остаток 1 и 2. 
        # Данные индексы будут точкой отсчёта для нахождения фрагмента максимальной длинны.
        # Т.к. разность сумм, остатки от деления по модулю 3 которых равны, дают число,
        # делящееся на 3, то самым длинным фрагментом будет разность сумм с одинаковым 
        # остатком и максимальным расстоянием между началом и концом.
        # Остаток 0 даёт 0-ой элемент, поэтому для него индекс не ищем.
        if not all(best['flags']):
            for j in range(1, 3):
                if p[i] == j and not best['flags'][j]:
                    best['start'][j] = i
                    best['flags'][j] = True

    # Сбрасываем флаги, чтобы регистрировать последние суммы, 
    # которые дают остаток 0, 1, 2.
    best['flags'] = [False] * 3

    # Находим индексы конечных сумм, дающих 0, 1, 2.
    for i in range(number_of_items, 0, -1):
        if all(best['flags']):
            break
        for j in range(3):
                if p[i] == j and not best['flags'][j]:
                    best['end'][j] = i
                    best['flags'][j] = True

    # Находим длины фрагментов на 0, 1, 2.
    for i in range(3):
        best['lenght'][i] = best['end'][i] - best['start'][i]

    # Находим максимальную длинну.
    maxlen = max(best['lenght'])

    # Если фрагментов нет, или на вход было подано 0 элеметнов - 
    # выводим сообщение об отсутствии ответа.
    if maxlen == 0 or number_of_items == 0:
        return -1

    # Выбираем лучшую левую границу. Так как в задаче необходимо 
    # найти фрагмент с минимальным индексом начала, то мы находим, 
    # какой фрагмент максимальной длинны раньше начинается. 
    # Фильтруем начальные значения на основании длинны фрагмента и 
    # выбираем минимальный из них.
    best_start = min(filter(lambda x: True if 
                           best['lenght'][best['start'].index(x)] == maxlen 
                           else False, 
                           best['start']))

    # Берем индекс (0, 1, 2) для лучшего фрагмента. 
    # Выше было найдено лучшее начало, его индекс и берем.
    best['index'] = best['start'].index(best_start)

    # Берем i и j границы по индексу.
    best['i'] = best['start'][best['index']] + 1
    best['j'] = best['end'][best['index']]

    return p, best, best['i'], best['j']


def max_fragment_sum(number_of_items: int, items: tuple) -> tuple:
    """
    Сумма чисел в массиве.

    В одномерном массиве, заполненном произвольными целыми числами, 
    за один проход найдите непрерывный кусок, сумма чисел в котором максимальна.

    Примечание. Фактически требуется найти такие i и j (i≤j), что сумма всех
    элементов массива от ai до aj включительно будет максимальна.

    Входные данные:
    На вход программе сначала подаётся натуральное n≤100000 — количество элементов
    в массиве. Далее, по одному в строке расположены сами элементы массива — 
    целые числа, по модулю не превосходящие 30000.

    Выходные данные:
    Выдайте пару искомых значений индексов. Если таких пар несколько, 
    то j должно быть минимально возможным, а при равных j значение i должно 
    быть максимально возможным.
    """
    p = [0] * (n + 1)

    for i in range(1, n + 1):
        p[i] = p[i-1] + items[i-1]

    ibest = 0
    jbest = 0
    imin = 0

    for j in range(1, n + 1):
        if p[j] <= p[imin]:
            imin = j
        if p[j] - p[imin] > p[jbest] - p[ibest]:
            jbest = j
            ibest = imin

    return (0, 0) if ibest == 0 and jbest == 0 else (ibest+1, jbest) 


def city_che(number_of_items: int, 
             visible_range: int, 
             items: tuple) -> int:
    """
    Город Че.

    В центре города Че есть пешеходная улица — одно из самых популярных 
    мест для прогулок жителей города. По этой улице очень приятно гулять, 
    ведь вдоль улицы расположено n забавных памятников.

    Девочке Маше из города Че нравятся два мальчика из её школы, и она 
    никак не может сделать выбор между ними. Чтобы принять окончательное 
    решение, она решила назначить обоим мальчикам свидание в одно и то же 
    время. Маша хочет выбрать два памятника на пешеходной улице, около 
    которых мальчики будут её ждать. При этом она хочет выбрать такие памятники,
    чтобы мальчики не увидели друг друга. Маша знает, что из-за тумана мальчики 
    увидят друг друга только в том случае, если они будут на расстоянии 
    не более r метров.

    Маша заинтересовалась, а сколько способов есть выбрать два различных 
    памятника для организации свиданий.

    Формат входных данных:
    В первой строке находятся два целых числа n и r (2≤n≤300 000, 1≤r≤109) — 
    количество памятников и максимальное расстояние, на котором мальчики 
    могут увидеть друг друга.
    Во второй строке заданы n положительных чисел d1, d2, ..., dn, где di — 
    расстояние от i-го памятника до начала улицы. Все памятники находятся 
    на разном расстоянии от начала улицы. Памятники приведены в порядке 
    возрастания расстояния от начала улицы (1≤d1<d2<...<dn≤109).

    Формат выходных данных:
    Выведите одно число — число способов выбрать два памятника для 
    организации свиданий.
"""
    i = 0
    j = 1
    count = 0
    sum_range = items[j] - items[i]
    go = True

    while go:
        if sum_range > visible_range:
            count += number_of_items - j
            sum_range -= items[i+1] - items[i]
            i += 1

        elif j == (n - 1):
            go = False

        else:
            j += 1
            sum_range += items[j] - items[j-1]
    
    return count


def shirts_and_pants(number_of_shirts: int,
                     shirts_colors: tuple,
                     number_of_pants: int,
                     pants_colors: tuple) -> tuple:
    """
    Стильная одежда.

    Глеб обожает шопинг. Как-то раз он загорелся идеей подобрать себе майку и 
    штаны так, чтобы выглядеть в них максимально стильно. В понимании Глеба
    стильность одежды тем больше, чем меньше разница в цвете элементов его одежды.

    В наличии имеется N (1 ≤ N ≤ 105) маек и M (1 ≤ M ≤ 105) штанов, про 
    каждый элемент известен его цвет (целое число от 1 до 107). Помогите 
    Глебу выбрать одну майку и одни штаны так, чтобы разница в их цвете 
    была как можно меньше.

    Входные данные:
    Сначала вводится информация о майках: в первой строке целое число
    N (1 ≤ N ≤ 105) и во второй N целых чисел от 1 до 107 — цвета имеющихся
    в наличии маек. Гарантируется, что номера цветов идут в возрастающем 
    порядке (в частности, цвета никаких двух маек не совпадают).

    Далее в том же формате идёт описание штанов: их количество M (1 ≤ M ≤ 105)
    и в следующей строке M целых чисел от 1 до 107 в возрастающем 
    порядке — цвета штанов.

    Выходные данные:
    Выведите пару неотрицательных чисел — цвет майки и цвет штанов, 
    которые следует выбрать Глебу. Если вариантов выбора несколько, 
    выведите любой из них.
    """
    if number_of_shirts == number_of_pants == 1:
        return(shirts_colors[0], pants_colors[0])

    i = 0
    j = 0
    ibest = jbest = 0
    diff = abs(shirts_colors[i] - pants_colors[j])
    go = True

    while go:
        if (i == number_of_shirts or 
                j == number_of_pants):
            go = False

        elif shirts_colors[i] == pants_colors[j]:
            ibest = i
            jbest = j
            go = False

        elif abs(shirts_colors[i] - pants_colors[j]) >= diff:
            if shirts_colors[i] > pants_colors[j]:
                j += 1
            else:
                i += 1

        else:
            diff = abs(shirts_colors[i] - pants_colors[j])
            ibest = i
            jbest = j

    return (shirts_colors[ibest], pants_colors[jbest])


def beauty_above_all(number_of_items: int,
                    type_of_numbers: int,
                    items: tuple) -> tuple:
    """
    Красота превыше всего.

    В парке города Питсбурга есть чудесная аллея, состоящая из N 
    посаженных в один ряд деревьев, каждое одного из K сортов. 
    В связи с тем, что Питсбург принимает открытый чемпионат 
    Байтландии по программированию, было решено построить 
    огромную арену для проведения соревнований. Так, согласно 
    этому плану вся аллея подлежала вырубке. Однако министерство
    деревьев и кустов воспротивилось этому решению и потребовало 
    оставить некоторые из деревьев в покое. Согласно новому плану
    строительства все деревья, которые не будут вырублены, должны
    образовывать один непрерывный отрезок, являющийся подотрезком
    исходного. Каждого из K видов деревьев требуется сохранить 
    хотя бы по одному экземпляру. На вас возложена задача найти 
    отрезок наименьшей длины, удовлетворяющий указанным 
    ограничениям.

    Входные данные:
    В первой строкенаходятся два числа N и K (1 ≤N,K≤ 250000). 
    Во второй строке следуют N чисел (разделённых пробелами), 
    i-е число второй строки задаёт вид i-го слева дерева в аллее. 
    Гарантируется, что присутствует хотя бы одно дерево каждого вида.

    Выходные данные:
    Выведите два числа, координаты левого и правого концов отрезка 
    минимальной длины, удовлетворяющего условию. Если оптимальных 
    ответов несколько, выведите самый левый из отрезков.
    """
    counter = [0 for i in range(type_of_numbers)]
    counter[items[0] - 1] += 1
    ibest = 0
    jbest = number_of_items
    i = j = 0
    go = True
    zeros = type_of_numbers - 1


    while go:
        if not zeros and j - i < jbest - ibest:
            ibest, jbest = i, j
            if jbest - ibest + 1 == type_of_numbers:
                go = False

        elif j == number_of_items - 1 and zeros:
            go = False

        else:
            if zeros:
                j += 1
                if counter[items[j] - 1] == 0:
                    zeros -= 1
                counter[items[j] - 1] += 1
            else:
                if counter[items[i] - 1] == 1:
                    zeros += 1
                counter[items[i] - 1] -= 1
                i += 1

    return (ibest+1, jbest+1)
        

n = 10 ** 5
k = 25000
a = (1,2,3,4,5,6)
a = [0] * n

for i in range(1,n):
    a[i] = a[i-1] + 1 if a[i-1] < k else k

print(a)
print(beauty_above_all(n,k,a))


#n, x = map(int, input().split())
#a = tuple(map(int, input().split()))
