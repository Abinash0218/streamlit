import streamlit as st

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