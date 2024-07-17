# Fish Weight Prediction

This repository contains a Flask web application that predicts the weight of a fish based on its measurements using a trained machine learning model. The model is trained on the Fish Market dataset.


## Overview
The Fish Weight Prediction application uses a machine learning model to predict the weight of a fish based on its length, height, and width. The model is trained using the Fish Market dataset and is served through a Flask web application.

## Dataset
The dataset used for training the model is the Fish Market dataset, which contains measurements of various fish species. The dataset can be found [here](https://www.kaggle.com/aungpyaeap/fish-market).

## Model
The model used for prediction is a Random Forest Regressor, which provides high accuracy for regression tasks. The model is trained using the following features:
- Length1
- Length2
- Length3
- Height
- Width

## Web Application
The web application is built using Flask. It provides a simple web interface where users can input the measurements of a fish and get the predicted weight.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fish-weight-prediction.git
   cd fish-weight-prediction
