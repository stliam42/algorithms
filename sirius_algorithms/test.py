from random import randint

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

def get_min_list(items: list, inf: int) -> list:
    items_with_barriers = [inf] + items + [inf]
    answer = [0] * (len(items) + 2)
    st = Stack(0)

    for i in range(1, len(items) + 2):
        while items_with_barriers[i] < items_with_barriers[st.back]:
            answer[st.pop()] = i - 1
        else:
            st.push(i)

    return answer[1:-1]

def min_on_the_segment(number_of_elements: int,
                      window: int, 
                      items: list) -> list:
    min_list = get_min_list(items, -1)
    results = [0] * (number_of_elements - window + 1)
    imin = 0

    for i in range(0, number_of_elements - window + 1):
        if imin < i:
            imin = i

        while min_list[imin] < i +  window:
              imin = min_list[imin]
        results[i] = imin

    return [items[i] for i in results]
    
number_of_elements, window = map(int, input().split())
a = list(map(int, input().split()))

print(get_min_list(a, -1))
print(*min_on_the_segment(number_of_elements,window,a), sep='\n')

#for n in range(1, 150000):
#    k = randint(1, (n//2)+1)
#    a = [randint(0, 100) for i in range(n)]
#    #print(n,k,a)