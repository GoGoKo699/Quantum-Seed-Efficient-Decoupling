# Reproduce the finite checks

Use Python 3.12, create a virtual environment, then run these commands from the repository root.

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
```

The script enumerates small schedules and checks the following results.

| Check | What is computed |
| --- | --- |
| [Projective schedules](../science/seed.md) | Every nonidentity frame sign has zero mean, the sign Gram matrix is diagonal, and every pair of frame labels is uniform. The integer calculations cover several changes in seed length. |
| [Retained-bath process](../science/process-bound.md) | A five-slot example retains one bath qubit and applies noncommuting operations to the data qubit and a reference at four intervening ports. The script averages over all 16 seeded schedules and all 1,024 independent schedules. |
| [Seed converse](../science/converse.md) | An aligned sequence of equal-angle rotations gives a Bell-state failure probability of at least the aligned branch's failure times its weight. |
| [Independent-process approximation](../science/independent-process.md) | Polynomials over four field points give two-, three-, and four-wise independent schedules. The script checks the marginals and evaluates the tester distance to the independent process. A separate three-slot Choi tester verifies the exact rank distinction. |

In the five-slot example, the seeded and independent errors are 0.041799475 and 0.041822748 in half trace distance to the ideal output. The separation between their output states is 0.003305085. The deterministic control schedule has error 0.258973808 in this example. These figures are for the specified finite tester. The analytic sections give the guarantee over all allowed testers.
