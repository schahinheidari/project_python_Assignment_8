def sum(x,y):
    result={}
    result['s'] = x['s']+ y['s']
    result['m'] = x['m']+ y['m']
    result['h'] = x['m']+ y['m']

    if (result['s'] >= 60):
        result['s'] -= 60
        result['m'] += 1

    if (result['m'] >= 60):
        result['m'] -= 60
        result['h'] += 1
    return result

def sub(x,y):
    result={}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']
    result['h'] = x['m'] - y['m']

    if (result['s'] >= 60):
        result['s'] -= 60
        result['m'] += 1

    if (result['m'] >= 60):
        result['m'] -= 60
        result['h'] += 1
    return result

def show(x):
    print(x['h'],":",x['m'],":",x['s'])




t1 = {'h': 5, 'm':30, 's':45}
t2 = {'h': 3, 'm':17, 's':40}

t3 = sum(t1, t2)
show(t3)
print(t3)
