# CTRL + SHIFT + V To render it

# Results Summary (generated)

One line per complete run (a run that reached round 199) found under `logs/`,
with its final-round metrics. This file is generated from the raw logs by
`verify_numbers.py` and is never edited by hand. To update it after new runs:

    python results/verify_numbers.py

How to read the columns:

- **TACC (%)**: final test accuracy of the global model.
- **ASR (%)**: backdoor success rate. Only the two backdoor attacks (LIT and
  Scaling) have one.
- **DAR**: detection accuracy, the fraction of the 100 clients classified
  correctly. A defense that flags nobody scores 0.72 (the 72 honest clients).
- **Precision / Recall** of the malicious flagging. Logs written before the
  metrics fix of 2026-06-19 stored the two values swapped: those runs are
  marked "yes" in the last column and the values shown are already corrected.
- **Optimizer**: hardcoded in `main.py` and never logged (a documented
  deviation). The column follows the switch timeline: Adam until 2026-06-19,
  SGD from 2026-06-20, except the deliberate Adam comparison runs listed in
  the script.
- **Split**: seven early runs (2026-04-12 and 04-13) were launched with the
  IID split by mistake, before the setup was fixed to the non-IID split
  (Dirichlet, beta 5) the thesis uses. They stay in the list, marked IID.

Runs stopped before round 199 (quick diagnostic runs) are not listed.

## At a glance

One row per attack, defense, optimizer, and data split. Cells show the single
value of a lone run or the low-to-high spread of repeated runs.

