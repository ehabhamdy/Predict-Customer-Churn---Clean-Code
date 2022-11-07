'''
Testing script for the churn library

Author: Ehab Hussein
Creation Date: 7/11/2022
'''

import logging
import churn_library as cls
import glob
import time

logging.basicConfig(
    filename=f"./logs/churn_library_{time.strftime('%b_%d_%Y_%H_%M_%S')}.log",
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def test_import(import_data):
    '''
    test data import - this example is completed for you to assist with
    the other test functions
    '''
    try:
        df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't appear"
                      " to have rows and columns")
        raise err


def test_eda(perform_eda):
    '''
    test perform eda function
    '''
    try:
        df = cls.import_data("./data/bank_data.csv")
        perform_eda(df)
        eda_images = glob.glob("./images/eda/*")
        assert len(eda_images) == 5
        logging.info("Testing perform_eda: SUCCESS")

    except AssertionError as err:
        logging.error("Testing perform_eda: Some or all EDA diagrams are"
                      "failed to be created")
        raise err


def test_encoder_helper(encoder_helper):
    '''
    test encoder helper
    '''
    try:
        df = cls.import_data("./data/bank_data.csv")
        cat_columns = [
            'Gender',
            'Education_Level',
            'Marital_Status',
            'Income_Category',
            'Card_Category'
        ]

        encoder_helper(df, cat_columns)

        for i in range(len(cat_columns)):
            cat_columns[i] += "_Churn"

        assert set(cat_columns).issubset(df.columns)
        logging.info("Testing encoder_helper: SUCCESS")

    except AssertionError as err:
        logging.error("Testing perform_eda: Some or all EDA diagrams are"
                      "failed to be created")
        raise err


def test_perform_feature_engineering(perform_feature_engineering):
    '''
    test perform_feature_engineering
    '''
    try:
        df = cls.import_data("./data/bank_data.csv")
        X_train, X_test, y_train, y_test = perform_feature_engineering(df)

        assert X_train.shape[0] > 0
        assert X_train.shape[1] > 0

        assert X_test.shape[0] > 0
        assert X_test.shape[1] > 0

        assert y_train.shape[0] > 0

        assert y_test.shape[0] > 0

        logging.info("Testing perform_feature_engineering: SUCCESS")

    except AssertionError as err:
        logging.error("Testing perform_feature_engineering: Failed")
        raise err


def test_train_models(train_models):
    '''
    test train_models
    '''
    try:
        df = cls.import_data("./data/bank_data.csv")
        X_train, X_test, y_train, y_test = cls.perform_feature_engineering(df)
        train_models(X_train, X_test, y_train, y_test)
        model_files = glob.glob("./models/*")
        assert len(model_files) == 2
        logging.info("Testing test_train_models: SUCCESS")
    except AssertionError as err:
        logging.error("Testing test_train_models: Failed")
        raise err


if __name__ == "__main__":
    test_import(cls.import_data)

    test_encoder_helper(cls.encoder_helper)

    test_eda(cls.perform_eda)

    test_perform_feature_engineering(cls.perform_feature_engineering)

    test_train_models(cls.train_models)
