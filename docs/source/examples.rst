Examples
========

Example 1: Simple Polynomial Optimization
-----------------------------------------

Here's a simple example to get you started:

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint
   from sympy.abc import x, y

   # Define objective function
   objective = x*y

   # Create problem
   problem = Problem(objective)

   # Add constraints
   problem.add_constraint(Constraint.InequalityConstraint(1 - x**2 - y**2))

   # Solve the problem
   result = problem.solve(relaxation_order=2)
   print(f"Optimal value: {result}")

Example 2: Max-Cut Problem
--------------------------

This example shows how to solve a Max-Cut problem using ncpol3sdpa.

.. code-block:: python

   # Example code for Max-Cut will be provided here

Example 3: Quantum Correlation
------------------------------

This example shows how to compute quantum correlations.

.. code-block:: python

   # Example code for quantum correlations will be provided here

More examples will be added as the library matures.
