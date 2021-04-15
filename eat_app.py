####################################################################################################################
# eat_app.py
#
# Energy Automation Team's first streamlit app


####################################################################################################################
# IMPORTS
from eatlib import *  # import eatlib - the only library you'll ever need

####################################################################################################################
# SCRIPT

# do some housekeeping and create some variables
st.set_page_config(layout="wide")
example_data_path = './example data/'
logo = './images/EAT LOGO_COLOR.png'
df = []
fig = go.Figure()

# start printing stuff to the page, starting with a logo
st.image(logo, width=None)

# use triple quotes instead of st.write() for multiline printing using Markdown syntax
# (https://www.markdownguide.org/cheat-sheet/)
"""`Welcome to the party! This is an experimental app being developed by the P2S Energy Automation Team. If you run 
into any bugs/errors or have suggestions for additional features/functionality, please use the "Report a bug with 
this app" tool in the drop down menu in the top right corner of this page. Thanks for playing!` 

# Trend Data Visualization App

Quickly visualize lots of trend data to gain engineering insights and make nice-looking graphs to include in 
reports/presentations. 

To get started, upload a .csv file with timestamps in the first column and trend data in the remaining columns - or 
click "See example"."""

uploaded_file = st.file_uploader("Choose a file")

if st.button('See example'):
    df = pd.read_csv(example_data_path + random.choice(os.listdir(example_data_path)))  # pick a random example file
    if df.columns[0] == 'Unnamed: 0':
        df.drop(df.columns[0], axis=1, inplace=True)  # !!! drop the first column of data so timestamps are in column
    fig = plot_time(df)

    """
    ### Raw Data (example):

    Uploaded file should be in .csv format with timestamps in the first column and trend data in the remaining 
    columns. This app supports a variety of timestamp formats, but the format should be consistent for all timestamps 
    in the uploaded file. Trend data columns should have meaningful titles. For best practice, use *lowercase*, 
    *lowercase_with_underscores*, or *camelCase* 

    Click "See example" again to see a different example.
    """

    # this line displays the .csv file in table format, with the index column suppressed to avoid confusion
    st.dataframe(df.assign(drop_index='').set_index('drop_index'))

    """
    ### Point Trend Graph (example):
    
    Click on point names in the legend to make them visible.
    
    Pan and zoom with your mouse to get a closer look at the data. Double click inside the graph to reset the axes.
    
    You can download this graph as a .png by clicking the camera icon in the plot figure menu.
    """

    st.plotly_chart(fig, use_container_width=True)

# TODO: play around with structure and if/else statements so example data/plots and real data/plots replace each
#  other on the page instead of doubling up
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.columns[0] == 'Unnamed: 0':
        df.drop(df.columns[0], axis=1,
                inplace=True)  # !!! drop the first column of data so timestamps are in column - this is hardcoded to accomodate JH_CSV_DataCleaner.py outputs
    print('calling plot_time function...')
    fig = plot_time(df)
    """
    ### Raw Data:

    Uploaded file should be in .csv format with timestamps in the first column and trend data in the remaining 
    columns. This app supports a variety of timestamp formats, but the format should be consistent for all timestamps 
    in the uploaded file. Trend data columns should have meaningful titles. 

    Click "See example" again to see a different example, or upload a different file.
    """
    st.dataframe(df.assign(drop_index='').set_index(
        'drop_index'))  # this line displays the .csv file in table format, with the index column suppressed to avoid confusion
    """
    ### Point Trend Graph:
    
    Click on point names in the legend to make them visible.
    
    Pan and zoom with your mouse to get a closer look at the data. Double click inside the graph to reset the axes.
    
    You can download this graph as a .png by clicking the camera icon in the plot figure menu.
    """
    st.plotly_chart(fig, use_container_width=True)
