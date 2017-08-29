# numpy
import numpy as np

# pandas
import pandas as pd

# sklearn
from sklearn.feature_selection import VarianceThreshold


#######
# return a dataFrame
# with features with var below minimum_variance_
# removed using VarianceThreshold
# def get_VarianceThreshold_selector_FilteredDataFrame(data_, minimum_variance_):
#     return_data = data_.copy()
#     columns = return_data.columns
#     drop_labels = []
#     for c in columns:
#         value_ = ((return_data[c]-return_data[c].mean())/(return_data[c].max()-return_data[c].min())).var()
#         if value_ < minimum_variance_:
#             drop_labels.append(c)

#             print ("dropping ",c, " var[(x-mean)/(x_max-x_min)]  = ", 
#             ((return_data[c]-return_data[c].mean())/(return_data[c].max()-return_data[c].min())).var()
#             )

    # selector = VarianceThreshold(minimum_variance_)
    # selector.fit(data_)
    # print(list(data_))
    # print(selector.get_support())

    # keep_labels = [columns[x] for x in selector.get_support(indices=True) if x]
    # drop_labels = list( set(list(columns))-set(keep_labels) )
    # for d in drop_labels:
    #     print (" dropping feature ", d, "....")
    #     return_data.drop(d, axis=1, inplace=True)
    # print(" new dataframe has ", len(list(return_data)), " features with VAR > ", minimum_variance_)
    #return return_data




#######
# corr can be ruined by
# variables of low variance
# given a dataframe, a list of features to ignore, and a minimum
# variance return a new dataframe with only ignored features + 
# features with var > min_var

def get_good_var_data(data_, min_var, keep_feature_list):
    df = data_.copy()
    df_x =  data_.copy()

    for i in keep_feature_list:
        df_x.drop(i, axis=1, inplace=True)

    df_norm = (df_x - df_x.mean()) / (df_x.max() - df_x.min())

    feat_preSort = []
    var_preSort = []

    for k in list(df_norm):
        if k not in keep_feature_list:
            feat_preSort.append(k)
            var_preSort.append(df_norm[k].var())

    # sorting : 

    feat_postSort = []
    var_postSort = []

    sort_ = np.argsort(var_preSort)[::-1]

    for f in sort_:
        feat_postSort.append(feat_preSort[f])
        var_postSort.append(var_preSort[f])

        drop_list = []
    for t in range(0, len(feat_postSort)):
        if var_postSort[t] < min_var:
            drop_list.append(feat_postSort[t])
            print (feat_postSort[t], var_postSort[t], " ... dropping ")
        else:
            print (feat_postSort[t], var_postSort[t], " ... keeping ")
        
    for d in drop_list:
        df.drop(d, axis=1, inplace=True)

    return df        






#####################################################################
# for a dataframe (target_dataFrame) with a feature (target_Feature)
# and a second dataframe (second_data_frame) minus some features (drop_list)
# return a sorted list of linear correlations and features 
# if ABS = 1 return abs(corr)
########################################################################

def get_correlations_with_targetDataFrame(target_dataFrame, target_Feature, second_data_frame, drop_list, ABS):
    d_ = second_data_frame.copy()
    for drop_ in drop_list:
        d_ = d_.drop(drop_, axis=1, inplace=False)

    
    feature_names = list(d_)
    correlations = []

    for k in feature_names:        
        z = (float(target_dataFrame[target_Feature].corr(d_[k])))
        if ABS == 1:
            z = abs(float(target_dataFrame[target_Feature].corr(d_[k])))
        if pd.isnull(z) is False :
            correlations.append(z)
        else:
            correlations.append(0)

    #print(correlations)
    indices = np.argsort(correlations)[::-1]
    sorted_feature_names = []
    sorted_corr = []

    for f in range(0,d_.shape[1]):
        #print(f, d_.shape[1], feature_names[indices[f]])
        #print(feature_names[indices[f]], correlations[indices[f]])
        sorted_feature_names.append(feature_names[indices[f]])
        sorted_corr.append(correlations[indices[f]])
    return sorted_feature_names, sorted_corr


###############
# from a data_frame conatining a target_feature and a list of
# features to ignore (drop_list)
# return a correlation list of features 
# and the |correlations|


def get_correlations_with_target(target_feature, data_frame, drop_list):
    d_ = data_frame.drop('Date', axis=1, inplace=False)
    for drop_ in drop_list:
        d_ = d_.drop(drop_, axis=1, inplace=False)

    
    feature_names = list(d_)
    correlations = []

    for k in feature_names:
        z = abs(float(d_['A2 BAY 10 MLIQ DO'].corr(d_[k])))
        if pd.isnull(z) is False :
            correlations.append(z)
        else:
            correlations.append(0)

    #print(correlations)
    indices = np.argsort(correlations)[::-1]
    sorted_feature_names = []
    sorted_corr = []

    for f in range(0,d_.shape[1]):
        #print(feature_names[indices[f]], correlations[indices[f]])
        sorted_feature_names.append(feature_names[indices[f]])
        sorted_corr.append(correlations[indices[f]])
    return sorted_feature_names, sorted_corr


##################################################
# given a list of features ranked by correlation
# the ranked |correlation| values
# and a |correlation| max
# return a reduced dataframe of features
# where fi.corr(fj) < |correlation max|  for all i, j
# features in ignore_list will be kept 


def get_uncorrelated_features(sorted_feat, sorted_corr, max_corr, input_data, ignore_list):
    output_data = input_data.copy()
    to_drop = []
    for k in range(0, len(sorted_feat)):
        for l in range(k+1, len(sorted_feat)):
            if sorted_feat[k] not in ignore_list:
                if sorted_feat[l] not in ignore_list:
                    corr_ = abs(input_data[sorted_feat[k]].corr(input_data[sorted_feat[l]]))
                    if corr_ >= max_corr :
                        to_drop.append(sorted_feat[l])
    to_drop = list(set(to_drop))
    #print(to_drop)
    for k in to_drop:
        output_data = output_data.drop(k, axis=1, inplace=False)
    return output_data
        