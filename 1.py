
def sum(x,y):
    result = {}
    result['s'] = (x['s'] * y['m']) + (x['m'] * y['s'])
    result['m'] = x['m'] * y['m']
    return result

def mul(x,y):
    result= {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result

def show(x):
    print(x['s'], '/', x['m'])

a = {'s':2, 'm':3}
b = {'s':5, 'm':4}

c = mul(a,b)
d = sum(a,c)
show(d)


