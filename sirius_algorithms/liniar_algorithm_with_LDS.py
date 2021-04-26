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


def line_land(n: int, a: tuple):
    inf = 1
    a = [-inf] + list(a) + [-inf]
    answer = [0] * (n + 2)
    st = Stack(0)
    for i in range(1, n + 2):
        while a[i] < a[st.back]:
            answer[st.pop()] = (i - 1) if i != (n + 1) else -1
        else:
            st.push(i)

    return answer[1:-1]




n = 10
a = (1, 2, 3, 2, 1, 4, 2, 5, 3, 1)

print(*line_land(n, a))