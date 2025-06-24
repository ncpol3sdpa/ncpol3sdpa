import numpy as np
import math
from ncpol3sdpa import Constraint, Problem
from sympy.physics.quantum import HermitianOperator


"""Passer d'un problème state-ground  à deux corps à un problème polynomial"""
"""Cela revient a remplacer les conditions de relaxation du problème state-ground pour qu'elles correspondent a  un problème polynomial"""


""" https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.021008  to go from ground state problem to polynomial problem """

"""The studied space has two bodies"""


class Ground_state:
    def __init__(
        self,
        d: int,  # d**2 corresponds of the size of the matrix rho
        H: np.array(),
        rho: np.array(),
        # H:List[List[float]] ,
        # rho:List[List[float]],
    ):
        monomials = []
        for i in range(2 * d**2):
            X: HermitianOperator = HermitianOperator("X")
            monomials.append(X)

    """ l'ensemble des symboles utilisé sont les x(i), ... , X(2*d**2) , chacun vérifiant des propriétés. Il faut tout d'abord exprimer H en Xi """

    def calculate_trace_left(rho) -> np.array():  ### inutile ??
        """Calculate the trace 1 of the matrix to use in the polynomial relaxation"""
        """It represents what sees the second body only"""

        Trace_1 = np.array(math.sqrt(len(rho)))
        for i in range(len(rho)):
            for j in range(len(rho)):
                Trace_1[i, j] = 0
                for k in range(math.sqrt(len(rho))):
                    Trace_1[i, j] += rho[k, i] * rho[k, j]

        return Trace_1

    def calculate_trace_right(rho) -> np.array():  ### inutile ??
        """Calculate the trace 2 of the matrix to use in the polynomial relaxation"""
        """It represents what sees the first body only"""

        Trace_2 = np.array(math.sqrt(len(rho)))
        for i in range(len(rho)):
            for j in range(len(rho)):
                Trace_2[i, j] = 0
                for k in range(math.sqrt(len(rho))):
                    Trace_2[i, j] += rho[i, k] * rho[j, k]

        return Trace_2

    def polynomial_in_equality_of_trace(i: int, j: int):
        d = Ground_state.d
        return (
            Ground_state.monomials[d**2 + (j - 1) * d + i]
            - Ground_state.monomials[(j - 1) * d + i]
        )


def ground_state_problem_to_polynom(Ground_State_problem: Ground_state) -> Problem:
    """ " Return the polynomial problem whcih correspond to the relaxation of the ground state problem"""

    H = Ground_State_problem.H
    rho = Ground_State_problem.rho

    obj = 0
    for i in range(len(H)):
        obj += H @ rho[i, i]

    p = Problem(obj, is_commutative=False)

    #### Rajout des contraintes d'égalité

    Trace_rho = 0
    for i in range(len(rho)):
        Trace_rho += rho[i, i]

    c1 = Constraint.EqualityConstraint(Trace_rho - 1)

    p.add_constraint(c1)
    Trace_1 = Ground_state.calculate_trace_left(rho)
    Trace_2 = Ground_state.calculate_trace_right(rho)

    # for i in range (len(Trace_1)):
    #    for j in range (len (Trace_1)):
    #        c2 = Constraint.EqualityConstraint(Trace_1[i,j] - Trace_2[i,j])

    for i in range(len(Ground_state.d)):
        for j in range(len(Ground_state.d)):
            trace_i_j = 0
            for a in range(len(Ground_state.d)):
                for b in range(len(Ground_state.d)):
                    trace_i_j += rho[a, b][
                        a, b
                    ] * Ground_state.polynomial_in_equality_of_trace(i, j)

            c = Constraint.EqualityConstraint(trace_i_j)
            p.add_constraint(c)
