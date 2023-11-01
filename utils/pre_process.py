def pre_process(lst):
    res = []
    tmp = []
    cnt = 0
    for it in lst:
        tmp = []
        for i in it:
            i = str(i)
            tmp.append(i[7:])
        res.append(tmp)
        cnt += 1
    return res