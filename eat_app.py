####################################################################################################################
# eat_app.py
#
# Energy Automation Team's first streamlit app



####################################################################################################################
# IMPORTS
from eatlib import * # import eatlib - the only library you'll ever need



####################################################################################################################
# SCRIPT
logo = './images/EAT LOGO_COLOR.png'

st.image(logo,width=None)

"""
# Trend Data Visualization App
## Upload a .csv file with timestamps in the first column and trend data in the remaining columns. 
"""

uploaded_file = st.file_uploader("Choose a file")
df=[]

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.columns[0] == 'Unnamed: 0':
        df.drop(df.columns[0], axis=1, inplace=True) # !!! drop the first column of data so timestamps are in column
    print('calling plot_time function...')
    fig = plot_time(df)
    st.subheader('Data:')
    st.dataframe(df)
    st.subheader('Point Trends:')
    st.plotly_chart(fig, use_container_width=True)
