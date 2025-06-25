# Ground State

Hermitian matrix -> lowest eigenvalue

## Interaction Hamiltonian

$H = \bold 1 \otimes \bold 1 - X \otimes X - Y \otimes Y - Z \otimes Z$

With $X, Y, Z$ being the Pauli matrices.
We have $\sigma_i^2 = \bold 1$
and $[\sigma_i, \sigma_j] = 2i \epsilon_{ijk} \sigma_k$.

With $\epsilon_{ijk} = \epsilon_{jki} = \epsilon_{kij} = 1$,
$\epsilon_{jik} = -\epsilon_{ijk}$, $\epsilon_{kji} = -\epsilon_{ijk}$,
and $\epsilon_{ijk} = 0$ if any two indices are equal.

> This is only an example in the case of dimension 2.

## Ground State and Graphs

$X \in \mathcal L(\mathcal H)$
$H_{i,j} \in \mathcal L(\mathcal H^n)$

$H = \sum_{(i,j) \in E} H_{i,j}$

$H_{i,j} = \bold 1 - 1 \otimes 1 \otimes ... \otimes X_i \otimes 1 ... X_j - Y_i Y_j - Z_i Z_j$

Where $E$ is the set of edges in a graph.

We search for the ground state of $H$.

When the dimension of the Hilbert space is large, finding the ground state becomes challenging. So we use relaxation techniques to approximate the ground state.

When we have the ground state, we have information about the graph structure. The ground state can be used to infer properties of the graph, such as connectivity and clustering.
