
## SOS duality

We wish to solve the duality of the following non-commutative problem:

### Notation

Hilbert space $\mathcal H$, linear operators over the Hilbert space $\mathcal H_o$ <br>
vector $v \in \mathcal H$, and $\rho = v v^\dagger$. we have $\lvert\lvert v \rvert\rvert = 1$, ie $\mathrm{tr}(\rho) = 1$ <br>
Set of n x n Hermitian matrices: $\mathrm{Herm}(n) = \lbrace M \in \mathcal M_{k,k}(\mathbb C) : M = M^\dagger \rbrace$

Polynomial Variables: $X_1, \cdots , X_n \in \mathcal H$ <br>
Relaxation order: $k \in \mathbb N$ <br>
Number of monomials of degree less than k: $N\in\mathbb N$  <br>
Vector of all monomials up to degree $k$ : $\omega = \begin{pmatrix} X_1 & X_1^\dagger & X_2 & X_2^\dagger & \cdots & X_1^2 & X_1 X_1^\dagger & \cdots& \end{pmatrix} \in \mathcal M_{1,N} (\mathcal H_o)$ <br>
Variation : $w = v \cdot \omega  = \begin{pmatrix} v X_1 & v X_1^\dagger  & v X_2  &\cdots\; \end{pmatrix} \in \mathcal M_{1,N} (\mathcal H) $<br>
Moment matrix $M = w^\dagger w \in \mathcal M_{N,N} (\mathcal H)$


#### Polynomials relevant to the problem:

Objective polynomial: $c$, $C \in \mathrm{Herm}(N) $ s.t. $ c(X_1, \cdots , X_n) = \langle C \vert M \rangle$ <br>
Zero constraint polynomials: for $0 \leq i \le n_z,$
$$f_i \text{ and } F_i \in \mathrm{Herm}(N) \text{ s.t. } f_i(X_1, \cdots , X_n) = \langle F_i \vert M \rangle$$

Positive constraints: for $0 \leq i \le n_p,$
$$h_i \text{ and } H_i \in \mathrm{Herm}(N) \text{ s.t. } h_i(X_1, \cdots , X_n) = \langle H_i \vert M \rangle$$

PSD constraints: for $0 \leq i \le \widetilde n,$

 * $g_i(X_1, \cdots , X_n)$
 * Localizing moment matrix $M_i \in \mathcal M_{N_i,N_i} (\mathcal H_o)$, $k_i \in \mathbb N$ <br>such that $M_i = w_{k_i}^\dagger g_i w_{k_i}$ <br>
 where $w$ is shortened to up to degree $k_i$
 * for $0 \leq j \le n_{constraint, i}$ :
    * $G_i \in \mathrm{Herm}(N), \Gamma_i \in \mathrm{Herm}(N_i), $ <br>
    * $\langle G_i \vert M \rangle = \langle \Gamma_i \vert M_i \rangle$

$\forall i, c, f_i, g_i, h_i$ are hermitian

### Derivation

#### Primal Problem:

$$\large \begin{gather*} &\max_{\mathcal H, X_1, \cdots , X_n} & \mathrm{tr} \left(\rho \, c(X_1, \cdots , X_n)\right) \\
& \textrm{s.t.} & \mathrm{tr}(\rho f_i(X_1, \cdots , X_n)) = 0 & \forall i\\
& & \mathrm{tr}(\rho h_i(X_1, \cdots , X_n)) \geqslant 0 & \forall i\\
& & g_i(X_1, \cdots , X_n) \succcurlyeq 0 & \forall i\\
& & \mathrm{tr}(\rho) = 1 &\end{gather*}$$

#### Primal SDP Relaxation

$$\large\begin{gather*} & \max_{\bar Z^0, \cdots , \bar Z^{\widetilde n}} & \langle C \vert \bar Z^0 \rangle&  \\

 & \textrm{s.t.} & \langle F_i \vert \bar Z^0 \rangle = 0 &  \forall i\\
 &               & \langle H_i \vert \bar Z^0 \rangle \geqslant 0 &  \forall i\\
 &               & \langle G_{i,j} \vert \bar Z^0 \rangle = \langle \Gamma_{i,j} \vert \bar Z^i \rangle & \forall i, j \\
 &               & \bar Z^i \succcurlyeq 0 & \forall i \\
 &               & \langle E_{0,0} \vert \bar Z^0 \rangle = 1 & \\
