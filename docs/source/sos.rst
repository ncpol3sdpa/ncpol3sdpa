Sum of Squares decomposition (SOS)
==================================

Introduction
------------

ncpol3sdpa supports extracting a certificate that the value it gives is an upper bound on the
objective polynomial. This certificate takes the form of an SOS decomposition of the objective
polynomial. This is how it works:

The fundamental idea is to expresses :math:`\lambda - c` as sum of positive values.
:math:`\lambda` is an upper  bound, recuperated from the dual objective function. "Sum of Squares"
is a little bit of a misnomer, as the terms in the decomposition can include, but are not limited
to squares of polynomials :math:`p^\dagger p` (for some polynomial :math:`p` ). In the special case
of an unconstrained polynomial optimisation problem, this name is in fact accurate, as
:math:`\lambda - c` is written as a sum of squares of polynomials :math:`SOS` :

.. math::

    \begin{equation}
    \lambda - c  = SOS \tag{1}
    \end{equation}

The exact decomposition is stored in the
:py:attr:`SosDecomposition.SOS<ncpol3sdpa.sos.SosDecomposition.SOS>` attribute.
See also the :py:attr:`~ncpol3sdpa.sos.SumOfSquaresTerm` class(in this case
:py:class:`~ncpol3sdpa.sos.SumOfSquaresTerm.middle_term` should be 1).

.. note::

    The simplest way to access the sos decomposition is through
    :py:meth:`~ncpol3sdpa.sos.SosDecomposition.reconstructed_objective`
    or the varus :func:`to_expression` functions, however it may be cumbersome or slow to go
    through sympy expressions when working with large polynomials, in which case the data can
    be accessed directly by accessing the data felids of the
    :py:class:`~ncpol3sdpa.sos.SumOfSquaresTerm` and
    :py:class:`~ncpol3sdpa.sos.SOS_EqConstraintTerms` classes


Constraints terms
-----------------

For each constraint that is added, a corresponding term, which is positive at the :math:`v`,
is appended to the decomposition, i.e. the right side of equation :math:`(1)` .

PSD inequality constraint term
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With each constraint of the form :math:`g_i \succcurlyeq 0` that is added, the following term is appended
to the decomposition:

.. math::

    SOS_i = \sum_j p_j^\dagger g_i p_j

For some family of polynomials :math:`(p_j)` . For every feasible point :math:`(x_f, v)`, :math:`g_i(x_f)` is
positive semidefinite, and therefore :math:`v^\dagger p_j(x_f)^\dagger g_i(x_f) p_j(x_f) v \geqslant 0` .

The exact :math:`(p_j)` s are stored in :py:attr:`SosDecomposition.SOS_i<ncpol3sdpa.sos.SosDecomposition.SOS_i>` attribute.
See also the :py:class:`~ncpol3sdpa.sos.SumOfSquaresTerm` class.

Trace inequality constraint term
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With each constraint of the form :math:`v^\dagger  h_i v = \mathrm{tr} (\rho h_i) \geqslant 0` that is added,
the following term is appended to the decomposition:

.. math::

    \eta_{i}  h_i

with :math:`\eta_i \geqslant 0` . For every feasible point :math:`(x_f, v)`,
:math:`\eta_i v^\dagger h_i(x_f) v \geqslant 0`

The coefficient of this term (:math:`\eta_{i}` ) is stored in
:py:attr:`SosDecomposition.trace_terms<ncpol3sdpa.sos.SosDecomposition.trace_terms>` .
See the :py:class:`~ncpol3sdpa.sos.SOS_TraceConstraintTerm` class for more details.


Equality constraint term
~~~~~~~~~~~~~~~~~~~~~~~~

With each constraint of the form :math:`f_i = 0` that is added, this implies

.. math::

    \forall M, N \text{monomials},  \mathfrak{Re}\left(\mathrm{tr} (\rho M^\dagger f_{i} N)\right) = 0 \\
    \forall M, N \text{monomials},  \mathfrak{Im}\left(\mathrm{tr} (\rho M^\dagger f_{i} N)\right) = 0

These constraints are encoded in the SDP. Thus, the following term is appended to the decomposition:

.. math::

    \sum_{M, N \text{monomials}}\left( \nu_{i, M, N}^{\mathfrak{Re}} \frac {M^\dagger f_{i} N + N^\dagger f_{i}^\dagger M} {2}
                                      +\nu_{i, M, N}^{\mathfrak{Im}} \frac {M^\dagger f_{i} N - N^\dagger f_{i}^\dagger M} {2i} \right)

For every feasible point :math:`x_f`, :math:`f_i(x_f)` is zero, so each term in the sum above is zero,
and therefore positive.

The coefficients of this term (:math:`\nu_{i, M, N}^{\mathfrak{Re}}` s and
:math:`\nu_{i, M, N}^{\mathfrak{Im}}` s) are stored in
:py:attr:`SosDecomposition.eq_terms<ncpol3sdpa.sos.SosDecomposition.eq_terms>` .
See the :py:class:`~ncpol3sdpa.sos.SOS_EqConstraintTerms` class for more details.

.. note::

    In case the problem is real, the :math:`\nu_{i, M, N}^{\mathfrak{Im}}` term is zero and is not stored


Full decomposition formula
--------------------------

In the most general case, the SOS decomposition is written like so:

.. math::
    \begin{align}
    \tag{2}
    \lambda -  c =& \, SOS \\
      &+ \sum_i SOS_i \\
      &+ \sum_i\eta_{i}  h_i  \\
      &+ \sum_i\sum_{M, N \text{monomials}}\left( \nu_{i, M, N}^{\mathfrak{Re}} \frac {M^\dagger f_{i} N + N^\dagger f_{i}^\dagger M} {2}  \\
                                                + \nu_{i, M, N}^{\mathfrak{Im}} \frac {M^\dagger f_{i} N - N^\dagger f_{i}^\dagger M} {2i} \right)
    \end{align}

where :math:`SOS_i = \sum_j p_j^\dagger g_i p_j` for some family of polynomials :math:`(p_j)` .