| Attack                      | Defense                                            | Optimizer | Split   | Runs | TACC (%)       | ASR (%)        | DAR          |
|-----------------------------|----------------------------------------------------|-----------|---------|------|----------------|----------------|--------------|
| No attack (clean reference) | No defense (plain averaging)                       | SGD       | non-IID | 1    | 91.37          | -              | 1.00         |
|                             |                                                    | Adam      | non-IID | 1    | 97.85          | -              | 1.00         |
| Gaussian Noise attack       | No defense (plain averaging)                       | SGD       | non-IID | 1    | 11.38          | -              | 0.72         |
|                             | FedDMC, binary tree (faithful)                     | SGD       | non-IID | 3    | 91.26 to 91.44 | -              | 1.00         |
|                             |                                                    | Adam      | non-IID | 2    | 98.07 to 98.12 | -              | 1.00         |
|                             | FedDMC, HDBSCAN variant                            | Adam      | IID     | 1    | 98.08          | -              | 1.00         |
|                             | Multi-Krum                                         | SGD       | non-IID | 2    | 90.84 to 91.16 | -              | 1.00         |
|                             | Auror                                              | SGD       | non-IID | 2    | 91.16 to 91.18 | -              | 1.00         |
|                             | FoolsGold                                          | SGD       | non-IID | 2    | 9.65           | -              | 0.22 to 0.27 |
| Label Flipping attack       | No defense (plain averaging)                       | SGD       | non-IID | 3    | 90.74 to 91.10 | -              | 0.72         |
|                             |                                                    | Adam      | non-IID | 1    | 85.08          | -              | 0.72         |
|                             | FedDMC, binary tree (faithful)                     | SGD       | non-IID | 4    | 91.22 to 91.41 | -              | 1.00         |
|                             |                                                    | Adam      | non-IID | 5    | 41.09 to 93.71 | -              | 0.23 to 0.26 |
|                             | FedDMC, HDBSCAN variant                            | Adam      | non-IID | 4    | 94.82 to 97.17 | -              | 0.65 to 0.80 |
|                             | Multi-Krum                                         | SGD       | non-IID | 1    | 90.96          | -              | 1.00         |
|                             | Auror                                              | SGD       | non-IID | 1    | 91.02          | -              | 1.00         |
|                             | FoolsGold                                          | SGD       | non-IID | 1    | 87.63          | -              | 0.26         |
|                             |                                                    | Adam      | IID     | 1    | 42.77          | -              | 0.32         |
| LIT backdoor attack         | No defense (plain averaging)                       | SGD       | non-IID | 1    | 91.40          | 1.02           | 0.72         |
|                             | FedDMC, binary tree (faithful)                     | SGD       | non-IID | 3    | 91.11 to 91.45 | 0.61 to 0.71   | 1.00         |
|                             |                                                    | Adam      | non-IID | 2    | 97.94 to 98.01 | 0.31 to 0.38   | 1.00         |
|                             | FedDMC, HDBSCAN variant                            | Adam      | non-IID | 1    | 97.89          | 0.39           | 0.81         |
|                             | Multi-Krum                                         | SGD       | non-IID | 2    | 91.29 to 91.37 | 1.14 to 1.25   | 0.44         |
|                             |                                                    | Adam      | non-IID | 1    | 97.40          | 82.73          | 0.44         |
|                             |                                                    | Adam      | IID     | 5    | 97.37 to 97.70 | 54.80 to 60.04 | 0.44         |
|                             | Auror                                              | SGD       | non-IID | 2    | 91.26 to 91.48 | 1.00 to 1.03   | 0.61         |
|                             |                                                    | Adam      | non-IID | 1    | 97.83          | 50.51          | 0.71         |
|                             | FoolsGold                                          | SGD       | non-IID | 2    | 91.14 to 91.28 | 0.66 to 0.69   | 0.36 to 0.65 |
|                             |                                                    | Adam      | non-IID | 3    | 96.48 to 97.20 | 19.94 to 60.06 | 0.33 to 0.40 |
|                             | FLDetector (not implemented, runs plain averaging) | Adam      | non-IID | 1    | 97.67          | 49.00          | 0.72         |
| Scaling backdoor attack     | No defense (plain averaging)                       | SGD       | non-IID | 1    | 91.00          | 89.92          | 0.72         |
|                             | FedDMC, binary tree (faithful)                     | SGD       | non-IID | 6    | 91.14 to 91.36 | 0.66 to 0.75   | 1.00         |
|                             |                                                    | Adam      | non-IID | 2    | 98.04 to 98.07 | 90.18 to 90.20 | 0.67 to 0.72 |
|                             | FedDMC, HDBSCAN variant                            | Adam      | non-IID | 4    | 95.98 to 98.29 | 90.20          | 0.72         |
|                             | Multi-Krum                                         | SGD       | non-IID | 3    | 91.21 to 91.48 | 0.67 to 0.73   | 1.00         |
|                             | Auror                                              | SGD       | non-IID | 1    | 91.18          | 0.70           | 1.00         |
|                             | FoolsGold                                          | SGD       | non-IID | 2    | 89.71 to 90.61 | 89.83 to 90.17 | 0.24 to 0.26 |

## All runs, attack by attack

### No attack (clean reference)

| Defense                      | Run                 | Optimizer | Split   | TACC (%) | ASR (%) | DAR  | Precision | Recall | Pre-fix log |
|------------------------------|---------------------|-----------|---------|----------|---------|------|-----------|--------|-------------|
| No defense (plain averaging) | 2026-06-20/12.51.13 | SGD       | non-IID | 91.37    | -       | 1.00 | 1.00      | 0.00   | -           |
|                              | 2026-07-09/19.51.30 | Adam      | non-IID | 97.85    | -       | 1.00 | 1.00      | 0.00   | -           |

### Gaussian Noise attack

