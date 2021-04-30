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
# filepath_in = '/Users/maxsun/EAT/' # use output files from JH_CSV_DataCleaner
# filepath_out = './Plots/'   # where the plot gets saved
# file_name = 'EquipmentOutput' #name of the file w/o .csv suffix (used to conveniently name plots, but maybe not robust)
#
# df = pd.read_csv(filepath_in + file_name + '.csv') # read data into a DataFrame and print some info
# print('\nDATA READ SUCCESSFULLY...\n')
# print(df)
#
# # call a function from eatlib to plot the data
# print('calling plot_time function...')
# fig = plot_time(df)
# fig.write_html(filepath_out + file_name + '_Plot.html')   # write the plot to html so it's shareable
# fig.show()



# 2: call plot_x function from eatlib - STABLE
# df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
# df = df.abs()
# print('\nDATAFRAME CREATED...\n')
# print(df.head())
#
# print('calling plot_x function...')
# plot_x(df) #call a function from eatlib to plot the data



# 3: plot clean EAT data using plot_time - STABLE
# define paths and filenames
filepath_in = '../DataCleaner Output Files/'  # use output files from JH_CSV_DataCleaner
filepath_out = '../Plots/'  # where the plot gets saved
file_name = '2019 CHP Raw Trend_OUT_Clean_Data' #name of the file w/o .csv suffix (used to conveniently name plots, but maybe not robust)

df = pd.read_csv(filepath_in + file_name + '.csv') # read data into a DataFrame and print some info
print('\nDATA READ SUCCESSFULLY...\n')
print(df)

# !!! drop the first column of data so timestamps are in column
df.drop(df.columns[0],axis=1,inplace=True)

# call a function from eatlib to plot the data
print('calling plot_time function...')
fig = plot_time(df)
fig.write_html(filepath_out + file_name + '_Plot.html')   # write the plot to html so it's shareable
fig.show()


####################################################################################################################
# SANDBOX

# # 12: test os & random
# example_data_path = './example data/'
#
# df = pd.read_csv(example_data_path + random.choice(os.listdir(example_data_path)))  # pick a random file from ./example_data
# if df.columns[0] == 'Unnamed: 0':
#     df.drop(df.columns[0], axis=1, inplace=True)  # !!! drop the first column of data so timestamps are in column
# print('calling plot_time function...')
# fig = plot_time(df)
# st.subheader('Example Data:')
# st.dataframe(df)
# st.subheader('Example Point Trends:')
# st.plotly_chart(fig, use_container_width=True)


# # 11: test streamlit
# import streamlit as st
# import pandas as pd
# import altair as alt
#
# @st.cache
# def get_UN_data():
#     AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#     df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#     return df.set_index("Region")
#
# try:
#     df = get_UN_data()
#     countries = st.multiselect(
#         "Choose countries", list(df.index), ["China", "United States of America"]
#     )
#     if not countries:
#         st.error("Please select at least one country.")
#     else:
#         data = df.loc[countries]
#         data /= 1000000.0
#         st.write("### Gross Agricultural Production ($B)", data.sort_index())
#
#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=["index"]).rename(
#             columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#         )
#         chart = (
#             alt.Chart(data)
#             .mark_area(opacity=0.3)
#             .encode(
#                 x="year:T",
#                 y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                 color="Region:N",
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
# except urllib.error.URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#
#         Connection error: %s
#     """
#         % e.reason
#     )



## 10: test out psychrochart
# from psychrochart import PsychroChart
# import matplotlib.pyplot as plt
#
# PsychroChart('minimal').plot(ax=plt.gca())
# plt.show()



# 9: try reading excel file
# root = './' # define path to sample data
#
# df = pd.read_excel(root + 'User Inputs 2.xlsx', sheet_name=2) # read data into a DataFrame and print some info
# print('\nDATA READ SUCCESSFULLY...\n')
# print(df)



# 8: test plot_time function on Salk EBS1 data
# root = '/Users/maxsun/EAT' # define path to sample data
#
# df = pd.read_csv(root + '/CWRF EBS August and September 2020.csv') # read data into a DataFrame and print some info
# print('\nDATA READ SUCCESSFULLY...\n')
# print(df)
#
# print('calling plot_time function...')
# plot_time(df) #call a function from eatlib to plot the data



# 7: test multiple line plot
# import plotly.graph_objects as go
#
# root = '.' # define path to sample data
#
# df = pd.read_csv(root + '/2019 CHP Raw Trend_OUT_Clean_Data.csv') # read data into a DataFrame and print some info
# print('\nDATA READ SUCCESSFULLY...\n')
# print(df)
#
# # Create traces
# fig = go.Figure()
# columns = df.columns
# timestamps = pd.to_datetime(df.iloc[:, 1])
#
# for i in range(df.shape[1]-2):
#     print(df.columns[i+2],':',df.iloc[0,i+2])
#     fig.add_trace(go.Scatter(x=timestamps, y=df.iloc[:,i+2],
#                         mode='lines',
#                         name=df.columns[i+2]))
#
# fig.show()



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
