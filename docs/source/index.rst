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

You will need a mosek license to use the solver. You can get a free academic license from the [Mosek website](https://www.mosek.com/).

.. code-block:: console

   (docs) $ make html


you can use the ``src.ncpol3sdpa.momentmatrix.needed_monomials``.


Project Structure
-----------------

.. toctree::
   :maxdepth: 2

   Home <self>
   
   constraints
   funs
   momentmatrix
   monomial
   problem
   rules
   solver

