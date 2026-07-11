# FedDMC Replication Package

Replication and study of **FedDMC** (Mu et al., IEEE TDSC 2024), done for my
master's thesis at the University of Namur. I re-ran FedDMC and its baseline
defenses against four poisoning attacks on MNIST, and documented every place
where the released code and the paper disagree. Everything my thesis numbers
are built on is in this repository: the code, the raw logs of every run, and
a generated summary of all results.

- Original method and code: [MuXutong/FedDMC](https://github.com/MuXutong/FedDMC)
  (see [NOTICE](NOTICE) for attribution and licensing).
- Paper: Mu et al., *FedDMC: Efficient and Robust Federated Learning via
  Detecting Malicious Clients*, IEEE Transactions on Dependable and Secure
  Computing, 2024
  ([IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10458320)).

## What is in here

| File / folder | Role |
|---|---|
| `main.py` | Entry point: the round loop, attacker selection, defense dispatch, logging. |
| `clients.py` | Client local training, the non-IID data split, and the LF / GS / Scaling attacks. |
| `attack.py` | The LIT attack (crafted in-range backdoor update). |
| `aggregation.py` | The defenses: FedDMC variants, Multi-Krum, Auror, FoolsGold. |
| `getData.py` | Dataset loading (MNIST, and also EMNIST / CIFAR-10, unused here). |
| `my_PCA.py` | PCA wrapper used before clustering. |
| `utils.py` | Backdoor trigger, detection metrics, logging. |
| `model/` | The network (`Mnist_2NN`, a small two-layer model). |
| `requirements.txt` | Pinned dependencies. |
| `Results/results_summary.md` | Every completed run with its final metrics, generated from the logs. Start here if you just want the numbers. |
| `Results/verify_numbers.py` | The script that builds that summary. |
| `Results/Tests.md` | My run journal: the commands I launched and what they printed, in order. |
| `logs/` | The raw logs: one dated folder per run with its config, per-round metrics, and clustering snapshots (machine identifiers redacted). |
| `clustering/`, `log_viewer.py` | Exploration scripts left over from the original repository, not used here. |

## Requirements

- **Python 3.12**.
- Install into a virtual environment:

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

Everything ran on CPU (a GPU was not faster on this small model). One
200-round run takes a few hours, so plan ahead if you want to redo them all.

## Data

MNIST is downloaded automatically on the first run (into `data/`, via
torchvision). The code also supports EMNIST and CIFAR-10, but the thesis stays
on MNIST.

## Running an experiment

```bash
python main.py --dataset mnist --byz_type <attack> --agg_type <defense> \
  --epoch 1 --beta 5 --num_of_clients 100 --num_malicious_client 28 \
  --learning_rate 0.01 --pca_d 10
```

- `--byz_type` picks the attack: `LF_attack`, `GS_attack`, `LIT_attack`,
  `Scaling_attack`, or `no_attack`.
- `--agg_type` picks the defense: `pca_agglomer_a`, `pca_hdbscan_b`,
  `multi_krum`, `auror`, `foolsgold`, or `average` (no defense at all).
- The rest reproduces the thesis setup: 100 clients, 28 malicious, non-IID
  split with Dirichlet beta 5, 200 rounds.

If you only want to check my numbers without running anything for hours, open
[`Results/results_summary.md`](Results/results_summary.md) instead. Every
completed run is in there, and `Results/Tests.md` has the launch commands.

### Careful: two defaults are traps

**The optimizer.** The original repository trains the clients with Adam. The
paper specifies SGD. That single line decides half of the results, and my
thesis is largely about it. In this package the faithful SGD is active
(`main.py`, around line 157) and the Adam line sits commented just under it.
To reproduce the original repository's behaviour, swap the two lines back.

**The defense names.** Only `pca_agglomer_a` is the paper's actual method
(binary-tree clustering with noise removal). The *default* `--agg_type` is
`pca_hdbscan_b`, which is an HDBSCAN approximation, so running the code
without that flag does not evaluate the paper's method. Some other names
quietly fall back to plain averaging, and `FLDetector` is not implemented at
all. Check `aggregation.py` before trusting a name.

## Determinism

The data split (`numpy` seed 123) and the set of 28 malicious clients
(`random` seed 1) are fixed, so every run faces exactly the same conditions.
PyTorch itself is not seeded, so the initial model weights and the batch
shuffling differ from run to run. Expect the same conclusions, not the same
decimals. That is why the
thesis reports some results as small ranges.

## Deviations from the paper

The ones that matter, documented in full in the thesis:

- **Optimizer:** the original repository defaults to Adam, the paper specifies
  SGD. This package has SGD active.
- **Precision / recall** were swapped in the detection-metrics function
  (fixed here).
- **Default variant:** the dispatched `agg_type` is the HDBSCAN variant, not
  the paper's binary-tree method.
- **Data split:** the original code defaulted to the IID split, and its
  `--IID` flag was broken (any value gave True). The paper evaluates non-IID.
  Fixed here, the default is now the non-IID split.
- **Missing pieces:** `FLDetector` (a baseline) and the Adaptive attack are
  not implemented and fall back or are absent.

## License and citation

The modifications in this repository are released under the [MIT license](LICENSE).
The original FedDMC code it derives from carries no license of its own (see
[NOTICE](NOTICE)). If you use this package, please cite it (see
[`CITATION.cff`](CITATION.cff)) **and** the original FedDMC paper.