| Defense                        | Run                 | Optimizer | Split   | TACC (%) | ASR (%) | DAR  | Precision | Recall | Pre-fix log |
|--------------------------------|---------------------|-----------|---------|----------|---------|------|-----------|--------|-------------|
| No defense (plain averaging)   | 2026-07-06/14.19.14 | SGD       | non-IID | 11.38    | -       | 0.72 | 1.00      | 0.00   | -           |
| FedDMC, binary tree (faithful) | 2026-06-18/22.04.56 | Adam      | non-IID | 98.07    | -       | 1.00 | 1.00      | 1.00   | yes         |
|                                | 2026-06-19/02.45.33 | Adam      | non-IID | 98.12    | -       | 1.00 | 1.00      | 1.00   | yes         |
|                                | 2026-06-21/01.28.01 | SGD       | non-IID | 91.40    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-05/13.58.46 | SGD       | non-IID | 91.44    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/01.30.57 | SGD       | non-IID | 91.26    | -       | 1.00 | 1.00      | 1.00   | -           |
| FedDMC, HDBSCAN variant        | 2026-04-12/01.32.45 | Adam      | IID     | 98.08    | -       | 1.00 | 1.00      | 1.00   | yes         |
| Multi-Krum                     | 2026-07-04/01.36.49 | SGD       | non-IID | 91.16    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/13.42.14 | SGD       | non-IID | 90.84    | -       | 1.00 | 1.00      | 1.00   | -           |
| Auror                          | 2026-07-04/01.37.16 | SGD       | non-IID | 91.18    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/13.42.37 | SGD       | non-IID | 91.16    | -       | 1.00 | 1.00      | 1.00   | -           |
| FoolsGold                      | 2026-07-04/01.37.27 | SGD       | non-IID | 9.65     | -       | 0.22 | 0.20      | 0.57   | -           |
|                                | 2026-07-07/21.37.33 | SGD       | non-IID | 9.65     | -       | 0.27 | 0.21      | 0.57   | -           |

### Label Flipping attack

| Defense                        | Run                 | Optimizer | Split   | TACC (%) | ASR (%) | DAR  | Precision | Recall | Pre-fix log |
|--------------------------------|---------------------|-----------|---------|----------|---------|------|-----------|--------|-------------|
| No defense (plain averaging)   | 2026-06-18/01.23.29 | Adam      | non-IID | 85.08    | -       | 0.72 | 0.00      | 0.00   | yes         |
|                                | 2026-07-06/14.19.13 | SGD       | non-IID | 90.90    | -       | 0.72 | 1.00      | 0.00   | -           |
|                                | 2026-07-08/16.38.39 | SGD       | non-IID | 90.74    | -       | 0.72 | 1.00      | 0.00   | -           |
|                                | 2026-07-08/16.38.57 | SGD       | non-IID | 91.10    | -       | 0.72 | 1.00      | 0.00   | -           |
| FedDMC, binary tree (faithful) | 2026-06-18/14.08.32 | Adam      | non-IID | 41.09    | -       | 0.24 | 0.00      | 0.00   | yes         |
|                                | 2026-06-18/21.59.22 | Adam      | non-IID | 42.51    | -       | 0.25 | 0.00      | 0.00   | yes         |
|                                | 2026-06-18/21.59.23 | Adam      | non-IID | 45.79    | -       | 0.26 | 0.00      | 0.00   | yes         |
|                                | 2026-06-19/13.56.14 | Adam      | non-IID | 93.60    | -       | 0.23 | 0.00      | 0.00   | -           |
|                                | 2026-06-19/13.56.22 | Adam      | non-IID | 93.71    | -       | 0.23 | 0.00      | 0.00   | -           |
|                                | 2026-06-20/01.30.27 | SGD       | non-IID | 91.22    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-09/00.24.01 | SGD       | non-IID | 91.41    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-09/00.24.12 | SGD       | non-IID | 91.24    | -       | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-09/19.49.33 | SGD       | non-IID | 91.36    | -       | 1.00 | 1.00      | 1.00   | -           |
| FedDMC, HDBSCAN variant        | 2026-06-18/01.22.11 | Adam      | non-IID | 94.82    | -       | 0.75 | 0.57      | 0.46   | yes         |
|                                | 2026-06-18/01.22.37 | Adam      | non-IID | 97.15    | -       | 0.77 | 0.55      | 1.00   | yes         |
|                                | 2026-06-18/11.32.30 | Adam      | non-IID | 97.17    | -       | 0.80 | 0.58      | 1.00   | yes         |
|                                | 2026-06-18/11.32.46 | Adam      | non-IID | 95.37    | -       | 0.65 | 0.36      | 0.32   | yes         |
| Multi-Krum                     | 2026-06-20/17.03.55 | SGD       | non-IID | 90.96    | -       | 1.00 | 1.00      | 1.00   | -           |
| Auror                          | 2026-06-20/17.04.17 | SGD       | non-IID | 91.02    | -       | 1.00 | 1.00      | 1.00   | -           |
| FoolsGold                      | 2026-04-12/12.07.35 | Adam      | IID     | 42.77    | -       | 0.32 | 0.00      | 0.00   | yes         |
|                                | 2026-07-05/02.50.46 | SGD       | non-IID | 87.63    | -       | 0.26 | 0.24      | 0.79   | -           |

