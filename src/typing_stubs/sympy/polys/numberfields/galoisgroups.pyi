from sympy.polys.numberfields.galois_resolvents import GaloisGroupException

__all__ = ['galois_group']

class MaxTriesException(GaloisGroupException): ...

def galois_group(f, *gens, by_name: bool = False, max_tries: int = 30, randomize: bool = False, **args): ...
