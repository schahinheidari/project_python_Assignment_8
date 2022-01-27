res= {}

def sum(a,b):
    res["x"] = a['x'] + b['x']
    res["y"] = a['y'] + b['y']
    return res

def sub(a,b):
    res["x"] = a['x'] - b['x']
    res["y"] = a['y'] - b['y']
    return res

def mul(a,b):
    res["x"] = (a['x'] * b['x']) - (a['y'] * b['y']) 
    res["y"] = (a['x'] * b['y']) + (a['y'] * b['x'])
    return res

t1 = {'x': 3, 'y':2}
t2 = {'x': 1, 'y':7}

t3 = mul(t1, t2)

print(t3)