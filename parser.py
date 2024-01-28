import math


def parse(l):
    if 'ID' not in txt:
        raise Exception()
    prices = txt.split()[1] == 'prices'
    txt = '\n'.join(txt.split('\n')[1:])
    tmp = []
    wasalpha = False
    for i in l:
        if wasalpha:
            if i[0].isalpha() or i[0] == '-':
                tmp[-1] += ' ' + i
            else:
                tmp.append(i)
        else:
            tmp.append(i)
        wasalpha = i[0].isalpha() or i[0] == '-'
    try:
        if not prices:
            d = {x[1]: (float(x[2]), math.ceil(float(x[3])/float(x[2]))) for x in tmp}
        else:
            d = {x[1]: (float(x[2]), math.ceil(float(x[3]))) for x in tmp}
    except Exception as e:
        raise
    return d


