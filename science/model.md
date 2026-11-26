# Model and error criterion

A controller protects a data qubit $`Q`$ through $`n\ge 1`$ time slots. In slot $`t`$ an unknown joint unitary $`U_t`$ acts on $`Q`$ and a finite bath $`E`$. The same bath passes from slot to slot and can keep quantum information from earlier interactions. The initial bath state is independent of the controller's seed and of the data and tester. The sequence of unitaries is fixed independently of the sampled seed. It can depend on time and on the published schedule family.

The controller draws one private classical seed. For each slot it applies a Pauli $`P_t`$ to $`Q`$ before $`U_t`$ and applies $`P_t^\dagger`$ afterward. Both frame operations are ideal. In the resulting logical ports the slot unitary is

```math
\widetilde U_t=(P_t^\dagger\otimes I_E)U_t(P_t\otimes I_E).
```

Each port presents the qubit in the same logical coordinates. A tester can prepare an arbitrary state of the qubit and its own registers, apply operations at every port, use earlier measurement outcomes in later decisions, and read an arbitrary final quantum or classical register. Its strategy has access to the qubit and its own registers. The bath, seed and control records are private. Slot times and the sequence of bath interactions are fixed. If the qubit is kept idle at all interior ports, the controller can combine the two adjacent Pauli operations into a single update.

The ideal reference supplies identity wires on $`Q`$ in all slots. For two processes $`\mathfrak P,\mathfrak Q`$ on these ports, define their operational distance by

```math
d(\mathfrak P,\mathfrak Q)
=\sup_{\mathcal T}\frac12
\left\|\rho_{\mathfrak P,\mathcal T}-\rho_{\mathfrak Q,\mathcal T}\right\|_1.
```

Here $`\rho_{\mathfrak P,\mathcal T}`$ is the tester's accessible output averaged over the private seed. The supremum includes testers that keep a reference entangled with the input and retain quantum records between slots.

## Measuring the strength of a slot

Write $`\sigma_0=I_Q`$, $`\sigma_1=X`$, $`\sigma_2=Y`$ and $`\sigma_3=Z`$. The Pauli expansion and the weights used throughout are

```math
\begin{aligned}
U_t&=\sum_{p=0}^3\sigma_p\otimes B_{tp},
&B_{tp}&=\tfrac12\operatorname{Tr}_Q[(\sigma_p\otimes I_E)U_t],\\
w_{tp}&=\|B_{tp}\|_\infty\quad(p\ne0),
&\beta_t^2&=\sum_{p=1}^3w_{tp}^2,\\
S&=\sum_{t=1}^n\beta_t^2,
&L&=\sqrt3\sum_{t=1}^n\beta_t.
\end{aligned}
```

Taking the normalized qubit partial trace of $`U_t^\dagger U_t=I`$ gives

```math
B_{t0}^\dagger B_{t0}+\sum_{p=1}^3 B_{tp}^\dagger B_{tp}=I_E.
```

Thus $`B_{t0}`$ is a contraction with $`0\le I_E-B_{t0}^\dagger B_{t0}\le\beta_t^2 I_E`$. For a closed qubit rotation $`U_t=e^{i\theta_t\boldsymbol u_t\cdot\boldsymbol\sigma}`$ about a unit axis $`\boldsymbol u_t`$, one has $`\beta_t=|\sin\theta_t|`$.

If $`\|U_t-I_Q\otimes V_t\|_\infty\le\epsilon_t`$ for a bath unitary $`V_t`$, then $`w_{tp}\le\epsilon_t`$ for every $`p\ne0`$. Indeed the bath-only term drops out of the coefficient above, and normalized qubit partial trace is contractive in operator norm, as is evident by averaging its diagonal blocks. This implies $`\beta_t\le\sqrt3\epsilon_t`$. For example, a time-dependent Hamiltonian of the form $`I_Q\otimes H_E(s)+H_{\mathrm{int}}(s)`$ gives $`\epsilon_t\le\int_{\text{slot }t}\|H_{\mathrm{int}}(s)\|_\infty\,ds`$ by integrating the propagator in the bath interaction picture, in units with $`\hbar=1`$.

## Scaling and resources

The [finite process bound](process-bound.md) is expressed in the actual slot strengths, including unequal ones. When $`\sum_t\beta_t\le A`$ for a fixed constant $`A`$, the distance is $`O_A(S)`$. For example, $`\beta_t\le A/n`$ for each $`t`$ gives $`S\le A^2/n`$. For unequal strengths, $`S\le(\max_t\beta_t)\sum_t\beta_t`$. Subdivision reduces the bound when it reduces the largest coupling per slot at fixed total coupling. A single strong slot can dominate $`S`$.

The resource compared here is the number of uniform random bits per run for [generating the frame schedule](seed.md). The controller also uses classical computation to evaluate each frame and ideal local Pauli operations at the slot boundaries. The [converse](converse.md) compares finite ensembles of open-loop unitary controls on the same qubit, with no trusted alternate memory and no uncounted random choices.
