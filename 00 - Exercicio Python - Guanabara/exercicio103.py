def fatorial(n, show=False):
    """[Calcula O Fatorial De Um Numero]

    Args:
        n ([type]): [O numero a ser calculado]
        show (bool, optional): [Mostrar ou nao ]. Defaults to False.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f += c
    return f
# Programa principal
print(fatorial(5, show=True))
help(fatorial)