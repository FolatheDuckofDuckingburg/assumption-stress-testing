# Assumption Stress Testing (AST)
### A Computational Framework for Evaluating Assumptions in the Foundations of Physics

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--2148--5675-green.svg)](https://orcid.org/0009-0007-2148-5675)

**Assumption Stress Testing (AST)** is an independent computational research project concerned with the systematic examination of assumptions underlying theoretical models, particularly in the foundations of physics.

The framework is motivated by a methodological question:

> What happens when the assumptions underlying a theoretical model are made explicit, examined individually, and tested for the consequences they impose on the model?

AST aims to provide a structured approach to identifying assumptions, tracing their mathematical implications, evaluating internal consistency, and distinguishing theoretical plausibility from empirical support.

The project currently contains exploratory computational experiments. It does not establish a new physical theory or demonstrate that existing theories are invalid.

## Research objectives

AST is organized around several methodological objectives:

- **Assumption identification:** Make the foundational assumptions of a model explicit rather than treating them as implicit necessities.
- **Consequence analysis:** Examine the mathematical and logical consequences that follow from those assumptions.
- **Consistency evaluation:** Distinguish internal mathematical consistency from agreement with physical observations.
- **Robustness examination:** Investigate how model behaviour changes when assumptions, parameters, or constraints are varied.
- **Empirical accountability:** Identify what evidence would be required to support, constrain, or reject a proposed model.

These objectives are methodological. Their usefulness and originality must be evaluated through implementation, comparison with existing methods, and reproducible research.

## Methodological principles

AST follows several principles when evaluating theoretical claims.

### 1. Prediction is not the same as fundamentality

A theory's successful predictions provide important empirical support within the regimes in which it has been tested. However, predictive success alone does not establish that every assumption of the theory is fundamental or that the theory represents a final description of physical reality.

### 2. Incompleteness is not falsification

A theory may have unresolved questions or limitations without being invalid within its established domain of applicability.

### 3. Mathematical consistency is not empirical confirmation

A mathematically consistent model is not necessarily a physically accurate one. Mathematical derivation, empirical evidence, and physical interpretation must be evaluated separately.

### 4. Successor models carry a correspondence requirement

Any proposed alternative or extension must account for established experimental results and recover the successful predictions of existing theories in the regimes where those predictions have been verified.

These principles are not arguments against General Relativity or any other established physical theory. They are standards for evaluating theoretical proposals, including speculative ones.

## Current computational experiment

### Synthetic graph recovery

The repository currently includes an exploratory benchmark implemented in:

`ast_metric_induction.py`

The experiment investigates whether a known synthetic correlation structure can be recovered using pairwise information-theoretic measurements.

The pipeline proceeds as follows:

1. **Structure generation:** A circular graph structure is specified as the planted reference network.
2. **Covariance construction:** Correlations corresponding to the reference structure are encoded in a Gaussian covariance matrix.
3. **Synthetic sampling:** Observations are generated from the resulting multivariate Gaussian distribution.
4. **Information estimation:** Pairwise mutual information is estimated under a bivariate-Gaussian assumption.
5. **Graph inference:** Each node is connected to the two nodes with the highest estimated mutual-information scores.
6. **Evaluation:** The inferred graph is compared with the planted reference structure using edge precision, recall, and F1 score.

The benchmark provides a controlled setting in which the underlying structure is known, allowing the graph-recovery procedure to be evaluated against a reference.

**Scope limitation:** This experiment demonstrates a synthetic graph-recovery pipeline. It does not demonstrate that spacetime emerges from information, establish a physical metric, or provide empirical evidence for a new theory of gravity.

Further assumptions, implementation details, and limitations are documented in [`docs/MODEL_LIMITATIONS.md`](docs/MODEL_LIMITATIONS.md).

## Installation

Python 3.8 or later is recommended.

Install the required dependencies:

```bash
python -m pip install numpy matplotlib networkx
```

## Usage

Run the experiment with visualization:

```bash
python ast_metric_induction.py
```

Run without generating a plot:

```bash
python ast_metric_induction.py --no-plot --nodes 24 --samples 4000 --seed 42
```

The command-line options allow the synthetic benchmark to be configured, including the number of nodes, sample count, and random seed.

## Testing

Run the repository's unit tests:

```bash
python -m unittest discover -s tests -v
```

The tests are intended to check software behaviour and implementation correctness. Passing unit tests should not be interpreted as validation of a physical hypothesis.

## Research status and limitations

AST is an exploratory research methodology project.

The current implementation is limited to a synthetic computational benchmark. In particular, it does not:

- Establish a new physical theory.
- Demonstrate the emergence of spacetime or a physical metric.
- Challenge or falsify General Relativity.
- Establish empirical validity for an alternative model.
- Demonstrate that the AST methodology is novel relative to existing research.

Potential future work includes:

- Formalizing the AST methodology into a reproducible evaluation protocol.
- Reviewing existing literature on model criticism, sensitivity analysis, and theoretical foundations.
- Expanding the range of synthetic benchmarks.
- Evaluating alternative graph-recovery and information-estimation methods.
- Investigating how assumptions influence model behaviour under controlled perturbations.
- Developing physical models with explicit, mathematically derived, and empirically testable consequences.

Future extensions should be guided by reproducibility, clear mathematical definitions, appropriate baselines, and transparent reporting of limitations.

## Reproducibility

Computational experiments should make their assumptions, parameters, and evaluation procedures inspectable.

Where applicable, experiments should document:

- Random seeds and simulation parameters.
- Mathematical and statistical assumptions.
- Data-generation procedures.
- Evaluation metrics.
- Known limitations and sources of uncertainty.

Results should be interpreted within the scope of the experiment that produced them.

## License

This project is distributed under the [Apache License 2.0](LICENSE).

## Author

**Folarera Kassim**

[ORCID: 0009-0007-2148-5675](https://orcid.org/0009-0007-2148-5675)

---

*Assumption Stress Testing — making theoretical assumptions explicit, examining their consequences, and evaluating what they actually support.*
