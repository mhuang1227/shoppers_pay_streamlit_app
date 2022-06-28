# streamlit_app.py

import streamlit as st
import snowflake.connector 

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()
modelTraining = st.container()

with siteHeader:
    st.title('Welcome to the Awesome project!')
st.text('In this project I look into')

with dataExploration:
    st.header('Dataset: Iris flower dataset')
    st.text('I found this dataset at')

with newFeatures:
    st.header('New features I came up with')
    st.text('Let\'s take a look into the features I generated.')

with modelTraining:
    st.header('Model training')
    st.text('In this section you can selectthe hyperparameters!')