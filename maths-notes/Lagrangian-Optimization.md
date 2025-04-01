# Lagrangian Optimization

## Original Problem

$$ \max_X Tr(C X) \\
s.t. Tr(F_i X) = \omega_i \\
Tr(C_j X) \le v_j \\
X \ge 0 $$

## Lagrangian
$$ \begin{align*}
\mathcal L \; = & \quad Tr(C X) \\
& + \sum_i \lambda_i (Tr(F_i X) - \omega_i) \\
& + \sum_j \mu_j (v_j - Tr(C_j X)) \\
& + Tr(XY)
\end{align*}$$
with $Y \ge 0, \lambda_i \in \R, \mu_j \ge 0$

## Lagrangian Problem

$$ \max_X \min_{\lambda, \mu, Y} \mathcal L$$

### Dual Problem

$$ \min_{\lambda, \mu, Y} \max_X \mathcal L$$