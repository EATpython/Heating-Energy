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

st.image(logo,width=5)
st.title('Trend Data Visualization')

uploaded_file = st.file_uploader("Choose a file")
df=[]
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.drop(df.columns[0], axis=1, inplace=True) # !!! drop the first column of data so timestamps are in column
    print('calling plot_time function...')
    fig = plot_time(df)
    st.dataframe(df)
    st.plotly_chart(fig, use_container_width=True)
# else:
#     filepath_in = './DataCleaner Output Files/' # use output files from JH_CSV_DataCleaner
#     file_name = '2019 CHP Raw Trend_OUT_Clean_Data' #name of the file w/o .csv suffix (used to conveniently name plots, but maybe not robust)
#     df = pd.read_csv(filepath_in + file_name + '.csv') # read data into a DataFrame and print some info
#     print('\nDATA READ SUCCESSFULLY...\n')
#     print(df)



# call a function from eatlib to plot the data

# fig.write_html(filepath_out + file_name + '_Plot.html')   # write the plot to html so it's shareable
# fig.show()

