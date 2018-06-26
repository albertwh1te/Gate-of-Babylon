"""machinelearning model utility code
includes but not limited to,
model selection ,train test split,feature engineering and model training.
"""
from random import randint
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import roc_curve, auc, roc_auc_score, classification_report


__all__ = ['TrainTestValidation', 'runLGB', 'split', 'evaluate']

TRAIN_TEST_SPLIT_NUMBER = 2 / 10
TRAIN_TEST_SPLIT_NUMBER = 2 / 10


def log(*args):
    return print(args)


def TrainTestValidation(X, y):
    """
    get test train validation lightgbm datasets from X,y
    """
    X_train, y_train, X_test, y_test = split(X, y, 0.2)
    X_train, y_train, X_val, y_val = split(X_train, y_train, 0.2)
    log("split part is finished and the train,test validation nums are")
    log(X_train.shape, y_train.shape, X_test.shape,
        y_test.shape, X_val.shape, y_val.shape)
    return X_train, y_train, X_test, y_test, X_val, y_val


def split(X, y, test_size):
    """
    split data set into two pieces (maintain the distribution of data)
    """
    s = StratifiedShuffleSplit(
        n_splits=1, test_size=test_size, random_state=randint(1, 42))
    for train_index, test_index in s.split(X, y):
        X_train = X.iloc[train_index]
        y_train = y.iloc[train_index]
        X_test = X.iloc[test_index]
        y_test = y.iloc[test_index]
    return X_train, y_train, X_test, y_test


def lgb_train(train_data, val_data, parameters):
    """
    train a lightgb model with parameters
    """
    model = lgb.train(parameters,
                      train_data,
                      valid_sets=[train_data, val_data])
    log('train finished')
    return model


def evaluate(model, X_test, y_test):
    """
    print following things:
        TPR= TP/(TP+FN)
        FPR = FP/(FP+TN)
        AUC: Area Under the ROC Curve
    """
    y_pred = model.predict(X_test)
    false_positive_rate, true_positive_rate, thresholds = roc_curve(
        y_test, y_pred)
    log("false_positive_rate:{fpr}\ntrue_positive_rate:{tpr}".format(
        fpr=false_positive_rate, tpr=true_positive_rate))
    log('roc auc:')
    log(roc_auc_score(y_test, y_pred))
    log('classification report:')
    y_pred = list(1 if x > 0.5 else 0 for x in y_pred)
    log(classification_report(y_test, y_pred))


def runLGB(raw: pd.DataFrame, parameters: dict, lablename: str):
    """
    split => train => evaluation
    """
    X = raw.drop(columns=[lablename])
    y = raw[lablename]
    # pandas dataframe to lightgbm datasets
    X_train, y_train, X_test, y_test, X_val, y_val = TrainTestValidation(X, y)
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val)
    model = lgb_train(train_data, val_data, parameters)
    evaluate(model, X_test, y_test)
    return model
