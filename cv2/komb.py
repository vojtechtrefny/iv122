import copy

def permutations(lst):
    if len(lst) == 1:
        return [lst]

    perm_list = []
    for i in lst:
        lst2 = copy.deepcopy(lst)
        lst2.remove(i)

        for r in permutations(lst2):
            r.insert(0, i)
            perm_list.append(r)

    return perm_list

# ---------------------------------------------------------------------------- #

def combinations(lst, lenght, repetition=False):
    if lenght == 1:
        return [[i] for i in lst]

    comb_list = []
    for i in lst:
        lst2 = copy.deepcopy(lst)
        if not repetition:
            lst2.remove(i)

        for c in combinations(lst2, lenght - 1, repetition):
            c.insert(0, i)
            c.sort()
            if c not in comb_list:
                comb_list.append(c)

    return comb_list

# ---------------------------------------------------------------------------- #

def variations(lst, lenght, repetition=False):
    if lenght == 1:
        return [[i] for i in lst]

    var_list = []
    for i in lst:
        lst2 = copy.deepcopy(lst)
        if not repetition:
            lst2.remove(i)

        for v in variations(lst2, lenght - 1, repetition):
            v.insert(0, i)
            var_list.append(v)

    return var_list