### LIT backdoor attack

| Defense                                            | Run                 | Optimizer | Split   | TACC (%) | ASR (%) | DAR  | Precision | Recall | Pre-fix log |
|----------------------------------------------------|---------------------|-----------|---------|----------|---------|------|-----------|--------|-------------|
| No defense (plain averaging)                       | 2026-07-06/14.19.59 | SGD       | non-IID | 91.40    | 1.02    | 0.72 | 1.00      | 0.00   | -           |
| FedDMC, binary tree (faithful)                     | 2026-06-19/13.57.08 | Adam      | non-IID | 97.94    | 0.38    | 1.00 | 1.00      | 1.00   | -           |
|                                                    | 2026-06-20/01.22.06 | Adam      | non-IID | 98.01    | 0.31    | 1.00 | 1.00      | 1.00   | -           |
|                                                    | 2026-06-21/02.00.26 | SGD       | non-IID | 91.11    | 0.61    | 1.00 | 1.00      | 1.00   | -           |
|                                                    | 2026-07-05/20.38.57 | SGD       | non-IID | 91.21    | 0.65    | 1.00 | 1.00      | 1.00   | -           |
|                                                    | 2026-07-09/00.25.36 | SGD       | non-IID | 91.45    | 0.71    | 1.00 | 1.00      | 1.00   | -           |
| FedDMC, HDBSCAN variant                            | 2026-04-14/08.21.40 | Adam      | non-IID | 97.89    | 0.39    | 0.81 | 0.60      | 1.00   | yes         |
| Multi-Krum                                         | 2026-04-12/23.59.50 | Adam      | IID     | 97.70    | 60.04   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-04-13/00.00.21 | Adam      | IID     | 97.50    | 54.80   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-04-13/00.00.38 | Adam      | IID     | 97.49    | 60.04   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-04-13/00.00.54 | Adam      | IID     | 97.37    | 55.16   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-04-13/00.01.19 | Adam      | IID     | 97.50    | 56.82   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-04-13/16.12.26 | Adam      | non-IID | 97.40    | 82.73   | 0.44 | 0.00      | 0.00   | yes         |
|                                                    | 2026-07-05/20.39.26 | SGD       | non-IID | 91.29    | 1.25    | 0.44 | 0.00      | 0.00   | -           |
|                                                    | 2026-07-06/22.20.15 | SGD       | non-IID | 91.37    | 1.14    | 0.44 | 0.00      | 0.00   | -           |
| Auror                                              | 2026-04-13/16.28.04 | Adam      | non-IID | 97.83    | 50.51   | 0.71 | 0.00      | 0.00   | yes         |
|                                                    | 2026-07-05/13.58.58 | SGD       | non-IID | 91.48    | 1.03    | 0.61 | 0.00      | 0.00   | -           |
|                                                    | 2026-07-09/19.52.06 | SGD       | non-IID | 91.26    | 1.00    | 0.61 | 0.00      | 0.00   | -           |
| FoolsGold                                          | 2026-04-13/16.47.39 | Adam      | non-IID | 97.20    | 60.06   | 0.40 | 0.32      | 1.00   | yes         |
|                                                    | 2026-04-18/02.39.17 | Adam      | non-IID | 96.58    | 19.94   | 0.36 | 0.30      | 1.00   | yes         |
|                                                    | 2026-04-18/02.39.34 | Adam      | non-IID | 96.48    | 25.56   | 0.33 | 0.29      | 1.00   | yes         |
|                                                    | 2026-07-06/00.13.45 | SGD       | non-IID | 91.14    | 0.69    | 0.65 | 0.44      | 1.00   | -           |
|                                                    | 2026-07-09/19.53.23 | SGD       | non-IID | 91.28    | 0.66    | 0.36 | 0.30      | 1.00   | -           |
| FLDetector (not implemented, runs plain averaging) | 2026-04-14/08.21.08 | Adam      | non-IID | 97.67    | 49.00   | 0.72 | 0.00      | 0.00   | yes         |

