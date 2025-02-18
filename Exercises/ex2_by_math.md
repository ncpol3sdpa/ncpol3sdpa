# Exercise 2

## Problem

$$\max _{x1,x2\in\R} 2x_0x_1 \\
\text{s.t.} \left\{{\begin{matrix}
    x_0^2 − x_0 = 0\\
    -x_1^2 + x_1 + \frac 14 \ge 0
\end{matrix}}\right.$$

## Solution

We have $x_0^2 − x_0 = 0$. 
So $x_0 \in \{0, 1\}$.

### Case 1: $x_0 = 0$

The objective function becomes $0$.

### Case 2: $x_0 = 1$

The objective function becomes $2x_1$.

The condition is $-x_1^2 + x_1 + \frac 14 \ge 0$.  
And yet, $-x_1^2 + x_1 + \frac 14 = \frac 12 -\left(x_1 - \frac 12\right)^2$.  
So we need to have $\frac 12 -\left(x_1 - \frac 12\right)^2\ge 0$.  
So we need to have $\frac 12 \ge \left(x_1 - \frac 12\right)^2$.  
So we need to have $x_1 - \frac 12 \in \left[-\frac 1{\sqrt 2}, \frac 1{\sqrt 2}\right]$.  
So we need to have $x_1 \in \left[\frac 12 -\frac 1{\sqrt 2}, \frac 12 + \frac 1{\sqrt 2}\right]$.

So we have $2x_1 \in \left[1 -\sqrt 2, 1 + \sqrt 2\right]$.  
So the maximum is $1 + \sqrt 2$, for $x_1 = \frac 12 + \frac 1{\sqrt 2}$.

## Conclusion

The maximum is :
$$ 1 + \sqrt 2$$
for 
$$ (x_0,x_1) = \left(1,\frac 12 + \frac 1{\sqrt 2}\right)$$