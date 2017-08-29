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

# collections 

from collections import Counter


# init offline mode
#offline.init_notebook_mode(connected=True)




def word_freq(list_, title_, title_x, title_y):
	freq = 	Counter(list_)
	words, counts = zip(*freq.items())	
	# print (freq)
	# print(words)
	# print(counts)


	# sorting : 
	sort_ = np.argsort(counts)[::-1]
	# print(sort_)
	

	counts_sorted = []
	words_sorted = []

	for f in sort_:
	    words_sorted.append(words[f])
	    counts_sorted.append(counts[f])


	# print(words_sorted)
	# print(counts_sorted)

	traceF = go.Bar(x=words_sorted, y=counts_sorted)    

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
	# plotly.offline.plot(fig_, show_link=False, filename='/Users/Shalhout/Desktop/TEMP.html')
	# py.iplot(fig_)
	return fig_




