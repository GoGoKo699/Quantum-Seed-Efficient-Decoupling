"""Finite checks for the temporal Pauli schedules and their process bounds."""

from collections import Counter
from itertools import combinations, product
from math import exp, factorial, sin

import numpy as np
from scipy.linalg import expm


PAULIS = np.array(
    [
        [[1, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[0, -1j], [1j, 0]],
        [[1, 0], [0, -1]],
    ],
    dtype=complex,
)
IDENTITY = PAULIS[0]
BELL = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
FIELD = range(4)
CONJUGATION_SIGNS = np.array(
    [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]],
    dtype=np.int32,
)
TOLERANCE = 1e-12


def gf4_product(left, right):
    """Multiply polynomials represented by bit pairs modulo x² + x + 1."""
    result = 0
    while right:
        if right & 1:
            result ^= left
        left <<= 1
        if left & 4:
            left ^= 7
        right >>= 1
    return result


def short_schedules(slots):
    """Enumerate field seeds and evaluate on distinct projective tags."""
    dimension = 1
    while (4**dimension - 1) // 3 < slots:
        dimension += 1
    representatives = []
    for leading in range(dimension):
        for tail in product(FIELD, repeat=dimension - leading - 1):
            representatives.append((0,) * leading + (1,) + tail)
    tags = np.asarray(representatives[:slots], dtype=int)
    seeds = np.asarray(list(product(FIELD, repeat=dimension)), dtype=int)
    multiplication = np.array(
        [[gf4_product(left, right) for right in FIELD] for left in FIELD]
    )
    return np.bitwise_xor.reduce(
        multiplication[seeds[:, None, :], tags[None, :, :]], axis=2
    )


def check_uniform_marginals(schedules, order):
    expected_multiplicity = len(schedules) // 4**order
    slots = schedules.shape[1]
    for subset in combinations(range(slots), order):
        frequencies = Counter(map(tuple, schedules[:, subset]))
        assert len(frequencies) == 4**order
        assert set(frequencies.values()) == {expected_multiplicity}


def check_projective_design():
    for slots in (1, 2, 5, 6, 21, 22):
        schedules = short_schedules(slots)
        assert len(set(map(tuple, schedules))) == len(schedules)
        characters = CONJUGATION_SIGNS[schedules][:, :, 1:].reshape(
            len(schedules), 3 * slots
        )
        expected_gram = len(schedules) * np.eye(3 * slots, dtype=np.int32)
        assert np.array_equal(characters.sum(axis=0), np.zeros(3 * slots))
        assert np.array_equal(characters.T @ characters, expected_gram)
        check_uniform_marginals(schedules, min(slots, 2))
    print("Projective Pauli designs: exact character Gram and uniform marginals")


def bath_model(slots):
    """Create noncommuting error slots and fixed intervening tester unitaries."""
    unitaries = []
    for slot in range(slots):
        first = PAULIS[1 + slot % 3]
        second = PAULIS[1 + (slot + 1) % 3]
        third = PAULIS[1 + (slot + 2) % 3]
        hamiltonian = (
            0.46 * np.kron(first, second)
            + 0.21 * np.kron(second, third)
            + 0.37 * np.kron(IDENTITY, first)
        )
        unitaries.append(expm(1j * hamiltonian / slots))

    testers = [
        expm(
            -0.3j
            * np.kron(PAULIS[1 + slot % 3], PAULIS[1 + (slot + 1) % 3])
        )
        for slot in range(slots - 1)
    ]
    return unitaries, testers


def process_parameters(unitaries):
    betas = []
    for unitary in unitaries:
        system_bath = unitary.reshape(2, 2, 2, 2)
        coefficients = [
            np.einsum("ji,iajb->ab", pauli, system_bath) / 2 for pauli in PAULIS
        ]
        normalizer = sum(coefficient.conj().T @ coefficient for coefficient in coefficients)
        reconstructed = sum(
            np.kron(pauli, coefficient)
            for pauli, coefficient in zip(PAULIS, coefficients, strict=True)
        )
        assert np.allclose(normalizer, IDENTITY, atol=TOLERANCE)
        assert np.allclose(reconstructed, unitary, atol=TOLERANCE)
        betas.append(np.linalg.norm([np.linalg.norm(block, 2) for block in coefficients[1:]]))
    return sum(beta**2 for beta in betas), np.sqrt(3) * sum(betas)


def tester_outputs(unitaries, testers):
    """Construct the map from one frame schedule to the tester output."""
    frames = [np.kron(pauli, IDENTITY) for pauli in PAULIS]
    dressed = [
        [np.kron(IDENTITY, frame @ unitary @ frame) for frame in frames]
        for unitary in unitaries
    ]
    tester_steps = [np.kron(step, IDENTITY) for step in testers]
    initial = np.kron(BELL, [1, 0])

    def output(schedule=None):
        vector = initial
        for slot in range(len(unitaries)):
            if schedule is not None:
                vector = dressed[slot][schedule[slot]] @ vector
            if slot < len(tester_steps):
                vector = tester_steps[slot] @ vector
        vector = vector.reshape(4, 2)
        return vector @ vector.conj().T

    return output


