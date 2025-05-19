ncpol3sdpa
==========

.. toctree::
   :maxdepth: 2

   problem
   constraints
   momentmatrix
   monomial
   rules
   solver
   funs

Overview
--------

*ncpol3sdpa* is a Python package for solving noncommutative polynomial optimization problems using semidefinite programming (SDP) solvers.


We solve the following optimization problem:

.. math::

   \begin{align}
   \max_{x_1, \ldots, x_n} &\quad f(x_1, \ldots, x_n) \\
   \text{s.t.} &\quad g_i(x_1, \ldots, x_n) \leq 0 \quad \forall i
   \end{align}

where :math:`f,g_i \in \mathbb{K}[x_1,\ldots,x_n]`.

This library is a successor to the ncpol2sdpa library.

This package is not fully functional yet, but it is under development. 
