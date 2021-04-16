# ####################################################################################################################
# # Going to try to use dash with EAT code
# # visit http://127.0.0.1:8050/ in your web browser.
#
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd
# from eatlib import * # import eatlib - the only library you'll ever need
#
# # define paths and filenames
# filepath_in = './DataCleaner Output Files/' # use output files from JH_CSV_DataCleaner
# filepath_out = './Plots/'   # where the plot gets saved
# file_name = '2019 CHP Raw Trend_OUT_Clean_Data' #name of the file w/o .csv suffix (used to conveniently name plots, but maybe not robust)
#
# # read data into a DataFrame and print some info
# df = pd.read_csv(filepath_in + file_name + '.csv')
# print('\nDATA READ SUCCESSFULLY...\n')
# print(df)
#
# # !!! drop the first column of data so timestamps are in column
# df.drop(df.columns[0],axis=1,inplace=True)
#
# # call a function from eatlib to plot the data
# fig = plot_time(df)
#
# # dash stuff
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
#
# ####################################################################################################################
#
#
#
#
#
#
#
#
#
# ####################################################################################################################
# # # Run this app with `python dash_app.py` and
# # # visit http://127.0.0.1:8050/ in your web browser.
# #
# # import dash
# # import dash_html_components as html
# # import pandas as pd
# #
# # df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
# #
# #
# # def generate_table(dataframe, max_rows=10):
# #     return html.Table([
# #         html.Thead(
# #             html.Tr([html.Th(col) for col in dataframe.columns])
# #         ),
# #         html.Tbody([
# #             html.Tr([
# #                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
# #             ]) for i in range(min(len(dataframe), max_rows))
# #         ])
# #     ])
# #
# #
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #
# # app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# #
# # app.layout = html.Div(children=[
# #     html.H4(children='US Agriculture Exports (2011)'),
# #     generate_table(df)
# # ])
# #
# # if __name__ == '__main__':
# #     app.run_server(debug=True)
# ####################################################################################################################
#
#
#
#
#
#
#
#
#
# ####################################################################################################################
# # # -*- coding: utf-8 -*-
# #
# # # Run this app with `python dash_app.py` and
# # # visit http://127.0.0.1:8050/ in your web browser.
# #
# # import dash
# # import dash_core_components as dcc
# # import dash_html_components as html
# # import plotly.express as px
# # import pandas as pd
# #
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #
# # app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# #
# # colors = {
# #     'background': '#111111',
# #     'text': '#7FDBFF'
# # }
# #
# # # assume you have a "long-form" data frame
# # # see https://plotly.com/python/px-arguments/ for more options
# # df = pd.DataFrame({
# #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# #     "Amount": [4, 1, 2, 2, 4, 5],
# #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # })
# #
# # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# #
# # fig.update_layout(
# #     plot_bgcolor=colors['background'],
# #     paper_bgcolor=colors['background'],
# #     font_color=colors['text']
# # )
# #
# # app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
# #     html.H1(
# #         children='Hello Dash',
# #         style={
# #             'textAlign': 'center',
# #             'color': colors['text']
# #         }
# #     ),
# #
# #     html.Div(children='Dash: A web application framework for Python.', style={
# #         'textAlign': 'center',
# #         'color': colors['text']
# #     }),
# #
# #     dcc.Graph(
# #         id='example-graph-2',
# #         figure=fig
# #     )
# # ])
# #
# # if __name__ == '__main__':
# #     app.run_server(debug=True)
# ####################################################################################################################
#
#
#
#
#
#
#
# ####################################################################################################################
# # # -*- coding: utf-8 -*-
# #
# # # Run this app with `python dash_app.py` and
# # # visit http://127.0.0.1:8050/ in your web browser.
# #
# # import dash
# # import dash_core_components as dcc
# # import dash_html_components as html
# # import plotly.express as px
# # import pandas as pd
# #
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #
# # app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# #
# # # assume you have a "long-form" data frame
# # # see https://plotly.com/python/px-arguments/ for more options
# # df = pd.DataFrame({
# #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# #     "Amount": [4, 1, 2, 2, 4, 5],
# #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # })
# #
# # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# #
# # app.layout = html.Div(children=[
# #     html.H1(children="that's crazy"),
# #
# #     html.Div(children='''
# #         Dash: A web application framework for Python.
# #     '''),
# #
# #     dcc.Graph(
# #         id='example-graph',
# #         figure=fig
# #     )
# # ])
# #
# # if __name__ == '__main__':
# #     app.run_server(debug=True)
# ####################################################################################################################
