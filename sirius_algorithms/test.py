from random import randint

def get_list_of_next_smaller_number_index(items: list, direction: str='right') -> list:
    """
    Функция находит индексы меньших ближайщих элементов.
    items - входной список,
    direction - направление поиска.
    Функция возвращает список.
    """
    
    inf = - 1
    items_with_barriers = [inf] + items + [inf]
    answer = [0] * (len(items) + 2)
    
    if direction == 'right':
        st = [0]
        for i in range(1, len(items) + 2):
            while items_with_barriers[i] < items_with_barriers[st[-1]]:
                answer[st.pop()] = i - 1
            else:
                st.append(i)

    elif direction == 'left':
        st = [len(answer) - 1]
        for i in range(len(items), -1, -1):
            while items_with_barriers[i] < items_with_barriers[st[-1]]:
                answer[st.pop()] = (i - 1) if (i - 1) >= 0 else len(items)
            else:
                st.append(i)

    return answer[1:-1]


#start = datetime.datetime.now()

n = int(input())

a = [randint(1, 1000) for i in range(n)]

print(get_list_of_next_smaller_number_index(a, 'left'))