\end{gather*}$$

$E_{0,0}$ is the matrix with all zeros exept a 1 at (0,0)

Note that $\bar Z^0$ models the moment matrix, and the other $\bar Z^i$ s correspond to $g_i$ localizing moment matrices

#### Lagrangian

$$
\large
\begin{align*}
\mathcal L\left(\bar Z, \bar A, (\nu_i), (\eta_i),  (\mu_{i,j}), \lambda\right)
=&\ \langle C \vert \bar Z^0 \rangle \ +\\
&\ + \sum_i\nu_{i}\langle F_i \vert \bar Z^0 \rangle + \sum_i\eta_{i}\langle H_i \vert \bar Z^0 \rangle \ + \\
&\ + \sum_{i,j} \mu_{i,j}\left(\langle G_{i,j} \vert \bar Z^0 \rangle - \langle \Gamma_{i,j} \vert \bar Z^i \rangle\right) \ +\\
&\ + \sum_i  \langle \bar A^i \vert \bar Z^i \rangle \ +\\
&\ + \lambda\left(1 - \langle E_{0,0} \vert \bar Z^0 \rangle\right)
\end{align*}
$$
1 term per constraint, and 1 term for the objective

Primal SDP Relaxation is equivelent to:


$$\large\begin{gather*}
& \Large\max_{
   \normalsize\begin{gather*}
   \bar Z^0, \cdots , \bar Z^{\widetilde n} \succcurlyeq 0
   \end{gather*}
}
& \Large\min_{
   \normalsize\begin{gather*}
   \bar A^0, \cdots , \bar A^{\widetilde n} \succcurlyeq 0 \\
   (\nu_{i}), (\mu_{i,j}), \lambda \\
   (\eta_i) \geqslant 0
   \end{gather*}
}
& \mathcal L\left((\bar Z^i), (\bar A^i), (\nu_i), (\eta_i),  (\mu_{i,j}), \lambda\right)
\end{gather*}$$

#### Dual SDP

The dual SDP is $\min \max \mathcal L( \cdots ) = $

$$\large\begin{gather*}
& \Large\min_{
   \normalsize\begin{gather*}
   \bar A^0, \cdots , \bar A^{\widetilde n} \succcurlyeq 0 \\
   (\nu_{i}), (\mu_{i,j}), \lambda \\
   (\eta_i) \geqslant 0
   \end{gather*}
}
& \Large\max_{
   \normalsize\begin{gather*}
   \bar Z^0, \cdots , \bar Z^{\widetilde n} \succcurlyeq 0
   \end{gather*}
}
& \lambda \ + \\
&&& +\ \lang C + \sum_i\nu_{i}F_i + \sum_i\eta_{i} H_i + \sum_{i,j} \mu_{i,j} G_{i,j} + \bar A^0  - \lambda E_{0,0}\vert \bar Z ^0\rang \ +\\\
&&& +\ \sum_i\lang -\sum_{j} \mu_{i,j} \Gamma_{i,j} + \bar A^i  \vert \bar Z ^0\rang \\
\end{gather*}$$

This is equivalent to :

$$\large\begin{gather*}
\Large\min & \lambda \\
{
   \normalsize\begin{gather*}
   \bar A^0, \cdots , \bar A^{\widetilde n} \succcurlyeq 0 \\
   (\nu_{i}), (\mu_{i,j}), \lambda \\
   (\eta_i) \geqslant 0 \\
   \end{gather*}
}
&    C + \sum_i\nu_{i}F_i + \sum_i\eta_{i} H_i + \sum_{i,j} \mu_{i,j} G_{i,j} + \bar A^0  - \lambda E_{0,0} \preccurlyeq 0\\
&   \forall i,   -\sum_{j} \mu_{i,j} \Gamma_{i,j} + \bar A^i   \preccurlyeq  0
\end{gather*}$$

Which can be simplified by adding $-\bar A^i \preccurlyeq 0$ to each side of the PSD-inequality in each new PSD constraint:


$$\large\begin{gather*}
\Large\min & \lambda \\
{
   \normalsize\begin{gather*}
   (\nu_{i}), (\mu_{i,j}), \lambda \\
   (\eta_i) \geqslant 0 \\
   \end{gather*}
}
& \bar Y ^0 = \lambda E_{0,0} - C - \sum_i\nu_{i}F_i - \sum_i\eta_{i} H_i - \sum_{i,j} \mu_{i,j} G_{i,j} \succcurlyeq 0\\
&   \forall i,  \bar Y^i = \sum_{j} \mu_{i,j} \Gamma_{i,j} \succcurlyeq  0
\end{gather*}$$

