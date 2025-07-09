def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for sc, tc in zip(s, t):
        if sc in s_to_t:
            if s_to_t[sc] != tc:
                return False
        else:
            s_to_t[sc] = tc

        if tc in t_to_s:
            if t_to_s[tc] != sc:
                return False
        else:
            t_to_s[tc] = sc

    return True
s="paper"
t="title"
print(is_isomorphic(s, t))