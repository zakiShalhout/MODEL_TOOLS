
###########################################################################
# given an input_dataFrame_, a traget_ dataFrame consiting only of the targets, 
# a testing_fraction, a random_state
# and an index_ variable return:
# dataframes : x_train, y_train, x_test, y_test, index_
# and the StandardScaler applied to x_train and x_test

# numpy
import numpy as np

# pandas
import pandas as pd

# sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def get_prepped_data_multipleTargets(input_dataFrame_, target_, index_, testing_fraction, random_state):
   

    # target
    y_ = target_
    #y_ = y_.values.reshape((len(y_), ))

    # features 

    x_ = input_dataFrame_.copy()
    x_ = input_dataFrame_.drop(target_, axis=1, inplace=False)


    # keep the date alone

    date_ = x_[index_]
    date_ = date_.values.reshape((len(date_), -1))

    # drop date from features used for model

    x_ = x_.drop(index_, axis=1, inplace=False)

    cleanedData = x_.copy()

    x_ = x_.values.reshape((len(x_), -1))

    # # apply the standard scaler to x_

    # scaler = preprocessing.StandardScaler().fit(x_)
    # x_ = scaler.transform(x_)


    # split into training and testing data and keep the date_

    x_train, x_test, y_train, y_test, date_train, date_test = train_test_split(
        x_, y_, date_, test_size=testing_fraction, random_state=random_state)   

    # apply the standard scaler to x_train

    scaler = preprocessing.StandardScaler().fit(x_train)
    print(" be sure to apply scaler to data before fit or predict")
    return x_train, y_train, x_test, y_test, date_test, date_train, scaler, cleanedData
