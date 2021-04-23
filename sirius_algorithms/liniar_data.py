class Stack:

    def __init__(self):
        self.__st = []

    def push(self, x):
        self.__st.append(x)

    def pop(self):
        return self.__st.pop() if self.size > 0 else 'error'

    @property
    def back(self):
        return self.__st[-1]  if self.size > 0 else 'error'

    @property
    def size(self):
        return len(self.__st)

    def clear(self):
        self.__st.clear()

    def __repr__(self):
        return str(self.__st)

    def __str__(self):
        return str(self.__st)


def analyze_brackets(brackets: str) -> str:
    """
    Правильная скобочная последовательность.

    Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных
    скобок. Программа должна определить, является ли данная скобочная 
    последовательность правильной.

    Пустая последовательность является правильной. Если A правильная, 
    то последовательности (A), [A], {A} правильные. Если A и B правильные 
    последовательности, то последовательность AB правильная.

    Входные данные:
    В единственной строке записана скобочная последовательность, 
    содержащая не более 100000 скобок.

    Выходные данные:
    Если данная скобочная последовательность правильная, 
    то программа должна вывести строку yes, иначе — строку no.
    """
    right = False
    st = Stack()
    bracket_dict = {
                    ')': '(',
                    ']': '[',
                    '}': '{',
                    }

    for i in range(len(brackets)):
        bracket = brackets[i]

        if bracket in ('(', '[', '{'):
            st.push(bracket)
        else:
            if st.back == bracket_dict[bracket]:
                st.pop()
            else:
                st.push(bracket)
                break
       

    if st.size == 0:
        right = True

    return 'yes' if right else 'no'


brackets = input()

print(analyze_brackets(brackets))

