####################################################################################################################
# max.py
#
# script for demonstrating weekly progress - Max
# imports and calls functions from eatlib



####################################################################################################################
# IMPORTS
from eatlib import * # import eatlib - the only library you'll ever need



####################################################################################################################
# SCRIPT

# 1: call plot_time function from eatlib - STABLE
# root = '/Users/maxsun/EAT' # define path to sample data
#
# df = pd.read_csv(root + '/EquipmentOutput.csv') # read data into a DataFrame and print some info
# print('\nDATA READ SUCCESSFULLY...\n')
#
# print('calling plot_time function...')
# plot_time(df) #call a function from eatlib to plot the data

# 1: call plot_time function from eatlib - STABLE
df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
print('\nDATAFRAME CREATED...\n')

print('calling plot_x function...')
plot_x(df) #call a function from eatlib to plot the data



####################################################################################################################
# SANDBOX

# 6: use Plotly Express to create entire figures at once. RECOMMENDED APPROACH
# import pandas as pd
# pd.options.plotting.backend = "plotly"
#
# df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
# fig = df.plot()
# fig.show()



# # 5: use graph objects figure constructor
# import plotly.graph_objects as go
#
# fig = go.Figure(data=go.Bar(y=[2,3,1]))
# fig.write_html('first_figure.html', auto_open=True)



# # 4: use Plotly Express to create entire figures at once. RECOMMENDED APPROACH
# import plotly.express as px
#
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
#
# # If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)
#
# fig.show()



# # 3: create graph object figure from dictionary representation using go.Figure
# import plotly.graph_objects as go
#
# dict_of_fig = dict({
#     "data": [{"type": "bar",
#               "x": [1, 2, 3],
#               "y": [1, 3, 2]}],
#     "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
# })
#
# fig = go.Figure(dict_of_fig)
#
# fig.show()



# # 2: use a graph object instead of a dictionary
# import plotly.graph_objects as go
#
# fig = go.Figure(
#     data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
#     layout=go.Layout(
#         title=go.layout.Title(text="A Figure Specified By A Graph Object")
#     )
# )
#
# fig.show()



# # 1: low level, create figures ground up using dictionaries
# fig = dict({
#     "data": [{"type": "bar",
#               "x": [1, 2, 3],
#               "y": [1, 3, 2]}],
#     "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
# })
#
# # To display the figure defined by this dict, use the low-level plotly.io.show function
# import plotly.io as pio
#
# pio.show(fig)