### SOS Dual

#### Some properties:
$$\begin{align*}
\omega C \omega^\dagger =& \, c(X_1, \cdots X_n) \\
\forall i, \omega F_i \omega^\dagger  =& \, f_i(X_1, \cdots X_n) \\
\forall i, \omega H_i \omega^\dagger  =& \, h_i(X_1, \cdots X_n)
\end{align*}
$$

<!-- TODO -->
At a feasible point of the primal problem, for a given i,j, there exist indicies a,b s.t. :

$$\begin{align*}
w_s\Gamma_{i,j} w_s^\dagger =&\;\mathrm{tr}(\rho \, \bar X^{a} \bar X^{b\dagger}) \\
w_s (g_i \cdot \Gamma_{i,j}) w_s^\dagger =&\; \mathrm{tr}(\rho \, \bar X^{a} g_i \bar X^{b\dagger}) \\
=&\; \lang G_{i,j} \vert M \rang \\
=&\; w G_{i,j} w^\dagger
\end{align*}$$
($w_s$ is a version of $w$ shortened to monomials up to degree $k_i$)

Therefore:
$$\begin{align*}
\forall i, \sum_{j} \mu_{i,j} \omega G_{i,j} \omega^\dagger =&\; \sum_{j} \mu_{i,j} w_s (g_{i,j}\cdot\Gamma_{i,j}) w_s^\dagger \\
=&\; w_s (g_{i,j}\cdot\bar Y^i) w_s^\dagger
=: q_i&
\end{align*}$$

#### Final formulation

By tacking the result of the Dual SDP, which means the values: $\lambda, (\nu_i), (\eta_i),$ and $(\bar Y^i)$, we can get an sos decomposition. Note that $(\mu_{i,j})$ are not needed if you can directly get a $(\bar Y_i)$. If you can only get $\bar A_{i}$ from the solver, then you would need to reconstruct the $\bar Y_i$ s from all the other variables.

Because $(\bar Y^i)$ are PSD, then $\omega\bar Y^0 \omega^\dagger = s_0$ is a SOS polynomial, for which the SOS decomposition can be retrieved using the Cholesky decomposition of $\bar Y^0$.

By multiplying by $\omega$ on each side of the PSD constraint of the dual SDP,
$$\begin{align*}
s_0(X_0, \cdots, X_n) =&  \omega\bar Y^0 \omega^\dagger \\
=& \lambda \omega E_{0,0} \omega^\dagger - \omega C\omega^\dagger - \sum_i\nu_{i}\omega F_i \omega^\dagger - \sum_i\eta_{i} \omega H_i\omega^\dagger - \sum_{i,j} \mu_{i,j} \omega G_{i,j}\omega^\dagger \\
=& \lambda \omega E_{0,0} \omega^\dagger - \omega C\omega^\dagger - \sum_i\nu_{i}\omega F_i \omega^\dagger - \sum_i\eta_{i} \omega H_i\omega^\dagger - \sum_{i,j} \mu_{i,j} \omega_s (g_i \cdot \Gamma_{i,j})\omega_s^\dagger \\
=& \lambda \omega E_{0,0} \omega^\dagger - \omega C\omega^\dagger - \sum_i\nu_{i}\omega F_i \omega^\dagger - \sum_i\eta_{i} \omega H_i\omega^\dagger - \sum_{i} \omega_s (g_i \cdot Y_i)\omega_s^\dagger \\
=& \lambda I_N  -  c(X) - \sum_i\nu_{i} f_i(X)  - \sum_i\eta_{i}  h_i(X) - \sum_i q_i(X)
\end{align*}$$

Thus the SOS decomposition of $\lambda I_N - c(X)$:
$$\lambda I_N -  c(X) = s_0(X) + \sum_i\nu_{i} f_i(X)  + \sum_i\eta_{i}  h_i(X) + \sum_i q_i(X)$$

### Conclusion

At a feasible point of the primal polynomial problem $(X_1 , \cdots , X_n)$, $\lambda I_N - c(X)$ is positive semidefinite, and thus for all feasible $X$, $\mathrm{tr} (\rho \, c(X)) \leqslant \lambda$
