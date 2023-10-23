import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



#miniing data
df = pd.read_csv('data.csv')
st.title('Data Analysis')

col1, col2, col3 =st.columns(3)
col1.metric('Year','$8765','$3467')
col2.metric('India', '$42561')

#df1=df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'], axis='columns')
#st.write(df, height=300, width=500)
#st.map(df1)

st.sidebar.button('hello')
   
    
if st.sidebar.button('load description'):
    st.write(df.describe())

if st.sidebar.button('load bar chart'):
    df2=df.head(20)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df2['Product'],df2['Qty'])
    st.pyplot(fig) 