""" Алгорит поиска в ширину. Находит кратчайшее расстояние между графами.
Конкретная задача - найти знакомого, с которым у тебя 3 общих друга."""

class BFS:
    def __init__(self):
        self.graph = {}
        self.graph['me'] = ['alice', 'bob', 'claire', 'rob']
        self.graph['bob'] = ['anuj', 'peggy', 'alex']
        self.graph['alice'] = ['peggy', 'sonia', 'anuj']
        self.graph['claire'] = ['thom', 'jonny']
        self.graph['anuj'] = ['alex', 'sonia', 'rob']
        self.graph['peggy'] = ['me', 'thom']
        self.graph['thom'] = ['alice', 'peggy', 'rob', 'claire']
        self.graph['jonny'] = ['me', 'anuj', 'sonia', 'claire']



        self.search_queue = []
        self.search_queue += self.graph['me']
        self.searched = ['me']

    def breadth_first_search(self):
        while self.search_queue:
            person = self.search_queue.pop(0)
            if person in self.searched:
                continue
            if self.person_has_3_mutual_friend(person):
                print(person.capitalize() + ' and you have 3 mutual friends!')
                return True
            else:
                self.searched.append(person)
                try:
                    self.search_queue += self.graph[person]
                except:
                    pass
        return False

    def person_has_3_mutual_friend(self, person):
        try:
            mutual_friends = set(self.graph['me']) & set(self.graph[person])
        except:
            return False
        return True if len(mutual_friends) >= 3 else False


bfs = BFS()

bfs.breadth_first_search()