def average_output(output, schedules):
    return sum(map(output, schedules)) / len(schedules)


def trace_distance(left, right):
    return float(np.abs(np.linalg.eigvalsh(left - right)).sum() / 2)


def check_bath_process():
    slots = 5
    short = short_schedules(slots)
    independent = list(product(FIELD, repeat=slots))
    unitaries, testers = bath_model(slots)
    assert not np.allclose(unitaries[0] @ unitaries[1], unitaries[1] @ unitaries[0])
    output = tester_outputs(unitaries, testers)
    seeded_state = average_output(output, short)
    independent_state = average_output(output, independent)
    ideal = output()
    seeded_error = trace_distance(seeded_state, ideal)
    independent_error = trace_distance(independent_state, ideal)
    seeded_difference = trace_distance(seeded_state, independent_state)
    deterministic_error = trace_distance(output((0,) * slots), ideal)
    squared_budget, total_budget = process_parameters(unitaries)
    process_bound = (1 + exp(total_budget)) ** 2 * squared_budget / 2
    assert abs(np.trace(seeded_state) - 1) < TOLERANCE
    assert seeded_error <= process_bound + TOLERANCE
    assert seeded_error < deterministic_error
    np.testing.assert_allclose(
        [seeded_error, independent_error, seeded_difference, deterministic_error],
        [0.041799475, 0.041822748, 0.003305085, 0.258973808],
        atol=5e-9,
        rtol=0,
    )
    print(f"Bath tester, {slots} slots: {len(short)} seeded / {len(independent)} independent schedules")
    print(f"  Trace distance to ideal: seeded {seeded_error:.9f}, independent {independent_error:.9f}")
    print(f"  Seeded versus independent: {seeded_difference:.9f}")
    print(f"  Deterministic error: {deterministic_error:.9f}, seeded bound: {process_bound:.9f}")


def check_aligned_branch():
    slots = 5
    schedules = short_schedules(slots)
    angle = 0.6
    signs = CONJUGATION_SIGNS[schedules, 3]
    aligned_angles = (angle / slots) * (signs @ signs[0])
    mixture_failure = float(np.mean(np.sin(aligned_angles)**2))
    weighted_branch_failure = sin(angle)**2 / len(schedules)
    assert np.isclose(aligned_angles[0], angle, rtol=0, atol=TOLERANCE)
    assert weighted_branch_failure <= mixture_failure + TOLERANCE
    print(f"Aligned branch failure: {weighted_branch_failure:.9f}; mixture failure: {mixture_failure:.9f}")


def polynomial_schedules(order):
    """Evaluate every short polynomial on the four distinct GF(4) points."""
    values = []
    for coefficients in product(FIELD, repeat=order):
        row = []
        for point in FIELD:
            value = 0
            for coefficient in coefficients:
                value = gf4_product(value, point) ^ coefficient
            row.append(value)
        values.append(row)
    return np.array(values)


def check_independent_process_approximation():
    slots = 4
    unitaries, testers = bath_model(slots)
    output = tester_outputs(unitaries, testers)
    independent = average_output(output, list(product(FIELD, repeat=slots)))
    squared_budget, total_budget = process_parameters(unitaries)
    for order in (2, 3, 4):
        schedules = polynomial_schedules(order)
        check_uniform_marginals(schedules, order)
        correlated = average_output(output, schedules)
        distance = trace_distance(correlated, independent)
        tail = sum((2 * total_budget) ** k / factorial(k) for k in range(order - 1, 40))
        bound = 2 * squared_budget * tail
        assert distance <= bound + TOLERANCE
        if order == slots:
            assert distance < TOLERANCE
        print(f"{order}-wise tester: distance {distance:.9f}, bound {bound:.9f}")


def check_exact_independent_rank():
    slots = 3
    error = expm(0.2j * (PAULIS[1] + PAULIS[2] + PAULIS[3]))
    dressed_bell = [
        np.kron(IDENTITY, pauli @ error @ pauli) @ BELL for pauli in PAULIS
    ]
    single_slot = np.column_stack(dressed_bell)
    assert np.linalg.matrix_rank(single_slot) == 4
    independent = np.kron(np.kron(single_slot, single_slot), single_slot)
    short = short_schedules(slots)
    branch_indices = np.ravel_multi_index(short.T, (4,) * slots)
    seeded = independent[:, branch_indices]
    assert np.linalg.matrix_rank(independent) == 4**slots
    assert np.linalg.matrix_rank(seeded) == len(short)
    print(f"Exact matching tester: independent rank {4**slots}, seeded rank {len(short)}")


if __name__ == "__main__":
    check_projective_design()
    check_bath_process()
    check_aligned_branch()
    check_independent_process_approximation()
    check_exact_independent_rank()
    print("All finite checks passed.")
