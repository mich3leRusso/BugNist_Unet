# Domain Adaptation in Volumetric Data Analysis(BugNist)

Domain adaptation in volumetric data analysis presents a significant challenge, particularly when identifying complex-shaped objects in various contexts.

In this project, we present a solution to the *BugNIST* challenge [BugNIST 2024](https://github.com/bugnist2024fgvc), which is part of the *FGVC11* workshop at *CVPR 2024*.

## Project Goals

The goal is to train a model that can detect center points and classify bug types in volumetric scans, where bugs are mixed with other materials.

## Dataset

The *BugNIST* dataset is composed of 12 classes of bugs including larvae, pupae, grasshoppers, etc. The training data consists of 9185 micro-CT scans of individual bugs of each type, while the validation set includes 78 mixture volumes, and the test data includes 155 mixture volumes. Both validation and test sets are provided with center point annotations.

## Methodology

The model will be a neural network designed for detecting and classifying bugs. It is built to be resilient to domain shifts, as the objects of interest have the same appearance in the training set, but the context surrounding these objects will differ in the validation and test sets.
