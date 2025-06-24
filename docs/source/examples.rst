Examples
========

Example 1: Simple Polynomial Optimization
-----------------------------------------

Here's a simple example to get you started:

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint, AvailableSolvers
   from sympy.abc import x, y

   # Define objective function
   objective = x*y

   # Create problem
   problem = Problem(obj, is_real=True)

   # Add constraints
   c1 = Constraint.EqualityConstraint(x * x - x)
   c2 = Constraint.InequalityConstraint(-y * y + y + 0.25)
   problem.add_constraint(c1)
   problem.add_constraint(c2)

   # Solve the problem (default solver is CVXPY)
   result = problem.solve(relaxation_order=2)
   print(f"Optimal value: {result}")

   # Select a particular solver
   print(f"CVXPY : {problem.solve(relaxation_order=2, solver=AvailableSolvers.CVXPY)}")
   print(f"MOSEK : {problem.solve(relaxation_order=2, solver=AvailableSolvers.MOSEK)}")


Example 2: Non-commutative Complex Polynomial Optimization
----------------------------------------------------------

This example demonstrates how to solve a non-commutative complex polynomial optimization problem.

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint
   from sympy.physics.quantum import HermitianOperator

   a = HermitianOperator("a")
   b = HermitianOperator("b")

   obj = a ** 2 - 0.5 * a * b - 0.5 * b * a - a.adjoint()

   p = Problem(obj, is_commutative=False, is_real=False)

   c1 = Constraint.InequalityConstraint(a - a**2)
   c2 = Constraint.InequalityConstraint(b - b**2)
   p.add_constraint(c1)
   p.add_constraint(c2)

   print(f"Optimal value: {p.solve(relaxation_order=2)}")

Example X: Max-Cut Problem
--------------------------

This example shows how to solve a Max-Cut problem using ncpol3sdpa.

.. code-block:: python

   # Example code for Max-Cut will be provided here

For more information about Max-Cut, see the :doc:`api/max_cut` section.

Example X: Sum-of-Squares (SOS) Optimization
--------------------------------------------

This example shows how to perform Sum-of-Squares (SOS) optimization.

.. code-block:: python

   # Example code for Sum-of-Squares (SOS) optimization will be provided here


For more information about SOS, see the :doc:`api/SOS` section.

Example X: Ground State Preparation
-----------------------------------

This example demonstrates how to prepare the ground state of a quantum system.

.. code-block:: python

   # Example code for ground state preparation will be provided here

Example X: BB84 Quantum Key Distribution
-----------------------------------------

This example demonstrates how to implement the BB84 quantum key distribution protocol.

.. code-block:: python

   # Example code for BB84 will be provided here
