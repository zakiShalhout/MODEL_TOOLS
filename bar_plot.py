#######################
# given a list_ of words
# make a sorted occurance freq. 
# plot

# plotly
from plotly import __version__
from plotly.offline import  init_notebook_mode, iplot
import plotly 
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
import plotly.plotly as py

# numpy
import numpy as np


# take to lists list_x, list_y along with titles
# and return a bar plot fig 

def bar_plot(list_x, list_y, title_, title_x, title_y):
	

	traceF = go.Bar(x=list_x, y=list_y)    

	layoutF = go.Layout(title=title_,
		xaxis=dict(title=title_x),
		yaxis=dict(title=title_y),
        margin=go.Margin(
            l=50,
            r=50,
            b=150,
            t=100,
            pad=4)
		)

	fig_ = go.Figure(data=[traceF], layout=layoutF)
	return fig_




