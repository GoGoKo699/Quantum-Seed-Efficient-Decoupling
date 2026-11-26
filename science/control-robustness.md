# Control robustness and seed leakage

## Comparing implemented and ideal dressed slots

Let $`Q`$ denote the protected qubit and $`E`$ the retained device memory in the [process model](model.md). For a seed $`s`$ and slot $`t`$, the reference channel $`\mathcal C_{s,t}`$ on $`QE`$ is conjugation by $`(P_t(s)^\dagger\otimes I)U_t(P_t(s)\otimes I)`$. The joint slot unitary $`U_t`$ is common to all seeds and may vary with $`t`$. Let $`\mathcal A_{s,t}`$ be the corresponding implementation on the same joint space, with the same corrected logical ports. Write $`\mathfrak A`$ for the averaged implemented process. Any implementation memory that persists between slots belongs in $`E`$. Define

```math
\delta_t = \max_s\frac12\left\|\mathcal A_{s,t}-\mathcal C_{s,t}\right\|_\diamond.
```

The diamond norm here is a joint-channel norm, including a reference system. Agreement on the reduced qubit channel for a fixed bath state is insufficient because earlier interventions can change the bath state and its correlations with the qubit.

Fix any adaptive tester that acts only on the corrected logical ports and retains its own records. At a fixed seed, replace the implementation channels one at a time by the reference channels. Each replacement changes the tester's accessible output by at most $`\delta_t`$ in half trace norm. This uses the input bound from the diamond norm and contractivity under the remaining channels, including the tester's operations. Averaging over the seeds and taking the supremum over testers preserves the bound. With an independent uniform seed and the bath initialized independently of the tester and data, the [process bound](process-bound.md) gives

```math
d(\mathfrak A,\mathfrak I)
\le \min\left\{1,\frac{(1+e^L)^2}{2}S+\sum_{t=1}^n\delta_t\right\},
\qquad
S=\sum_{t=1}^n\beta_t^2,\qquad L=\sqrt 3\sum_{t=1}^n\beta_t.
```

The sum of slot errors can be necessary. With identity reference slots and an implementation that inserts the same logical rotation $`e^{i\gamma Z}`$ at each slot, $`\delta_t=|\sin\gamma|`$ for $`|\gamma|\le\pi/2`$. An idle Bell-pair tester observes half trace distance $`|\sin(n\gamma)|`$ after the $`n`$ slots, which is asymptotic to $`\sum_t\delta_t`$ as $`n|\gamma|\to0`$.

## Pulse budgets

One route to a joint discrepancy bound is an explicit finite-duration Hamiltonian model. Suppose the reference and implemented dressed slots have unitary realizations on a common joint space and over the same time interval. If their joint Hamiltonians $`H^{\mathrm{ref}}_{s,t}(u)`$ and $`H^{\mathrm{act}}_{s,t}(u)`$ differ, unitary Duhamel comparison gives

```math
\delta_t
\le \max_s\int_{\mathrm{slot}\ t}
\left\|H^{\mathrm{act}}_{s,t}(u)-H^{\mathrm{ref}}_{s,t}(u)\right\|_\infty\,du
```

in units with $`\hbar=1`$. The half diamond norm between two unitary channels is bounded by the operator-norm distance between the implementing unitaries. In particular, a mismatch of norm at most $`g_t`$ confined to pulse windows of total length $`\tau_t`$ contributes at most $`g_t\tau_t`$ to the sum. This comparison requires a reference evolution with the stated common slot unitary after the frame dressing is included. It requires actual bounds on the joint Hamiltonians and a timing model for the pulses.

At bounded $`L`$, an implementation budget $`\sum_t\delta_t=O(S)`$ preserves the order of the reference guarantee. For equal slots with $`\beta_t\le a/n`$ and fixed $`a>0`$, a uniform slot allowance $`\delta_t\le\delta`$ gives a certificate of the form $`C_a a^2/n+n\delta`$. The two terms cross at $`n=a\sqrt{C_a/\delta}`$ for fixed $`\delta>0`$, treating $`n`$ as continuous. Keeping the certified $`O(1/n)`$ scaling as $`n`$ grows requires a uniform allowance of order $`1/n^2`$ or an aggregate allowance of order $`1/n`$ in this bound. The crossover describes the certificate. Hardware performance depends on the pulse and noise model that supplies the slot bounds.

## Initial exposure of the seed

Let $`R`$ be the classical seed register, with uniform state $`\omega_R`$, and let $`\rho_{RE}`$ be its joint state with the initial bath. Keep the tester and data independent of $`RE`$. Define

```math
\eta=\frac12\left\|\rho_{RE}-\omega_R\otimes\rho_E\right\|_1.
```

Treat the entire protocol, including conditional control on $`R`$, as one channel from the initial registers to the tester's accessible output. Replacing $`\rho_{RE}`$ by the independent product can change that output by at most $`\eta`$. This term enters once, increasing the combined certificate to

```math
d(\mathfrak A,\mathfrak I)
\le\min\left\{1,\frac{(1+e^L)^2}{2}S+\sum_{t=1}^n\delta_t+\eta\right\}.
```

Any exposure later in the protocol needs its own model. For example, a device interaction that writes frame information into retained memory during a pulse can enter through its joint slot discrepancy.

### A fixed joint unitary can exploit a leaked seed

Knowing the control parity can preserve coherent error accumulation, as illustrated by Winick et al. The example below quantifies a different exposure model, where the retained bath receives the entire seed at initialization with a specified probability. [Winick et al., Sec. III.3](https://arxiv.org/html/2212.07500v1#S3.SS3)

Suppose a classical bath register holds the full seed $`s`$ with probability $`q`$, and otherwise holds an erasure symbol. For a seed space of size $`M`$, $`\eta=q(1-1/M)`$. This follows by comparing the diagonal correlated distribution with the uniform distribution on seed–label pairs, conditional on the register having a non-erasure label.

On each bath label $`\ell`$ that represents a seed, choose the raw slot unitary to act on the qubit as $`P_t(\ell)e^{iaZ/n}P_t(\ell)^\dagger`$. On the erasure label it acts as the identity. These blocks define one fixed joint unitary per slot. For $`0\lt a\le\pi/2`$, the only nonidentity Pauli coefficient is the $`Z`$ coefficient and $`S=n\sin^2(a/n)\le a^2/n`$.

The seed-independent idle tester keeps one half of a Bell pair. In an erasure run its output is ideal. In a revealed run the dressed rotation is $`e^{iaZ/n}`$ in every slot, so the final logical action is $`e^{iaZ}`$. The separation between the averaged actual and ideal Bell outputs is exactly $`q|\sin a|`$ in half trace norm. At fixed nonzero $`q`$ and $`a`$, small slot coefficients coexist with a constant tester error. This gives a matching linear dependence on the order of initial leakage in the worst case.
