# Quantum Seed-Efficient Decoupling

**How much private randomness does a controller need to protect a qubit from a bath that remembers earlier interactions?** For $`n`$ control slots, a single seed of $`\log_2 n+O(1)`$ bits suffices to suppress coherent error throughout the sequence. At fixed total coupling, the process error is $`O(1/n)`$ when the slot strengths are equal. A matching entropy lower bound holds for randomized unitary frame schedules.

Each slot applies a Pauli frame before the joint qubit–bath unitary and undoes it afterward. A finite-field schedule makes each pair of frames independent. The realized frames remain private. Users can insert adaptive operations in the corrected logical frame, and the bath can retain quantum information throughout the run.

## Results

| Task | Guarantee |
| --- | --- |
| Protect the qubit at all logical interfaces | The explicit schedule uses $`2\lceil\log_4(3n+1)\rceil`$ uniform bits. The worst tester half trace distance from ideal is at most $`\tfrac12(1+e^L)^2 S`$. |
| Determine the necessary randomness | An oblivious sequence of rotations can align with the most probable schedule. Achieving $`O(1/n)`$ error at fixed nonzero total angle requires $`\log_2 n-O(1)`$ bits of min-entropy. |
| Reproduce independent random frames | A $`t`$-wise independent schedule uses $`O(t\log n)`$ bits and approximates the independent-frame process with a factorial-tail error bound. Exact reproduction can require $`4^n`$ deterministic schedules. |

Here $`S=\sum_j\beta_j^2`$ and $`L=\sqrt3\sum_j\beta_j`$, where $`\beta_j`$ is the root-sum-square operator norm of the three nonidentity Pauli coefficients of the joint unitary in slot $`j`$. If the sum of the slot strengths is bounded and the largest strength is $`O(1/n)`$, then $`S=O(1/n)`$.

In a [five-slot calculation](verification/README.md), four uniform seed bits give an output trace distance of **0.04180** from ideal for one specified tester with a retained bath. Ten bits for independent frames give **0.04182** in that example. It illustrates the finite comparison for that tester.

## Read the science

The [scientific account](science/README.md) starts with the control mechanism and connects the proofs to the physical resources.

| Question | Account |
| --- | --- |
| What does a run supply and what can the tester do? | [Model and resources](science/model.md) |
| How do the seed bits generate all the Pauli frames? | [Finite-field construction](science/seed.md) |
| Why does pairwise independence control the whole process? | [Complete process-error bound](science/process-bound.md) |
| Why are logarithmically many bits necessary? | [Seed-entropy converse](science/converse.md) |
| How closely can a short seed reproduce independent controls? | [Independent-frame simulation](science/independent-process.md) |
| How much imperfect control or seed leakage can the guarantee tolerate? | [Control robustness](science/control-robustness.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) |
| How can I check the finite examples? | [Verification](verification/README.md) |

The main theorem assumes ideal frame operations and joint slot unitaries fixed independently of the seed. A comparison on the full retained memory quantifies how imperfect dressed slots and initial seed leakage affect the error.

## Learn the project

The [learning route](learning/README.md) uses John Watrous’s *The Theory of Quantum Information* to connect channels, dilation and distinguishability to the [30 milestones](learning/MILESTONES.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
