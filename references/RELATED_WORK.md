# Related work

## Random decoupling and correlated noise

Viola and Knill established the quadratic short-slot error-probability law for randomized dynamical decoupling. Their Theorems 1 and 2 give a bound of order $`T\Delta t\,k^2`$ in the small-error regime for their final-state criterion, including a retained environment in Theorem 2 with the corresponding interaction bound. They use uniformly distributed controls under a temporal independence condition. Here the protected object is the entire corrected-port process, compared through all allowed adaptive testers. The project constructs a finite short-seed schedule and proves that logarithmically many bits are necessary under this operational requirement. [Phys. Rev. Lett. 94, 060502 (2005)](https://doi.org/10.1103/PhysRevLett.94.060502) · [arXiv text](https://arxiv.org/html/quant-ph/0511120v1)

Wallman and Emerson use freshly sampled twirling and correction gates in randomized compiling. Theorem 1 tailors errors into stochastic Pauli noise under its gate-independence assumption. Theorem 2 bounds the change from gate-dependent easy-gate noise in diamond norm. The [control robustness estimate](../science/control-robustness.md) uses the same basic channel replacement argument on the joint data and memory space, so it applies to interventions by an adaptive tester. [Phys. Rev. A 94, 052325 (2016)](https://doi.org/10.1103/PhysRevA.94.052325)

Winick et al. extend stochastic-Pauli tailoring to retained environments. Their Theorem 3 assumes independent twirl choices in each round and gate-independent easy-gate errors. Their local stochastic description gives more information about the error structure than a distance to the ideal process. Section III.3 explains how revealing a twirl parity to the environment can restore coherent accumulation. The present [leakage example](../science/control-robustness.md#a-fixed-joint-unitary-can-exploit-a-leaked-seed) quantifies probabilistic exposure of the initial seed in trace distance. The correlated schedules here certify an ideal-process approximation in the bounded-strength regime and can approximate the independent process with [higher independence](../science/independent-process.md). [arXiv:2212.07500 (2022)](https://arxiv.org/abs/2212.07500)

## Short schedules and hardware

Rötteler and Wocjan connect orthogonal arrays and classical codes to dynamical decoupling for spatially local interactions. The orthogonal-array construction used here is standard. Its columns specify temporal slots and one uniformly sampled word specifies a run. The [seed converse](../science/converse.md) applies to general finite ensembles of unitary-frame schedules and does not assume those ensembles form an orthogonal array. [IEEE Trans. Inf. Theory 52, 4171–4181 (2006)](https://doi.org/10.1109/TIT.2006.880059)

Fruitwala et al. use an FPGA linear-feedback shift register to select twirling gates on the fly. Their QubiC implementation addresses classical compilation, circuit upload and execution overhead. Here the resource is the number of independent uniform seed bits per run for a specified worst-case process guarantee. Hardware timing, device-specific performance and fault-tolerance implications require separate analysis. [arXiv:2406.13967 (2024)](https://arxiv.org/abs/2406.13967)

## Interactive distance

The adaptive tester comparison uses the established operational viewpoint of quantum combs and quantum strategies. The repository specifies the allowed port access and writes its distance directly as the supremum of half trace distance over final tester states. [Chiribella, D’Ariano and Perinotti, Phys. Rev. A 80, 022339 (2009)](https://doi.org/10.1103/PhysRevA.80.022339) · [Gutoski, J. Math. Phys. 53, 032202 (2012)](https://doi.org/10.1063/1.3693621)

[BibTeX bibliography](references.bib)
