####################################################################################################################
# eat_app.py
#
# Energy Automation Team's first streamlit app



####################################################################################################################
# IMPORTS
from eatlib import * # import eatlib - the only library you'll ever need



####################################################################################################################
# SCRIPT

# do some housekeeping and create some variables
example_data_path = './example data/'
logo = './images/EAT LOGO_COLOR.png'
st.image(logo,width=None)
df=[]
fig = go.Figure()

# use triple quotes instead of st.write() for multiline printing using Markdown syntax (https://www.markdownguide.org/cheat-sheet/)
"""
`This is an experimental app in development by the P2S Energy Automation Team. If you run into any issues/bugs/errors, please use the "Report a bug with this app" tool in the drop down menu in the top right corner of this page. Thanks for playing!`

# Trend Data Visualization App
### Upload a .csv file with timestamps in the first column and trend data in the remaining columns. 
"""
uploaded_file = st.file_uploader("Choose a file")

if st.button('See example'):
    df = pd.read_csv(example_data_path + random.choice(os.listdir(example_data_path)))  # pick a random file from ./example_data/
    if df.columns[0] == 'Unnamed: 0':
        df.drop(df.columns[0], axis=1, inplace=True) # !!! drop the first column of data so timestamps are in column
    print('calling plot_time function...')
    fig = plot_time(df)
    st.subheader('Data (example):')
    st.dataframe(df)
    """
    ###Point Trends (example):
    
    Click on point names in the legend to make them visible.
    
    Pan and zoom with your mouse to get a closer look at the data. Double click inside the graph to reset the axes.
    """
    st.plotly_chart(fig, use_container_width=True)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.columns[0] == 'Unnamed: 0':
        df.drop(df.columns[0], axis=1, inplace=True) # !!! drop the first column of data so timestamps are in column
    print('calling plot_time function...')
    fig = plot_time(df)
    st.subheader('Data:')
    st.dataframe(df)
    """
    ### Point Trends
    
    Click on point names in the legend to make them visible.
    
    Pan and zoom with your mouse to get a closer look at the data. Double click inside the graph to reset the axes.
    """
    st.plotly_chart(fig, use_container_width=True)