### Scaling backdoor attack

| Defense                        | Run                 | Optimizer | Split   | TACC (%) | ASR (%) | DAR  | Precision | Recall | Pre-fix log |
|--------------------------------|---------------------|-----------|---------|----------|---------|------|-----------|--------|-------------|
| No defense (plain averaging)   | 2026-07-06/22.18.11 | SGD       | non-IID | 91.00    | 89.92   | 0.72 | 1.00      | 0.00   | -           |
| FedDMC, binary tree (faithful) | 2026-06-20/00.41.08 | Adam      | non-IID | 98.07    | 90.18   | 0.72 | 1.00      | 0.00   | -           |
|                                | 2026-06-20/00.42.42 | Adam      | non-IID | 98.04    | 90.20   | 0.67 | 0.42      | 0.50   | -           |
|                                | 2026-06-20/12.50.58 | SGD       | non-IID | 91.17    | 0.69    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-06-21/01.26.51 | SGD       | non-IID | 91.22    | 0.67    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-05/02.46.58 | SGD       | non-IID | 91.29    | 0.66    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-05/02.47.36 | SGD       | non-IID | 91.36    | 0.67    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/04.28.01 | SGD       | non-IID | 91.19    | 0.75    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/13.03.44 | SGD       | non-IID | 91.14    | 0.70    | 1.00 | 1.00      | 1.00   | -           |
| FedDMC, HDBSCAN variant        | 2026-04-14/23.03.39 | Adam      | non-IID | 98.10    | 90.20   | 0.72 | 0.00      | 0.00   | yes         |
|                                | 2026-04-14/23.03.51 | Adam      | non-IID | 98.29    | 90.20   | 0.72 | 0.00      | 0.00   | yes         |
|                                | 2026-04-17/12.39.25 | Adam      | non-IID | 98.00    | 90.20   | 0.72 | 0.00      | 0.00   | yes         |
|                                | 2026-04-17/12.39.52 | Adam      | non-IID | 95.98    | 90.20   | 0.72 | 0.00      | 0.00   | yes         |
| Multi-Krum                     | 2026-07-04/12.45.13 | SGD       | non-IID | 91.48    | 0.67    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-04/12.48.48 | SGD       | non-IID | 91.29    | 0.73    | 1.00 | 1.00      | 1.00   | -           |
|                                | 2026-07-07/21.38.35 | SGD       | non-IID | 91.21    | 0.68    | 1.00 | 1.00      | 1.00   | -           |
| Auror                          | 2026-07-07/21.38.53 | SGD       | non-IID | 91.18    | 0.70    | 1.00 | 1.00      | 1.00   | -           |
| FoolsGold                      | 2026-07-04/22.14.16 | SGD       | non-IID | 89.71    | 89.83   | 0.26 | 0.27      | 0.93   | -           |
|                                | 2026-07-08/02.04.54 | SGD       | non-IID | 90.61    | 90.17   | 0.24 | 0.25      | 0.86   | -           |

