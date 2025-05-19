Quick Start
==========

Installation
-----------

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/yourusername/python-poly-opt.git
   cd python-poly-opt

2. Install the package:

.. code-block:: bash

   pip install -e .

Basic Example
------------

Here's a simple example to get you started:

.. code-block:: python

   from ncpol3sdpa import Problem, Constraint
   from sympy.abc import x, y
   
   # Define variables
   variables = [x, y]
   
   # Define objective function
   objective = x*y
   
   # Create problem
   problem = Problem(objective)
   
   # Add constraints
   problem.add_constraint(Constraint.InequalityConstraint(1 - x**2 - y**2))
   
   # Solve the problem
   result = problem.solve(relaxation_order=2)
   print(f"Optimal value: {result}")

For more examples, see the :doc:`examples` section.
