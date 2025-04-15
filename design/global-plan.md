# Plan for the project

## How it works

Algebra step : simplify polynomial
Build moment matrix constraint by constraint

For each variable,
- try to simplify with the constraints
- add to the moment matrix

Example of simplification:
if we get the constraint $X_0^2 - X_0 = 0$
$X_0^2$ is not added to the moment matrix

## Parts of the package

1. Algebraic manipulation
2. Building moments matrices
3. Talking to the solver

## Manipulation of monomials

Get an object that represent monomials and polynomials.

### Use sympy

Their is a bug in polynomial simplification.

### Build from scratch

Simple for commutative polynomials
Harder for non commutative polynomials
