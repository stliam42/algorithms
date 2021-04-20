best = {'start': (1,2,3),
        'len': (2,5,4),
        }
maxlen = max(best['len'])

y = list(filter(lambda x: True if best['len'][best['start'].index(x)] == maxlen else False, best['start']))

print(y)