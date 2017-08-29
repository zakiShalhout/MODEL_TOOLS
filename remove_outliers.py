import pandas as pd

####################### 
# remove outliers     #
####################### 
# given a dataframe (df_) and a key column name
# (column_name_) and a multiplier on 1 std (std_factor)
# return a new dataframe with only rows in which df_[column_name_]
# is within mean+/-std_factor*STD

def get_outlier_filtered_data(df_, column_name_, std_factor):
	
	df_return = df_.copy()
	max_do_2sigma = df_return[column_name_].mean()+std_factor*df_return[column_name_].std()
	min_do_2sigma = df_return[column_name_].mean()-std_factor*df_return[column_name_].std()

	df_return = df_return[df_return[column_name_] <= max_do_2sigma]
	df_return = df_return[df_return[column_name_] >= min_do_2sigma]

	return df_return
#######################################


