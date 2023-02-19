import pandas as pd  
import streamlit as st
# import plotly.express as px
from chart_studio import plotly
import plotly.express as px
from PIL import Image


st.set_page_config(page_title=' Sentiment Results')
st.header('Results') 

# header.update_traces(header_font_color='yellow', selector=dict(type='table'))


st.subheader('Sentiment Analysis of scrapped data and tweets using TextBlob')

excel_file = 'TextBlob_results.csv'
sheet_name = 'DATA'

df = pd.read_csv(excel_file)

st.dataframe(df)


#plot line graph between polarity and subectivity from df
fig = px.line(df,'polarity', 'subjectivity', title='Polarity vs Subjectivity of Text scrapped')
##give color to the line
fig.update_traces(mode='lines+markers', line_color='rgb(159, 43, 104)')
##give color to the markers
fig.update_traces(marker_color='blue')
##give color to the title
fig.update_layout(title_x=0, title_font_color='red')
##give color to the x-axis
fig.update_xaxes(title_text='POLARITY', title_font_color='white')
##give color to the y-axis
fig.update_yaxes(title_text='SUBJECTIVITY', title_font_color='white ')
##give color to the background
fig.update_layout(plot_bgcolor='black')
##give color to the grid
##give color to the legend
fig.update_layout(legend_title_text='Legend', legend_title_font_color='rgb(159, 43, 104)')
##give color to the tick labels
# fig.update_xaxes(tickfont_color='red')
# fig.update_yaxes(tickfont_color='red')
st.plotly_chart(fig)

# /////

st.subheader('Sentiment Analysis of scrapped data and tweets using Vadar')
# with open('VADAR_results.csv', 'r') as textfile:
#     for row in reversed(list(csv.reader(textfile))):
#         print(row)

#display the data from the csv file in reverser order
df_vader = pd.read_csv('VADAR_results.csv')
st.dataframe(df_vader)




a=df_vader['Sentiment'].value_counts()

negative=a[0]
neutral=a[1]
positive=a[2]
d={'Sentiment':['Negative','Neutral','Positive'],'Count':[negative,neutral,positive]}
#plot d
df_plot=pd.DataFrame(d)
fig = px.line(df_plot, x='Sentiment', y='Count', title='Sentiment Analysis of scrapped data and tweets using Vadar')
##give color to the line
fig.update_traces(mode='lines+markers', line_color='rgb(159, 43, 104)')
##give color to the markers
fig.update_traces(marker_color='blue')
##give color to the title
fig.update_layout(title_x=0, title_font_color='red')
##give color to the x-axis
fig.update_xaxes(title_text='SENTIMENTS', title_font_color='white')
##give color to the y-axis
fig.update_yaxes(title_text='TEXT COUNTS', title_font_color='white ')
##give color to the background
fig.update_layout(plot_bgcolor='black')
##give color to the grid
##give color to the legend
fig.update_layout(legend_title_text='Legend', legend_title_font_color='rgb(159, 43, 104)')
##give color to the tick labels
# fig.update_xaxes(tickfont_color='red')
# fig.update_yaxes(tickfont_color='red')

st.plotly_chart(fig)





