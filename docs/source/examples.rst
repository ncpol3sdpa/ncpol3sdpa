Examples
========

Example 1: Simple Polynomial Optimization
-----------------------------------------

Here's a simple example to get you started:

.. math::

   \begin{align}
   \max_{x, y} &\quad\quad x \cdot y\\
   \text{s.t.} &\quad\quad x^2 - x &= 0 \\
               &\quad\quad -y^2 + y + 0.25 &\geq 0
   \end{align}

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint, SolverList
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
   print(f"CVXPY : {problem.solve(relaxation_order=2, solver=SolverList.CVXPY)}")
   print(f"MOSEK : {problem.solve(relaxation_order=2, solver=SolverList.MOSEK)}")


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

This example shows how to obtain a basic Sum-of-Squares decomposition certificate (SOS) for a problem.
Consider the following problem:
.. math::

   \begin{align}
   \max_{x, y} &\quad\quad  4 x y -(x + y)^2 \\
   \end{align}


.. code-block:: python

   from ncpol3sdpa import Problem, Constraint
   from sympy.abc import x, y
   import sympy

   # Define objective function
   objective = -sympy.expand((x + y)**2 - 4* x * y)

   # Create problem
   problem = Problem(obj, is_real=True)

   # Solve the problem (default solver is CVXPY)
   result = problem.solve()
   print(f"Optimal value: {result.dual_objective_value}")

   # Extract SOS decomposition
   sos = problem.compute_sos_decomposition()

   # This is a sum of squares decomposition of the objective, proving that objective <= result.dual_objective_value
   obj_decomposition = sos.reconstructed_objective()
   print(obj_decomposition)

   # Because of floating-point rounding errors, there is a difference between the objective and the decomposition
   # the following function mesures this error:
   error = sos.objective_error()
   print("sos error=", error)

In this case, result.dual_objective_value is 0, so we prove that $(x + y)^2 \geq 4 x y$,
proving the AM-GM inequality.

This example is without constraints. With each constraint that is added, there are additional
terms that appear in the SOS decomposition.

For more information about SOS, see the :doc:`sos` and :doc:`api/SOS` section.

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


.. toctree::
   :maxdepth: 2
   :caption: Contents
