# Simulating independently sampled frames

The [logarithmic-seed schedule](seed.md) reproduces the error scale of independent frames at bounded total coupling. Higher-order independence also approximates the independent-frame process itself. The comparison uses the same bath, slot dynamics and logical tester under both schedules.

## Approximation theorem

Use the [joint slot model](model.md) and write $`S=\sum_{j=1}^n\beta_j^2`$ and $`L=\sqrt3\sum_{j=1}^n\beta_j`$. For an integer $`2\le t\le n`$, draw $`t`$-wise independent uniform Pauli frames. Let $`\rho_{\mathrm{seed}}`$ and $`\rho_{\mathrm{iid}}`$ denote the accessible outputs of the same tester with the short seed and independent frames, respectively. Then

```math
\sup_{\mathrm{testers}}
\frac12\|\rho_{\mathrm{seed}}-\rho_{\mathrm{iid}}\|_1
\le 2S\sum_{r=t-1}^{\infty}\frac{(2L)^r}{r!}.
```

One explicit choice uses $`m=\max\{1,\lceil\log_4 n\rceil\}`$ and $`n`$ distinct points of $`\mathbb F_{4^m}`$. Draw $`t`$ independent uniform coefficients in that field for a polynomial of degree at most $`t-1`$. Evaluate at the $`n`$ points and apply a fixed surjective $`\mathbb F_4`$-linear map to each value. Any $`t`$ evaluations are jointly uniform by Vandermonde invertibility. The linear projection therefore gives $`t`$-wise uniform Pauli labels using exactly $`2mt`$ independent uniform bits.

At fixed $`L`$, increasing $`t`$ drives the relative error bound down factorially. For example, choosing $`t`$ of order $`\log n/\log\log n`$ with a suitable fixed constant gives a bound of order $`S n^{-c}`$ for any fixed $`c>0`$, and takes $`O((\log n)^2/\log\log n)`$ bits. This statement is asymptotic in $`n`$ with $`L`$ bounded. Independent frames remain available at cost $`2n`$ bits.

## Proof

Purify the tester and bath as in the [process bound](process-bound.md). Expand the final vector as $`v=\sum_{j=0}^n v_j`$, where each term in $`v_j`$ includes nonidentity coefficients at exactly $`j`$ slots. The coefficient of any term in $`|v_j\rangle\langle v_k|`$ is a product of characters with support on at most $`j+k`$ slots. Its expectation is identical for both distributions if $`j+k\le t`$. Keep the same bath purification in both expectations.

For either distribution the distinct nonidentity sign functions at the same slot are orthogonal, and the sign functions at distinct slots are orthogonal by pairwise independence. Thus the last-slot argument in the process theorem gives, for each $`j\ge1`$,

```math
\bigl(\mathbb E\|v_j\|^2\bigr)^{1/2}
\le \sqrt S\,\frac{L^{j-1}}{(j-1)!}.
```

First consider terms with $`j,k\ge1`$. For one distribution, the trace norm of the average of each cross term is bounded by

```math
\left\|\mathbb E|v_j\rangle\langle v_k|\right\|_1
\le S\,\frac{L^{j+k-2}}{(j-1)!(k-1)!}.
```

This follows from the trace norm of a rank-one operator and Cauchy–Schwarz. Summing over $`j+k>t`$ gives at most $`S\sum_{r\ge t-1}(2L)^r/r!`$ for each distribution by the binomial identity.

The remaining unmatched terms have $`j=0`$ or $`k=0`$. Under independent frames every $`v_j`$ with $`j\ge1`$ has mean zero. Under the short seed, the mean-amplitude estimate in the process bound applies because $`t`$-wise independence includes pairwise independence. It gives $`\|\mathbb E v_j\|\le S L^{j-2}/(j-2)!`$ for $`j\ge2`$. Since $`\|v_0\|\le1`$, the two cross terms involving $`v_0`$ contribute at most $`2S\sum_{r\ge t-1}L^r/r!`$ to the unhalved difference. Combining the bounds, tracing out the bath, and dividing by two proves the result.

## Exact reproduction can need exponentially many schedules

Take a bath-free qubit and the same unitary in each slot, with every coefficient in $`U=\sum_{a=0}^3 u_a\sigma_a`$ nonzero. For example use

```math
U=\cos(\theta)I+
\frac{i\sin(\theta)}{\sqrt3}(X+Y+Z),
\qquad 0\lt\theta\lt\pi/2.
```

A tester supplies a fresh half Bell pair in every slot, then stores the output with its partner. With independent Pauli frames, the saved state is a tensor product of full-rank one-slot Choi states. Each slot is full rank because Pauli conjugation averages over the four orthogonal sign vectors and leaves all four diagonal weights $`|u_a|^2`$ positive. Thus the tester output has rank $`4^n`$.

Every deterministic unitary-frame schedule gives a pure output for this tester. A mixture of fewer than $`4^n`$ schedules has smaller rank and cannot reproduce the independent-frame output exactly. Therefore exact reproduction for this example requires at least $`2n`$ uniform bits, even when the finite family can use arbitrary unitary frames. The rank argument is a support-size bound for nonuniform ensembles.

For Pauli schedules one can say more. The four possible one-slot output kets have an invertible coefficient matrix in the Bell basis, given by the Pauli sign matrix times an invertible diagonal matrix. Their tensor products form a basis. If a linear combination of their outer products vanishes, conjugating by the inverse basis matrix leaves a diagonal matrix whose entries are the coefficients. Hence their mixture weights are unique. Exact reproduction with Pauli schedules requires the full uniform product distribution.

This example also fits the bounded-coupling regime by setting $`\theta=a/n`$ for a fixed positive $`a`$ small enough for all the stated slot angles. Compare the [finite rank and distance checks](../verification/README.md).
