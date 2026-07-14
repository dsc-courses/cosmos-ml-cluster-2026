---
layout: assignment
title: "Week 2: Classification"
parent: "📝 Projects"
released: true
nav_order: 2
---

# Week 2: Classification

Aim to complete all labs and the challenge by end-of-day Friday. In particular, the challenge closes at 4pm sharp on Friday (and the winners will be revealed at that time).

## Lab 5

Complete this lab: [Lab 5][lab05]

## Lab 6

Complete this lab: [Lab 6][lab06]

## Lab 7

Complete this lab: [Lab 7][lab07]

## Challenge: Steel Plate Fault Classification

[lab05]: https://colab.research.google.com/github/dsc-courses/cosmos-ml-cluster-2026/blob/main/labs/lab05/build/student/lab05.ipynb
[lab06]: https://colab.research.google.com/github/dsc-courses/cosmos-ml-cluster-2026/blob/main/labs/lab06/build/student/lab06.ipynb
[lab07]: https://colab.research.google.com/github/dsc-courses/cosmos-ml-cluster-2026/blob/main/labs/lab07/build/student/lab07.ipynb
[starter-notebook]: https://colab.research.google.com/github/dsc-courses/cosmos-ml-cluster-2026/blob/main/projects/proj02/steel_plate_faults.ipynb
[kaggle-competition]: https://www.kaggle.com/t/6130717017bb4475a31c4f0044d61ff7

In this challenge, you will build a classifier that identifies the type of fault on a steel plate from measurements collected during manufacturing. Your goal is to make predictions for the rows in `test.csv` and submit them to the [class Kaggle competition][kaggle-competition].

The data has 24 numeric measurements for each plate. The target, `fault_type`, is one of seven kinds of surface fault:

- `Pastry`
- `Z_Scratch`
- `K_Scatch`
- `Stains`
- `Dirtiness`
- `Bumps`
- `Other_Faults`

### Getting started

Open the [starter notebook][starter-notebook] in Google Colab. It downloads the competition data, trains a simple 1-nearest-neighbor model, and creates `submission.csv` in the Colab file browser. Download that file and upload it to Kaggle to make your first submission.

Your submission must have two columns:

```text
id,fault_type
0,Pastry
1,Bumps
```

After making a baseline submission, investigate the data and try different classifiers, preprocessing steps, engineered features, and hyperparameters. Can you improve on the 1-nearest-neighbor model?
