.. ncpol3sdpa documentation master file, created by
   sphinx-quickstart on Tue Mar 18 11:32:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ncpol3sdpa documentation
========================

**ncpol3sdpa** is a Python package for solving noncommutative polynomial optimization problems using the SDPA family of semidefinite programming solvers.

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
   ncpol3sdpa
   quickstart
   examples
   api
   
   generated/problem
   generated/constraints
   generated/momentmatrix
   generated/monomial
   generated/rules
   generated/solver
   generated/funs
