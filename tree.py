import os

origin = [
        ['id3'], ['id2', 'id3'], ['id1', 'id2', 'id3'],
        ['id4', 'id3'], ['id5', 'id4', 'id3']
        ]


def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a == len_b:
        for ix in xrange(len_a):
            if a[ix] != b[ix]:
                return False
    elif len_a > len_b:
        master = a
        slave = b
    else:
        master = b
        slave = a

    # judge
    try:
        index = master.index(slave[0])
    except Exception, e:
        return False

    master_ix = index
    slave_ix = 0
    while slave_ix < len(slave):
        if master[master_ix] != slave[slave_ix]:
            return False
        master_ix += 1
        slave_ix += 1

    return True


if __name__ == '__main__':
    final = []
    while len(origin) > 0:
        ori_item = origin.pop()
        merged = 0
        for fin_item in final:
            if merge(ori_item, fin_item):
                merged = 1
                break

        if merged == 0:
            final.append(ori_item)

    for i in final:
        print i
