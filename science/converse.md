# A lower bound on control randomness

Consider any finite ensemble of open-loop single-qubit unitary schedules using the same idle slots. Each draw fixes all physical control unitaries on the qubit. The controller has no noiseless quantum register into which it can move the state and no additional randomness. The noise may know the ensemble and slot boundaries. It fixes its unitaries before the seed is sampled.

Let $`p_{\max}`$ be the probability of the most probable schedule. Choose slot angles $`\alpha_t\ge0`$ with sum $`a\in(0,\pi/4]`$. There is a closed-qubit noise sequence with these slot angles for which

```math
d(\mathfrak P,\mathfrak I)\ge p_{\max}\sin^2 a .
```

It suffices to use the endpoint tester, which prepares a Bell pair of the qubit and a private reference, performs no interior interventions, and measures whether the output pair is that Bell state.

## Align the noise on one schedule

Fix a most probable schedule and write its physical controls as $`C_0,\ldots,C_n`$, with $`C_0`$ before the first slot and $`C_t`$ after slot $`t`$. Set $`F_t=C_{t-1}\cdots C_0`$ and $`W=C_n\cdots C_0`$. The target branch's final unitary is

```math
W(F_n^\dagger U_n F_n)\cdots(F_1^\dagger U_1 F_1).
```

For a sign chosen once for the whole run, take the fixed noise sequence $`U_t^\pm=F_t e^{\pm i\alpha_t Z}F_t^\dagger`$. Its rotations commute in the chosen branch's coordinates and produce the output $`W e^{\pm iaZ}`$. The noise uses knowledge of the most probable schedule but acts with the same unitaries on every branch.

If the ensemble implements the ideal channel exactly in the zero-noise case, every positive-probability schedule has $`W`$ proportional to the identity. This follows because the Choi state of the ideal channel is pure. The chosen branch then fails the Bell test with probability $`\sin^2 a`$ for either sign. Every other branch has a nonnegative failure probability, so the averaged Bell-test failure is at least $`p_{\max}\sin^2 a`$. The ideal process never fails this test.

The bound also allows a noiseless residual unitary in the chosen branch. With its global phase removed, write $`W=w_0I+i\boldsymbol w\cdot\boldsymbol\sigma`$ for real coefficients satisfying $`w_0^2+\|\boldsymbol w\|^2=1`$. Bell-test success equals $`|\mathrm{Tr}(We^{\pm iaZ})/2|^2`$. Averaging the two signs gives

```math
w_0^2\cos^2 a+w_z^2\sin^2 a\le \cos^2 a .
```

Thus one sign forces that branch to fail with probability at least $`\sin^2 a`$. Again positivity of the other branch failure probabilities proves the bound. This uses the tester's actual outcome distribution on the averaged channel, including when its output is mixed.

## Consequence for seed size

Take equal angles $`\alpha_t=a/n`$ at fixed $`a>0`$. Their strengths obey $`\sum_t\beta_t=n\sin(a/n)\le a`$ and $`S=n\sin^2(a/n)\le a^2/n`$. If the controller guarantees $`d(\mathfrak P,\mathfrak I)\le K S`$ for all allowed sequences in that total-coupling budget, with $`K`$ fixed independently of $`n`$, then

```math
p_{\max}\le\frac{K a^2}{n\sin^2 a},\qquad
H_{\min}=-\log_2 p_{\max}
\ge\log_2 n-\log_2\left(\frac{K a^2}{\sin^2 a}\right).
```

The same lower bound holds for the number of uniform seed bits. A $`b`$-bit seed has at most $`2^b`$ possible schedules, so the largest schedule probability is at least $`2^{-b}`$. The [explicit schedule](seed.md) and [process bound](process-bound.md) achieve the logarithmic order in this same equal-angle regime. The alignment itself permits uneven $`\alpha_t`$. For a prescribed profile the condition becomes $`p_{\max}\sin^2 a\le K\sum_t\sin^2\alpha_t`$. A profile concentrated in a few strong slots can therefore yield a weaker bound on randomness.
