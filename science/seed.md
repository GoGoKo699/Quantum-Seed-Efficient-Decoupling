# Constructing the Pauli schedule

The controller needs uniform Pauli labels whose pairs are independent across distinct time slots. A finite field provides an explicit family using $`2\lceil\log_4(3n+1)\rceil=\log_2 n+O(1)`$ random bits. All subsequent computation is deterministic.

## Finite-field construction

Let $`F=\mathbb F_4`$ and $`m=\lceil\log_4(3n+1)\rceil`$. There are $`(4^m-1)/3`$ one-dimensional subspaces of $`F^m`$. Select $`n`$ distinct subspaces and use one representative $`a_t\ne0`$ of each. The representatives can be generated without a table by enumerating vectors whose first nonzero coordinate equals $`1`$.

Draw $`s\in F^m`$ uniformly, compute $`r_t=s\cdot a_t`$, and use $`r_t`$ as the Pauli label. With $`F=\mathbb F_2[\omega]/(\omega^2+\omega+1)`$, one specific map sends $`r_t=x_t+\omega z_t`$ to $`P_t=X^{x_t}Z^{z_t}`$. Phases cancel in the conjugation. Each individual $`r_t`$ is uniform since $`a_t\ne0`$. For distinct $`t,u`$, the two representatives are linearly independent over $`F`$, so the map $`s\mapsto(r_t,r_u)`$ is surjective and every output pair has the same number of preimages.

## The conjugation signs

Let $`\chi_{tp}(s)`$ denote the sign in $`P_t^\dagger\sigma_pP_t=\chi_{tp}(s)\sigma_p`$. For $`p\ne0`$, the sign takes the form

```math
\chi_{tp}(s)=(-1)^{\mathrm{Tr}_{F/\mathbb F_2}(s\cdot b_{tp})},
\qquad b_{tp}=c_p a_t,
```

where the three values $`c_p`$ run through $`F\setminus\{0\}`$. Conjugation by $`X^xZ^z`$ gives the sign exponents $`z,x+z,x`$ for $`X,Y,Z`$, respectively. These three nonzero binary linear maps on $`F`$ are the three maps $`r\mapsto\mathrm{Tr}_{F/\mathbb F_2}(cr)`$ with $`c\ne0`$.

All $`3n`$ tags $`b_{tp}`$ are distinct and nonzero. Their characters have mean zero and are orthogonal in $`L^2`$ of the uniform seed. Products of characters add the corresponding tags. The average of a product of signs is one if its tag sum vanishes and zero otherwise. The [process proof](process-bound.md) uses this rule to sum over two selected slot labels, as well as pairwise orthogonality after multiplying all signs by a fixed prefix.

## Seed count and pulse sequence

The $`m`$ field elements of $`s`$ require exactly $`2m`$ uniform bits in this construction. Independent Pauli draws use $`2n`$ bits. Both strategies can evaluate the current frame on demand and use the same types of pulse operations at the logical ports. For example, a controller can keep the seed and slot index, generate the tag from that index, and evaluate a field inner product with $`O(m)`$ field operations per slot.

Orthogonality implies at least $`3n+1`$ positive-probability schedules for any distribution with uniform pairwise-independent Pauli labels. The constant function and all $`3n`$ signs form an orthonormal set in the space of functions on that support. The finite-field seed has $`4^m`$ possibilities, with $`3n+1\le4^m<4(3n+1)`$. The [operational converse](converse.md) derives the logarithmic lower bound from the protection task itself, with a larger comparison class of controls.
