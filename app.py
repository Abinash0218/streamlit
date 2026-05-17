import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="My first app"
)

# title and text
st.title("Streamlit complete app")
st.header("This is header")
st.subheader("This is subheader")
st.text("This is simple text")
st.markdown("**Markdown support** with _formating_")
st.write({"key":"value"})

# sidebar
st.sidebar.title("This is sidebar")
name=st.sidebar.text_input("Enter your name")
age=st.sidebar.slider("Select your age",10,60,30)
st.sidebar.write(f"Hello my name is {name} and my age is {age}")

# input widgets
text=st.text_input("Enter a text")
number=st.number_input("Number input",min_value=0,max_value=100)
password=st.text_input("Password",type='password')
date=st.date_input("Select date")
time=st.time_input("Select time")

checkbox=st.checkbox("Check")
radio=st.radio("Select one",["Option A","Option B","Option C"])
select=st.selectbox("Select box",["Python","Java","C++"])
muliselect=st.multiselect("Multi select",["HTML","CSS","JS"])

if st.button("Click me"):
    st.success("Button clicked")

st.header("Form")
with st.form("My_form"):
    username=st.text_input("username")
    email=st.text_input("Email")
    comment=st.text_area("comment....")
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.success(f"Submitted: {username}, {email}, {comment}")

st.header("Data")
df=pd.DataFrame({
    "A":np.random.randn(10),
    "B":np.random.randn(10)
})
st.dataframe(df)
st.table(df.head())

st.header("Charts")
st.line_chart(df)
st.bar_chart(df)

fig,ax=plt.subplots()
ax.plot(df["A"])
ax.set_title("Matplotlib_plot")
st.pyplot(fig)

fig,ax=plt.subplots()
ax.plot(df["B"])
ax.set_title("Matplotlib_plot")
st.pyplot(fig)

st.header("File Upload")
uploaded_file=st.file_uploader("upload CSV",type=["csv"])
if uploaded_file:
    data=pd.read_csv(uploaded_file)
    st.write(data)

col1,col2,col3,col4=st.columns(4)
with col1:
    st.info("Column 1")
    st.button("Button 1")

with col2:
    st.warning("Column 2")
    st.button("Button 2")

with col3:
    st.info("Column 3")
    st.button("Button 3")

with col4:
    st.error("Column 4")
    st.button("Button 4")


st.header("Expander")
with st.expander("Click to expand"):
    st.write("Hidden content here")

# st.header("Progress")
# progress=st.progress(0)
# for i in range(100):
#     time.sleep(0.01)
#     progress.progress(i+1)
# with st.spinner("Loading..."):
#     time.sleep(2)
# st.success("Done")


st.header("Session state")
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("Increment"):
    st.session_state.count+=1
if st.button("Decrement"):
    st.session_state.count-=1
st.write("Count:",st.session_state.count)


st.header("Cache")
@st.cache_data
def load_data():
    time.sleep(2)
    return pd.DataFrame(np.random.randn(100,3),columns=["A","B","C"])
if st.button("Load cached data"):
    data=load_data()
    st.write(data)


st.header("Metrices")
st.metric("Revenue","10000","+5%")
st.metric("Users","1500","-2%")

st.header("Alerts")
st.success("Success Message")
st.error("Error Message")
st.warning("Warning Message")
st.info("Info Message")