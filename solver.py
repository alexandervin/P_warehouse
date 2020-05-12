def squere_equition_solver(a, b, c):
    if any(map(
            lambda v: isinstance(v, (int, float)),
            (a, b, c)
    )):
       raise TypeError
