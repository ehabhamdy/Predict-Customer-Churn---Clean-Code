# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
Customer churn is defined as the loss of existing customers. The project purpose is to build, train and ability 
to forecast customers who are likely to churn or in other words finding out customers who are going to
close their accounts. In this project we have applied software engineering and clean code best practices
to transfrom the code developed in the jupyter notebook into a reusable and testable library reliable for
production use.

## Dataset
We have utilized the kaggle data set for the `Credit Card Customer Churn Prediction` competition.
This dataset represent records of credit card customers. 
It contains 10,127 instances (customers) and 16.0% of them are attrited.

For more details, please visit:
https://www.kaggle.com/c/1056lab-credit-card-customer-churn-prediction


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
3. For testing the churn library, you can run `python churn_script_logging_and_test.py` The results is savved under ./logs/churn_library.log


### Expected Output
The script will train two models to predict customer churn. The script will also generate models files, results plots and the EDA plots and save them into the respective output files.


