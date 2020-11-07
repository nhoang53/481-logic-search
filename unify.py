def unify(e1, e2):
    # e1, e2 is in list of string form
    # e.g. e1 = p(X, Y) -> e1 = ['p', 'X', 'Y']
    if (is_const(e1) and is_const(e2)) \
            or (len(e1) == 0 and len(e2) == 0):
        if e1 == e2:
            return []
        else:
            return -1
    if is_variable(e1):
        if e1[0] in e2:
            return -1
        else:
            return [e2 + e1]
    if is_variable(e2):
        if e2[0] in e1:
            return -1
        else:
            return [e1 + e2]
    if len(e1) == 0 or len(e2) == 0:
        return -1

    he1 = [e1[0]]
    if type(he1[0]) is list:
        he1 = he1[0]
    he2 = [e2[0]]
    if type(he2[0]) is list:
        he2 = he1[0]
    subs1 = unify(he1, he2)
    if subs1 == -1:
        return -1
    te1 = apply(subs1, e1[1:])
    te2 = apply(subs1, e2[1:])
    # print(te1)
    # print(te2)
    subs2 = unify(te1, te2)
    if subs2 == -1:
        return -1
    else:
        return composition(subs1, subs2)


def is_const(e):
    if len(e) != 1:
        return False

    t = str(e[0])
    if 'a' <= t[0] <= 'z':
        return True
    return False


def is_variable(e):
    if len(e) != 1:
        return False

    t = str(e[0])
    if 'A' <= t[0] <= 'Z':
        return True
    return False


# apply subs to e
def apply(subs, e):
    for s in subs:
        for i in range(len(e)):
            if type(e[i]) is list:
                e[i] = apply(subs, e[i])
            elif e[i] == s[1] and is_variable(e[i]):
                e[i] = s[0]
    return e


# compose s1 and s2
def composition(s1, s2):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1

    s = apply(s2, s1)
    return s + s2
