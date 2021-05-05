#n, x = map(int, input().split())
#a = tuple(map(int, input().split()))


def delete_repeats(a: str) -> str:
    a_list = list(a)
    a_set = set()
    answer = ''
    for i in range(len(a_list)):
        if a_list[i] not in a_set:
            a_set.add(a_list[i])
            answer += a_list[i]

    return str(answer)


def get_schedule(t: set, r: set, t1: set, r1: set) -> tuple:
    if (t1 - t) != t1 or not (r1 - r):
        return -1
    t2 = t | t1
    r.add(sorted(r1 - r)[0])
    return (len(t2), sorted(t2), len(r), sorted(r))



bank = {}
states = {}
candidates = {}
requests = ['Florida Gore', 'Florida Bush', 'Florida Bush', 'Pennsylvania  Gore', 'Florida Gore', 'Pennsylvania  Bush', 'Florida Bush', 'Pennsylvania  Gore']
voices = {}

#n = int(input())

#for state in range(n):
#    state, electors = input().split()
#    states[state] = int(electors)

#m = int(input())

for request in requests:
    state, candidate = request.split() #input().split()

    if state not in candidates:
        candidates[state] = {}

    candidates[state][candidate] = candidates[state].get(candidate, 0) + 1


for state in candidates:
    candidates[state] = {k: v for k, v in sorted(candidates[state].items(), key=lambda item: item[1], reverse=True)}

print(states, candidates)

