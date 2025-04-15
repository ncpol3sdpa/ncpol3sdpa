# Exercise 1

We want to show that $(x+y)^2 - 4xy \ge 0$

## Question 1

The moment matrix is :

$M = \begin{bmatrix} 1 & x & y \\ x & x^2 & xy \\ y & yx & y^2 \end{bmatrix}$

## Question 2

$M$ semi-positive definite
So $\forall X,X^\top M X \ge 0$


For $X = (0, -1, 1)$
We get $(x+y)^2 - 4xy \ge 0$

## Question 3

$w = (1,x,y)^\top$

$M = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & -1 & 1 \end{bmatrix}$
$N = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}$

We have $M = N^\top N$
$w^\top M w = w^\top N^\top N w = (Nw)^\top Nw = ||Nw||^2 \ge 0$
So $(x+y)^2 - 4xy \ge 0$
