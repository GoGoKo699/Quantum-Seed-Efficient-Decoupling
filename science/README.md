# Protecting a qubit with one short seed

One deterministic frame schedule can leave a coherent rotation that grows over all slots. A controller can randomize the Pauli frames and make the process error depend on the sum of squared slot strengths. The question here is how much of that randomization a controller needs when it keeps the same bath throughout the run.

The construction chooses a row of a finite-field array once and reads one Pauli label per slot. Each possible nonidentity Pauli coefficient then carries a distinct sign character. Orthogonality controls a sum of amplitudes when their last positions vary. In the mean amplitude, fixing the middle positions separates the first and last errors into two segments. Cauchy–Schwarz bounds their contribution using the same orthogonality. These two estimates control the interference and population terms of the final tester state.

The seed saving concerns the number of private random bits drawn per run. The number of physical frame operations still grows with the number of slots. The adaptive tester interface uses two ideal Pauli operations per slot to present a corrected qubit at each port. In the idle-memory implementation, adjacent frame updates can be combined. Subdivision trades more control operations for smaller slot strengths when the total interaction is fixed. The implementation analysis quantifies how residual slot errors or correlations between seed and bath can limit that trade.

1. Read the [model](model.md) for the exact control and tester interfaces.
2. Follow the [seed construction](seed.md) and [process proof](process-bound.md) for the attaining protocol.
3. Compare the [entropy converse](converse.md) with the [independent-frame comparison](independent-process.md). They concern two distinct operational tasks.
4. Use the [robustness bounds](control-robustness.md) to account for deviations from ideal controls, and the [verification](../verification/README.md) for finite calculations.
