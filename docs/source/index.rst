.. ncpol3sdpa documentation master file, created by
   sphinx-quickstart on Tue Mar 18 11:32:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ncpol3sdpa documentation
========================


**ncpol3sdpa** is a Python package for solving noncommutative polynomial optimization problems using semidefinite programming (SDP) solvers.


We solve the following optimization problem:

.. math::

   \begin{align}
   \max_{x_1, \ldots, x_n} &\quad f(x_1, \ldots, x_n) \\
   \text{s.t.} &\quad g_i(x_1, \ldots, x_n) \leq 0 \quad \forall i
   \end{align}

where :math:`f,g_i \in \mathbb{K}[x_1,\ldots,x_n]`.

This library is a successor to the ncpol2sdpa library.

.. note::

   The project is under development and is not yet ready for use.

Installation
------------

You will need a mosek license to use the solver. You can get a free academic license from the `Mosek website <https://www.mosek.com/>`_.


Basic Usage
-----------

Here's a simple example of how to use the package:

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint
   from sympy.abc import x, y

   # Define the objective function
   objective = x*y

   # Create a problem instance
   problem = Problem(objective)

   # Add constraints
   problem.add_constraint(Constraint.InequalityConstraint(1 - x**2 - y**2))

   # Solve the problem
   result = problem.solve(relaxation_order=2)
   print(f"Optimal value: {result}")


Documentation
-------------

.. toctree::
   :maxdepth: 2

   Home <self>
   quickstart
   examples
   api
