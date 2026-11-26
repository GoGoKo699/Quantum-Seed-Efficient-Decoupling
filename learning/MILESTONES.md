# Project understanding map

The first twelve milestones build the memory experiment from registers, slot interactions, and classical randomness. The following eighteen develop the compiler, the tester-level guarantee, and the lower bound, then compare the construction with independent frames and imperfect controls. This allocation gives the proof and its operational consequences space to develop from their constituent steps.

The [Watrous bridge](WATROUS_BRIDGE.md) supplies the relevant textbook sections. The linked science pages contain the precise statements and proofs.

## Phase I · Background and preliminaries

### M01 Data, bath, and reference

**Central question.** Which registers can carry information about the input through a memory experiment?

**Understanding target.** Identify the data qubit, an inaccessible bath, and the tester's accessible reference as distinct tensor factors. Trace which registers the slot and tester operations can affect directly.

**Prerequisites and connection.** None. These tensor factors specify the physical accessibility used throughout the model. [Registers and partial trace](WATROUS_BRIDGE.md#targeted-reading) · [Memory model](../science/model.md)

### M02 A bath that persists between slots

**Central question.** How can an interaction in one slot affect the data qubit in a later slot?

**Understanding target.** Explain how a previously independent bath becomes correlated with the data and carries correlations into the next interaction. Identify the joint state one must propagate from slot to slot.

**Prerequisites and connection.** [M01](#m01-data-bath-and-reference). The causal experiment retains the bath across the interfaces and reduces it away at the output. [Watrous bridge](WATROUS_BRIDGE.md#targeted-reading) · [Memory model](../science/model.md)

### M03 Coherent representation of a tester

**Central question.** How can one describe a tester that records an outcome and uses it later?

**Understanding target.** Represent each operation by an isometry with retained auxiliary registers. Explain how a later operation can depend on a retained record through a fixed controlled isometry.

**Prerequisites and connection.** [M01](#m01-data-bath-and-reference), [M02](#m02-a-bath-that-persists-between-slots). This representation lets the proof expand a vector while retaining the tester's ability to adapt. [Stinespring representations](WATROUS_BRIDGE.md#targeted-reading) · [Process bound](../science/process-bound.md)

### M04 Operational distance at the output

**Central question.** What measurement difference does a trace-distance estimate certify?

**Understanding target.** Interpret half the trace norm as the greatest difference in a binary outcome probability for two normalized states. Recognize which supremum over testers turns that state comparison into a process comparison.

**Prerequisites and connection.** [M02](#m02-a-bath-that-persists-between-slots), [M03](#m03-coherent-representation-of-a-tester). A uniform output bound certifies both passive final readouts and interventions between logical slots. [State and channel distance](WATROUS_BRIDGE.md#targeted-reading) · [Memory model](../science/model.md)

### M05 The Pauli basis with operator coefficients

**Central question.** What is a Pauli coefficient when a qubit operator also acts on the bath?

**Understanding target.** Use the orthogonality relation $`\operatorname{Tr}(\sigma_p\sigma_q)=2\delta_{pq}`$ to see why each coefficient is an operator on the bath and why its extraction includes a factor of $`1/2`$.

**Prerequisites and connection.** [M01](#m01-data-bath-and-reference). This expansion identifies which terms can act on the bath alone and which carry a nontrivial data Pauli. [Operator basis](WATROUS_BRIDGE.md#conventions) · [Memory model](../science/model.md)

### M06 Conjugation signs

**Central question.** What changes when a Pauli frame is applied around an interaction?

**Understanding target.** Predict the sign of each nonidentity Pauli term from commutation or anticommutation. Explain why Pauli phases leave conjugation unchanged and why the identity term keeps a positive sign.

**Prerequisites and connection.** [M05](#m05-the-pauli-basis-with-operator-coefficients). The controller changes the signs of fixed bath coefficients by operations on the data qubit. [One Pauli average](WATROUS_BRIDGE.md#from-one-pauli-average-to-a-causal-process) · [Seed construction](../science/seed.md)

### M07 Independence of pairs of slots

**Central question.** What does pairwise independence specify about a whole schedule?

**Understanding target.** Interpret pairwise independence as uniform joint draws for any two distinct slots. Recognize that several slots can obey exact relations even when each pair is independent.

**Prerequisites and connection.** [M06](#m06-conjugation-signs). This is the statistical promise that permits far fewer random bits than sampling every slot independently. [Seed construction](../science/seed.md)

### M08 Character tags and seed averages

**Central question.** How can one tell which products of signs survive averaging over the seed?

**Understanding target.** Assign the signs to real additive characters of the finite seed space. Explain why multiplying the characters adds their tags and why the average is supported at total tag zero.

**Prerequisites and connection.** [M06](#m06-conjugation-signs), [M07](#m07-independence-of-pairs-of-slots). This converts averages over a shared seed into algebraic constraints on error histories. [Seed construction](../science/seed.md)

### M09 A normalized slot coefficient budget

**Central question.** How does unitarity constrain the amount of data-dependent interaction in a slot?

**Understanding target.** Derive the coefficient identity after tracing the data factor out of $`U_t^\dagger U_t`$. Use it to bound the loss of squared norm of the identity coefficient on any incoming bath vector.

**Prerequisites and connection.** [M02](#m02-a-bath-that-persists-between-slots), [M05](#m05-the-pauli-basis-with-operator-coefficients). This supplies a deterministic estimate that remains valid as the bath changes state. [Memory model](../science/model.md) · [Process bound](../science/process-bound.md)

### M10 Total and squared slot strengths

**Central question.** Why does splitting a fixed total interaction into weaker pieces change the certified error?

**Understanding target.** Interpret $`A=\sum_t\beta_t`$ and $`S=\sum_t\beta_t^2`$ as different measures of the interaction profile. Predict their behavior for comparably weak slots and for a profile concentrated in one slot.

**Prerequisites and connection.** [M09](#m09-a-normalized-slot-coefficient-budget). The finite bound keeps track of the total interaction in a prefactor and the squared strengths in the error scale. [Memory model](../science/model.md) · [Process bound](../science/process-bound.md)

### M11 Seed entropy and schedule probability

**Central question.** Which feature of a schedule distribution governs the cost of its most exposed branch?

**Understanding target.** Relate min-entropy to the probability of the most likely schedule. Explain why a deterministic generator fed $`b`$ fair bits can have schedule min-entropy at most $`b`$, even if different seeds give the same schedule.

**Prerequisites and connection.** [M07](#m07-independence-of-pairs-of-slots). The distribution of physical schedules is the object constrained by the converse. [Seed construction](../science/seed.md) · [Entropy converse](../science/converse.md)

### M12 The complete memory experiment

**Central question.** What must a low-randomness controller get right across all the slots?

**Understanding target.** State the initial independence, fixed joint slots, private seed, ideal qubit controls, logical boundary access, and worst-case tester comparison in one experiment. Trace how the seed, pulses, and tester are charged or supplied.

**Prerequisites and connection.** [M03](#m03-coherent-representation-of-a-tester), [M04](#m04-operational-distance-at-the-output), [M08](#m08-character-tags-and-seed-averages), [M10](#m10-total-and-squared-slot-strengths), [M11](#m11-seed-entropy-and-schedule-probability). The resulting task defines both sides of the seed comparison. [Memory model](../science/model.md)

## Phase II · Narrative and innovation

### M13 Projective directions for temporal slots

**Central question.** How can a short uniform seed generate any desired number of pairwise-independent Pauli labels?

**Understanding target.** Choose one representative from each selected one-dimensional direction in $`\mathbb F_4^m`$ and form its dot product with the uniform seed. Use linear independence of two representatives to explain joint uniformity.

**Prerequisites and connection.** [M07](#m07-independence-of-pairs-of-slots), [M08](#m08-character-tags-and-seed-averages). Counting directions gives the explicit budget $`2\lceil\log_4(3n+1)\rceil`$ bits. [Seed construction](../science/seed.md)

### M14 Character collisions and their absence

**Central question.** Why does every slot contribute exactly three sign tags that are unique across all slots?

**Understanding target.** Identify the three nonzero scalar multiples of each direction as the tags for the corresponding Pauli signs. Connect the choice of distinct directions to orthogonality of the resulting functions of the seed.

**Prerequisites and connection.** [M06](#m06-conjugation-signs), [M08](#m08-character-tags-and-seed-averages), [M13](#m13-projective-directions-for-temporal-slots). The proof will use uniqueness after adding a common tag to multiple histories. [Seed construction](../science/seed.md) · [Process bound](../science/process-bound.md)

### M15 Corrected logical ports

**Central question.** Where does the protocol put the Pauli gates when a tester can intervene?

**Understanding target.** Explain how the before-slot frame and after-slot inverse expose the logical qubit at every boundary. Count the two conjugation gates per slot in the interactive model and identify when adjacent gates can be combined in a passive run.

**Prerequisites and connection.** [M06](#m06-conjugation-signs), [M12](#m12-the-complete-memory-experiment), [M13](#m13-projective-directions-for-temporal-slots). This implements the sampled schedule with an exact ideal logical operation when the slots are bath-only. [Memory model](../science/model.md) · [Seed construction](../science/seed.md)

### M16 The all-identity history

**Central question.** What output does the history with every data Pauli equal to identity produce?

**Understanding target.** Factor it into the ideal tester vector and an unnormalized bath vector. Explain why the bound on each slot's norm loss adds along this history.

**Prerequisites and connection.** [M03](#m03-coherent-representation-of-a-tester), [M09](#m09-a-normalized-slot-coefficient-budget), [M15](#m15-corrected-logical-ports). This gives the ideal output times a scalar survival weight after tracing out the bath. [Process bound](../science/process-bound.md)

### M17 Organizing nonidentity histories by degree

**Central question.** How can one count many possible error histories while preserving the order of bath interactions?

**Understanding target.** Label a history by increasing slot positions and a Pauli choice at each selected slot. Interpret the ordered sums of products of slot strengths and the factorial from summing over distinct positions.

**Prerequisites and connection.** [M10](#m10-total-and-squared-slot-strengths), [M14](#m14-character-collisions-and-their-absence), [M16](#m16-the-all-identity-history). Grouping histories by degree controls the combinatorial sum while preserving noncommuting operator order. [Process bound](../science/process-bound.md)

### M18 The squared amplitude bound

**Central question.** Where does an orthogonal sum replace a coherent sum in the bound on nonidentity histories?

**Understanding target.** Hold the prefix of a degree-fixed history constant and vary its last slot and label. Explain why the shifted character tags stay distinct and why the squared norm then uses a sum of squared slot strengths.

**Prerequisites and connection.** [M14](#m14-character-collisions-and-their-absence), [M17](#m17-organizing-nonidentity-histories-by-degree). The root-mean-square norm gains a factor of $`\sqrt S`$ even when higher-degree histories have dependencies. [Process bound](../science/process-bound.md)

### M19 Controlling the mean amplitude

**Central question.** Why are the surviving higher-degree mean terms also of order $`S`$?

**Understanding target.** Fix the middle events and identify the matching constraint on the first and last tags. Use uniqueness and Cauchy–Schwarz to explain the squared-strength bound. Account separately for the vanishing degree-one contribution.

**Prerequisites and connection.** [M14](#m14-character-collisions-and-their-absence), [M17](#m17-organizing-nonidentity-histories-by-degree). This controls the interference between the ideal history and all nonidentity histories in the averaged output. [Process bound](../science/process-bound.md)

### M20 From amplitudes to an averaged state

**Central question.** Which pieces of the averaged density operator need separate estimates?

**Understanding target.** Identify the all-identity projector, its cross terms with the mean deviation, and the positive mean projector of the deviation. Explain how their trace norms are estimated by the three preceding bounds.

**Prerequisites and connection.** [M16](#m16-the-all-identity-history), [M18](#m18-the-squared-amplitude-bound), [M19](#m19-controlling-the-mean-amplitude). This joins the vector estimates into one physical state comparison. [Process bound](../science/process-bound.md)

### M21 A finite bound for every corrected-port tester

**Central question.** Why does the same error bound hold when the tester stores quantum side information and intervenes?

**Understanding target.** Locate where the proof uses the norm-preserving tester isometries and the independence of those isometries from the hidden seed. Explain why tracing out the bath and unused records preserves the bound.

**Prerequisites and connection.** [M03](#m03-coherent-representation-of-a-tester), [M04](#m04-operational-distance-at-the-output), [M15](#m15-corrected-logical-ports), [M20](#m20-from-amplitudes-to-an-averaged-state). Taking the supremum produces the finite causal-process guarantee. [Memory model](../science/model.md) · [Process bound](../science/process-bound.md)

### M22 The fixed-total-strength regime

**Central question.** In what regime does the upper bound predict inverse-slot error with logarithmic seed cost?

**Understanding target.** Use bounded $`A`$ and comparable slot strengths of order $`1/n`$ to get $`S=O(1/n)`$. Compare the seed length with the $`2n`$ uniform bits consumed by independent Pauli frames.

**Prerequisites and connection.** [M10](#m10-total-and-squared-slot-strengths), [M13](#m13-projective-directions-for-temporal-slots), [M21](#m21-a-finite-bound-for-every-corrected-port-tester). This identifies the controlled scaling limit and the chosen comparison budget. [Seed construction](../science/seed.md) · [Process bound](../science/process-bound.md)

### M23 A Bell witness against the heaviest schedule

**Central question.** How can fixed slot rotations expose a schedule the controller selects privately?

**Understanding target.** Choose rotation axes against the most likely complete frame schedule before the run. Follow how that schedule aligns equal weak rotations into one coherent angle and raises the Bell-test failure probability.

**Prerequisites and connection.** [M04](#m04-operational-distance-at-the-output), [M06](#m06-conjugation-signs), [M11](#m11-seed-entropy-and-schedule-probability), [M15](#m15-corrected-logical-ports). A bath-free idle tester suffices to lower-bound the worst-case process error. [Entropy converse](../science/converse.md)

### M24 Matching order of seed entropy

**Central question.** How does a single heavy branch establish the asymptotic randomness requirement?

**Understanding target.** Convert the weighted Bell-failure probability into a bound on $`p_{\max}`$, and hence on min-entropy, for a uniform worst-case $`O(1/n)`$ guarantee at fixed nonzero angle. Compare this bound with the compiler's bit count.

**Prerequisites and connection.** [M11](#m11-seed-entropy-and-schedule-probability), [M22](#m22-the-fixed-total-strength-regime), [M23](#m23-a-bell-witness-against-the-heaviest-schedule). The scheduler and the witness establish the same logarithmic order within the randomized unitary-frame model. [Seed construction](../science/seed.md) · [Entropy converse](../science/converse.md)

### M25 Approximating independently sampled frames

**Central question.** What extra guarantee does raising the independence order buy?

**Understanding target.** Explain why a density contribution of total degree up to the independence order has the same average under both schedules. Connect the unmatched degrees to a factorial tail and the increased seed length.

**Prerequisites and connection.** [M07](#m07-independence-of-pairs-of-slots), [M17](#m17-organizing-nonidentity-histories-by-degree), [M20](#m20-from-amplitudes-to-an-averaged-state), [M22](#m22-the-fixed-total-strength-regime). This compares two controlled processes directly. [Independent-process comparison](../science/independent-process.md)

### M26 Exact matching and full process rank

**Central question.** Why can reproducing independent frames exactly require many more schedules?

**Understanding target.** Follow a tester that inserts a fresh half Bell pair at every port and collects the outputs. Explain how full rank gives a lower bound on the number of pure deterministic histories in an exact ensemble.

**Prerequisites and connection.** [M03](#m03-coherent-representation-of-a-tester), [M23](#m23-a-bell-witness-against-the-heaviest-schedule), [M25](#m25-approximating-independently-sampled-frames). Exact reproduction is a separate resource requirement from bounded process error. [Independent-process comparison](../science/independent-process.md)

### M27 Imperfect control slots

**Central question.** What accuracy of the implemented controls preserves the bound at the scale of the target error?

**Understanding target.** Follow the hybrid comparison that replaces one implemented slot at a time. Translate a total perturbation budget into the additional process distance and compare it with the decoupling term.

**Prerequisites and connection.** [M04](#m04-operational-distance-at-the-output), [M15](#m15-corrected-logical-ports), [M21](#m21-a-finite-bound-for-every-corrected-port-tester). The estimate gives a concrete way to assess a specified implementation perturbation. [Control robustness](../science/control-robustness.md)

### M28 What a finite simulation checks

**Central question.** Which parts of the theorem can a small retained-bath example validate directly?

**Understanding target.** Identify the schedule checks, construction of the averaged accessible state, and computation of its distance for a chosen tester. Explain how changing to an independent schedule supplies a controlled comparison for that same instance.

**Prerequisites and connection.** [M14](#m14-character-collisions-and-their-absence), [M21](#m21-a-finite-bound-for-every-corrected-port-tester), [M25](#m25-approximating-independently-sampled-frames). Finite computations probe the algebra and operation order of explicit cases, while the tester supremum is controlled analytically. [Verification](../verification/README.md) · [Process bound](../science/process-bound.md)

### M29 A private average in the presence of memory

**Central question.** Which operational assumptions determine the interpretation of the seed savings?

**Understanding target.** Explain how using earlier tester outcomes differs from direct access to the seed, and how the proof charges initial seed–bath correlation once. Explain what the fixed-total-strength guarantee certifies about the accessible output even when individual fault events are correlated.

**Prerequisites and connection.** [M12](#m12-the-complete-memory-experiment), [M21](#m21-a-finite-bound-for-every-corrected-port-tester), [M25](#m25-approximating-independently-sampled-frames), [M27](#m27-imperfect-control-slots). These assumptions identify the experiments and noise comparisons supported by the result. [Memory model](../science/model.md) · [Control robustness](../science/control-robustness.md)

### M30 The complete seed and error tradeoff

**Central question.** What resources suffice to protect a qubit across a finite retained-bath process, and which of those resources does the converse certify?

**Understanding target.** Reconstruct the chain from private seed to pairwise-independent frames, corrected logical slots, and the tester-level error. State the matched logarithmic seed order and the assumptions needed for that comparison. Place independent-process approximation and control perturbations in the same resource account.

**Prerequisites and connection.** [M21](#m21-a-finite-bound-for-every-corrected-port-tester), [M24](#m24-matching-order-of-seed-entropy), [M26](#m26-exact-matching-and-full-process-rank), [M27](#m27-imperfect-control-slots), [M28](#m28-what-a-finite-simulation-checks), [M29](#m29-a-private-average-in-the-presence-of-memory). This completes the account of what the controller implements and why its randomness order is necessary. [Memory model](../science/model.md) · [Process bound](../science/process-bound.md) · [Entropy converse](../science/converse.md)

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md)
