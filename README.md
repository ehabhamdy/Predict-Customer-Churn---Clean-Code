# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
This project is intended to train a model capable of detect customer churn rates. 

## Files and data description
The project consists of the following files:
1. `churn-notebook.ipynb`: A jupyter notebook for model building and exploratory data analysis of the data set.
2. `churn_library.py`: A python script that contains the cleaned up code from the jupyter notebook that reads the data sets, perform EDA and train Logistic Regression and Random Forests models to detect customers churn. The script saves the trained models into the results folder `./models`. The resulting plots of the EDA are also saved under the `./images/eda` folder.
3. `chrun_script_logging_and_tests.py`: A test suite for testing core functions of the churn_library script to ensure.  

## Running the project

### Dependencies
Perform the following steps to prepare your environment with the required dependencies:
1. Install pip and venv, please refer to these instructions for more details https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
2. While in the root directory of this project, create a virtual environment using the command:
`python3 -m venv churn-env`
3. Activate the environment: `source churn-env/bin/activate`
4. Install the dependencies inside the activated env: `python -m pip install -r requirements_py3.8.txt`

### Instructions
There are two options to run the project:
1. Use the notebooks and executes each celll to perform the necessary steps.
2. Use the `churn_library.py`, In your terminal windows, run `python chun_library.py`


### Expected Output
The script will train two models to predict customer churn. The script will also generate models files, results plots and the EDA plots and save them into the respective output files.


