# GAN Synthetic Data Generator

This project implements **Generative Adversarial Networks (GANs)** for generating synthetic tabular data.
It demonstrates how deep learning models can learn the distribution of a dataset and generate new realistic samples.

The system includes:

* Custom GAN implementation using **PyTorch**
* **CTGAN** (state-of-the-art GAN for tabular data)
* Synthetic data generation
* Synthetic data evaluation and comparison
* Visualization of real vs generated distributions

The project simulates a **real-world synthetic data generation pipeline used in machine learning research and privacy-preserving data systems.**

---

# Project Overview

Synthetic data generation is an important technique in machine learning when:

* Real data is limited
* Privacy restrictions prevent sharing datasets
* Additional training data is required
* Data augmentation is needed

Generative models such as **GANs** can learn the underlying distribution of the dataset and generate new synthetic samples.

This project demonstrates how generative AI can be applied to **healthcare tabular datasets**.

---

# Dataset

The dataset used in this project contains **healthcare features related to diabetes prediction**.

Features include:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age
* Outcome

Example dataset structure:

```
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
```

The dataset contains **769 records** used to train the generative models.

---

# Generative Models Implemented

## Custom GAN (PyTorch)

A deep learning model composed of two neural networks:

Generator

* Produces synthetic data samples from random noise

Discriminator

* Distinguishes between real and generated samples

Both models are trained adversarially to improve sample realism.

---

## CTGAN (Conditional Tabular GAN)

CTGAN is a specialized GAN designed for **tabular datasets**.

Advantages:

* Handles mixed numerical and categorical features
* Better modeling of complex tabular distributions
* Widely used in synthetic data research

---

# Synthetic Data Evaluation

The project includes an evaluation module that compares real and synthetic datasets using:

* Statistical similarity
* Feature distribution comparison
* Correlation analysis
* Visualization of real vs synthetic data

These techniques are commonly used in **synthetic data research and benchmarking.**

---

# Project Structure

```
gan-synthetic-data-generator
│
├── data
│   ├── dataset.csv
│
├── screenshots
│   ├── img.jpg
│
├── models
│   └── generator.pth
│
├── src
│   ├── generator.py
│   ├── discriminator.py
│   ├── train_gan.py
│   ├── generate_samples.py
│   ├── train_ctgan.py
│   └── evaluate_synthetic_data.py
│
├── requirements.txt
└── README.md
```

---

# Machine Learning Pipeline

The system follows a full generative AI workflow:

```
Dataset
   ↓
Data Preprocessing
   ↓
GAN Training
   ↓
Synthetic Data Generation
   ↓
Synthetic Data Evaluation
   ↓
Visualization & Analysis
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd gan-synthetic-data-generator
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Train the GAN model:

```
python src/train_gan.py
```

Generate synthetic samples:

```
python src/generate_samples.py
```

Train CTGAN model:

```
python src/train_ctgan.py
```

Evaluate synthetic data quality:

```
python src/evaluate_synthetic_data.py
```

---

# Example Outputs

Synthetic datasets generated:

```
data/generated_samples.csv
data/ctgan_synthetic_data.csv
```

Visualization results:

```
screenshots/img.jpg
screenshots/ctgan_distribution.jpg
screenshots/real_correlation.png
screenshots/synthetic_correlation.png
```

---

# Applications

Synthetic data generation is widely used in:

* Healthcare data simulation
* Privacy-preserving data sharing
* Machine learning data augmentation
* Financial data generation
* Generative AI research

---

# Technologies Used

* Python
* PyTorch
* CTGAN
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

# Future Improvements

Possible enhancements include:

* Conditional GAN models
* Diffusion-based synthetic data generation
* Multi-table synthetic data generation
* Synthetic data privacy evaluation
* Benchmarking multiple generative models

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

