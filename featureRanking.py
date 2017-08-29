##########################################
# FEATURE RANKING Plot :
# make_feature_importance_plot(model_, feature_names_)
# given model_, and feature_names_
# will fail if the model does not have
# feature_importances_
##########################################

# plotly
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot

# numpy
import numpy as np

# pandas
import pandas as pd




def make_feature_importance_plot(model_, feature_names_):
	sorted_feature_names = []
	importances = model_.feature_importances_
	indices = np.argsort(importances)[::-1]

	print("Feature ranking:")

	for f in range(0, len(feature_names_)):
	    print(feature_names_[indices[f]], importances[indices[f]])
	    sorted_feature_names.append(feature_names_[indices[f]])

	    
	traceF = go.Bar(x=sorted_feature_names, y=importances[indices])    

	layoutF = go.Layout(title="Feature importances",
	                       height=1000,
	                       width=1000,
	                    margin=go.Margin(
	                                l=150,
	                                r=250,
	                                b=350,
	                                t=75,
	                                pad=4
	                            ),
	                     yaxis=dict(
			              title='Importance'),              
	                     xaxis=dict(
			              title='Feature')      

	                   )
	fig_ = go.Figure(data=[traceF], layout=layoutF)
	return (fig_)