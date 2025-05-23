# Eye Detection

The Eye Detection project is a machine learning application designed to detect whether human eyes in images are open or closed. This functionality is particularly useful in applications such as drowsiness detection systems, where monitoring eye states can help prevent accidents caused by driver fatigue.

## Repository Outline
```
1. README.md - This file
2. Eye_Detection.ipynb - The main notebook containing the data analysis, data processing and modeling process.
3. Eye_Detection_Inference.ipynb - Model inference of the model made in the main notebook.
4. url.txt - File containing URL of the dataset and model deployment.
5. Deployment - Folder containing files required for the deployment.
    a. app.py - The main script.
    b. model_new.keras - Model output
```

## Problem Background
The goal is to create a machine learning model with the ability to accurately classify images of human eyes. The model checks whether the eyes are open or closed. This model can serve as a foundational component for real-life applications, such as drowsiness detection systems.

## Project Output
The output of the project is a deployable machine learning model that can detect open/closed eyes in images.

## Data
The dataset used is generated using MRL and Closed Eyes in Wild (CEW) combined with a personal database from the uploader. The data consists of images showing opened and closed eyes that were taken under various conditions, including diverse lighting conditions, distance, and angle. The current version used is the 4th version which contains a total of 4000 images. The data is balanced between opened and closed eyes images with a total 2000 images for each case.

## Method
This is a machine learning project that utilize CNN model algorithm. There are two different models trained in the notebook with the difference in the model architecture.


## Stacks
Language:
- Python

Tools:
- Visual Studio Code
- HuggingFace

Library:
- NumPy
- Matplotlib
- Seaborn
- Tensorflow
- Scikit-learn

## Reference
Dataset:
- https://www.kaggle.com/datasets/prasadvpatil/mrl-dataset/data

Deployment:
- https://huggingface.co/spaces/thalibanallaam/EyeDetection
---
