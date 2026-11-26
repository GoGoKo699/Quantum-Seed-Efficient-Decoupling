# Finite error bound for the controlled process

For the [slot model](model.md) and [finite-field frames](seed.md), let $`\mathfrak P_{\rm seed}`$ denote the averaged controlled process and $`\mathfrak I`$ the ideal identity wires. With $`S=\sum_t\beta_t^2`$ and $`L=\sqrt3\sum_t\beta_t`$,

```math
d(\mathfrak P_{\rm seed},\mathfrak I)
\le \min\left\{1,\ \tfrac12(1+e^L)^2 S\right\}.
```

The bound holds for any pairwise independent family of uniform Pauli frames. The proof keeps the same bath throughout and allows arbitrary seed-independent operations at the corrected logical ports. The constant is uniform over bath dimension, tester memory and initial bath state.

## Expand the tester output

Fix a tester. Purify its inputs and the initial bath state separately. Dilate every intervening tester operation to an isometry on the data and tester registers, including registers for outcomes and any subsequent controls. Keeping each dilation register until the end and then discarding it reproduces the original tester. The dilated slot evolution sends the product initial state to a unit vector $`v(s)`$ for each seed $`s`$.

Expand each framed unitary by its Pauli labels. The terms with exactly $`j`$ nonidentity labels sum to $`v_j(s)`$, and

```math
v(s)=v_0+\Delta(s),\qquad
\Delta(s)=\sum_{j=1}^n v_j(s).
```

The coefficient vector of a given term is independent of the seed. Its sign is the product of the corresponding $`\chi_{tp}(s)`$, and its norm is at most the product of the corresponding $`w_{tp}`$. Each intervening isometry and each system Pauli have operator norm one. Every other slot contributes the contraction $`B_{t0}`$ on the bath.

Let $`\psi_{\rm id}`$ be the unit output vector obtained by the dilated tester with identity slots. The degree-zero term factors as $`v_0=\psi_{\rm id}\otimes\eta_n`$ where $`\eta_t=(B_{t0}\otimes I)\eta_{t-1}`$ is the bath and its purification after $`t`$ contractions and $`\|\eta_0\|=1`$. The identity for $`B_{t0}^\dagger B_{t0}`$ gives

```math
0\le\|\eta_{t-1}\|^2-\|\eta_t\|^2
\le\beta_t^2\|\eta_{t-1}\|^2\le\beta_t^2 .
```

Thus $`\|v_0\|\le1`$, and its squared norm differs from one by at most $`S`$.

## Bound the squared deviation

For $`j\ge1`$, fix the first $`j-1`$ nonidentity positions and their labels in a term of $`v_j`$. The last position and label range over all allowed choices after that prefix. Different last choices have orthogonal sign functions. Multiplying them all by the same sign of the prefix preserves orthogonality. Orthogonality makes the mean squared norm of this group equal to the sum of squared norms of its coefficient vectors. Its square root is at most $`\sqrt S`$ times the product of the prefix weights.

Put $`c_t=\sum_{p=1}^3 w_{tp}`$, so $`\sum_t c_t\le L`$. Summing the prefix weights over distinct ordered positions is bounded by the elementary symmetric polynomial in $`c_t`$ of degree $`j-1`$, which is at most $`L^{j-1}/(j-1)!`$. The latter bound follows by expanding $`(\sum_t c_t)^{j-1}`$ and counting each product on distinct positions $`(j-1)!`$ times. The triangle inequality in the seed-averaged vector norm gives

```math
\bigl(\mathbb E_s\|v_j(s)\|^2\bigr)^{1/2}
\le\sqrt S\,\frac{L^{j-1}}{(j-1)!},
\qquad
\mathbb E_s\|\Delta(s)\|^2\le S e^{2L}.
```

## Bound the mean deviation

The following bound uses only pairwise independence. The mean of $`v_1`$ is zero because every slot has uniform Pauli labels. The mean of $`v_2`$ is also zero because its two nontrivial signs come from distinct slots.

For $`j\ge3`$, fix the middle $`j-2`$ nonidentity slots and their Pauli labels. In the slots before the first fixed position exactly one nonidentity position and label can occur, and likewise in the slots after the last fixed position. Write the corresponding sum of vectors as

```math
f(s)G(s)K F(s)\psi .
```

Here $`\psi`$ is the joint input vector. The operators $`F(s)`$ and $`G(s)`$ contain the coherent sum over the allowed first and last choices in their respective segments, including the tester isometries. The middle operator $`K`$ is fixed, with norm at most the product of the middle weights. The scalar $`f(s)`$ is the product of the middle signs, of absolute value one. Every operator coefficient in $`F(s)`$ or $`G(s)`$ has norm at most its own nonidentity weight.

For any unit vector $`w`$ in the output space, take its inner product with the expectation of this group. Cauchy–Schwarz over seeds bounds the absolute value by

```math
\|K\|\,\bigl(\mathbb E_s\|F(s)\psi\|^2\bigr)^{1/2}
\bigl(\mathbb E_s\|G(s)^\dagger w\|^2\bigr)^{1/2}
\le S\|K\|.
```

Within each segment, the nonidentity sign functions are orthogonal in the seed average. For choices at the same slot, this follows from the uniform one-slot Pauli distribution. For choices at distinct slots, it follows from pairwise independence. Each mean squared norm is therefore bounded by its segment's sum of squared weights, which is at most $`S`$. The bound on every inner product gives the same operator-vector norm bound on this group's mean.

Summing the middle weights gives

```math
\|\mathbb E_s v_j(s)\|
\le S\,\frac{L^{j-2}}{(j-2)!},
\qquad
\|\mathbb E_s\Delta(s)\|\le Se^L.
```

## Compare with the ideal output

The averaged density operator differs from $`|v_0\rangle\langle v_0|`$ by two cross terms involving $`\mathbb E_s\Delta`$ and the positive operator $`\mathbb E_s|\Delta\rangle\langle\Delta|`$. The cross terms have total trace norm at most $`2\|v_0\|\|\mathbb E_s\Delta\|`$. The positive term has trace norm $`\mathbb E_s\|\Delta\|^2`$. Tracing out the bath and dilation registers can only decrease the trace norm of their Hermitian sum. The reduced $`|v_0\rangle\langle v_0|`$ is the ideal tester state multiplied by $`\|\eta_n\|^2`$, so replacing it by the ideal state costs at most $`S`$ in trace norm. The final trace norm is bounded by $`S+2Se^L+Se^{2L}`$. Halving and then taking the supremum over testers proves the result.
