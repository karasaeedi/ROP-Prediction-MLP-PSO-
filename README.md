# Optimization of Drilling Rate of Penetration Using Artificial Intelligence Algorithms

## Overview

This project investigates the application of Artificial Intelligence (AI) and Machine Learning (ML) techniques to predict the Rate of Penetration (ROP) in drilling operations.

The study combines a **Multilayer Perceptron (MLP)** neural network with **Particle Swarm Optimization (PSO)** to improve the prediction performance of a data-driven drilling model.

Accurate ROP prediction is important in drilling engineering because drilling performance directly affects operational efficiency, drilling time, and overall costs. AI-based approaches can help identify relationships between drilling parameters and ROP that may be difficult to capture using conventional mathematical models.

This project is based on my research paper, *Optimization of the Drilling Rate of Penetration Using Artificial Intelligence Algorithms*, presented at the 18th National Congress of Chemical Engineering.

## Research Objectives

- Develop an MLP-based model to predict drilling Rate of Penetration.
- Apply Particle Swarm Optimization to optimize the neural network model.
- Evaluate model performance using training, validation, and test datasets.
- Analyze prediction errors and compare predicted ROP values with actual values.
- Investigate the potential of AI-based methods for drilling performance analysis.

## Input Features and Target Variable

The model uses drilling parameters as input features to predict the Rate of Penetration.

| Input feature | Description | Unit |
|---|---|---|
| D | Depth | ft |
| WOB | Weight on Bit | klbf |
| N | Rotary Speed | rpm |
| Bit Diameter | Drill Bit Diameter | in |
| T | Torque | lbf·ft |
| Q | Flow Rate | gpm |
| Mud Density | Drilling Fluid Density | lbm/gal |
| SPP | Standpipe Pressure | psi |

**Target variable:** Rate of Penetration (ROP), measured in ft/h.

## Methodology

### 1. Data Preparation

The drilling dataset is prepared for machine learning. Data preprocessing and feature scaling are used as implemented in the research code.

The data is divided into training, validation, and test sets to evaluate the model's predictive performance.

### 2. Multilayer Perceptron (MLP)

An MLP neural network is used to learn the nonlinear relationship between drilling parameters and ROP.

The network architecture includes four hidden layers. The implementation also incorporates dropout regularization.

### 3. Particle Swarm Optimization (PSO)

PSO is a population-based optimization algorithm inspired by the collective behavior of particles.

In this project, PSO is used to optimize the neural network according to the objective function implemented in the code. The optimization process uses Mean Squared Error (MSE) as its objective.

### 4. Model Evaluation

The model is evaluated using the following regression metrics:

- **R² (Coefficient of Determination):** Measures how well the model explains the variation in the target values.
- **RMSE (Root Mean Squared Error):** Measures the typical magnitude of prediction errors, with greater weight given to larger errors.
- **MSE (Mean Squared Error):** Measures the average squared difference between predicted and actual values.

Prediction plots and error histograms are used to examine model behavior.

## Results

The research reports the following evaluation results for the MLP-PSO model:

| Dataset | R² | RMSE |
|---|---:|---:|
| Training | 0.99 | 5.23 |
| Validation | 0.98 | 9.23 |
| Test | 0.99 | 5.84 |

*RMSE is reported in the same unit as the target variable (ft/h), assuming the metrics were calculated on the original ROP scale.*

The reported results indicate strong predictive performance on the evaluated dataset. The validation RMSE is higher than the training and test RMSE, so the results should be interpreted in the context of the dataset, split strategy, and model evaluation procedure.

The research also examines error distributions and compares predicted ROP values with actual values across depth.

**Note:** These values are the results reported in the research paper. Reproducibility depends on the dataset, preprocessing steps, model configuration, and optimization settings used in the implementation.

## Repository Structure

```text
rop-prediction-mlp-pso/
├── notebooks/    # Jupyter Notebook for the research workflow
├── src/          # Python source code
├── data/         # Dataset and related documentation
├── results/      # Research plots and visualizations
├── README.md     # Project documentation
└── .gitignore    # Git ignore rules
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Keras
- Matplotlib
- Particle Swarm Optimization (PSO)

Please refer to the project code and dependency files for the exact libraries and versions used.

## How to Use

1. Clone or download the repository.
2. Install the required Python dependencies.
3. Review the dataset and preprocessing steps.
4. Open the Jupyter Notebook in the `notebooks/` directory, or run the Python script in `src/`.
5. Follow the execution order and configuration specified in the code.

The execution instructions and dependencies should be verified against the final implementation.

## Research Publication

**Title:** Optimization of the Drilling Rate of Penetration Using Artificial Intelligence Algorithms

**Conference:** 18th National Congress of Chemical Engineering

**Research areas:** Artificial Intelligence, Machine Learning, Drilling Engineering, and ROP Prediction

**Methods:** Multilayer Perceptron (MLP) and Particle Swarm Optimization (PSO)

Full bibliographic details and a publication link can be added when the official conference record is available.


## Copyright and Usage

Copyright © 2026 Kara Saeedi. All rights reserved.

This repository contains research code and materials associated with the project described above.

No license is granted to copy, modify, redistribute, or commercially use the original code or research materials without prior written permission from the copyright holder, except where permitted by applicable law.

For permission to use or reproduce any part of this work, please contact the author.

Please cite the original research paper when referring to the research methodology or findings.
