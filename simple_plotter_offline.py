# plotly
# plotly
from plotly import __version__
from plotly.offline import  init_notebook_mode, iplot
import plotly 
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
import plotly.plotly as py



# numpy
import numpy as np

######################################
# make it easier to create plots     #
######################################

def create_layout(title_, title_x, title_y):
	layout_ = go.Layout(
		    title=title_,
		   # height=600,
     #       width=900,
        margin=go.Margin(
                    l=50,
                    r=50,
                    b=150,
                    t=150,
                    pad=4
                ),
		    xaxis=dict(
		        title=title_x,
		        titlefont=dict(
		            family='Arial, sans-serif',
		            size=18,
		            color='black'
		        ),
		        showticklabels=True,
		        tickangle=45,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='All'
		    ),
		    yaxis=dict(
		        title=title_y,
		        titlefont=dict(
		            family='Arial, sans-serif',
		            size=18,
		            color='red'
		        ),
		        showticklabels=True,
		        tickangle=45,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='All'
		    )
		)
	return layout_

# def create_trace(x_data_, y_data_, meanDivideY_, name_):	
# 	y_data__ = y_data_
# 	if meanDivideY_==1 :
# 		y_data__ = y_data_/y_data_.mean()

# 	trace_ = go.Scatter(
# 	                    x=x_data_, y=y_data__, # Data
# 	                    name=name_ # Additional options                
# 	                    )
# 	return trace_

def create_trace(x_data_, y_data_, meanDivideY_, name_):	
	y_data__ = y_data_
	if meanDivideY_==1 :
		y_data__ = y_data_/y_data_.mean()

	trace_ = go.Scatter(
	                    x=x_data_, y=y_data__, # Data
	                    name=name_, # Additional options                
	                    mode = 'markers'

	                    )
	return trace_


def create_figure(x_data_s, y_data_s, meanDivideY_, name_s, title_, title_x, title_y):
	layout_=create_layout(title_, title_x, title_y)
	data_ = []
	for y_ in range(0, len(y_data_s)):
		tr_ = create_trace(x_data_s[y_], y_data_s[y_], meanDivideY_, name_s[y_])
		data_.append(tr_.copy())	

	#fig_ = go.Figure(data=data_,layout=layout_)
	fig_ = go.Figure(data=data_,layout=layout_)

	return fig_








