import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Bio_data_form"]
collection = db["users"]

# Page Title
st.title("📋 Bio Details Form")

# Form
name    = st.text_input("Full Name")
age     = st.number_input("Age", min_value=1, max_value=120, step=1)
email   = st.text_input("Email")
phone   = st.text_input("Phone Number")
city    = st.text_input("City")
gender  = st.selectbox("Gender", ["Male", "Female", "Other"])
about   = st.text_area("About You")

# Submit Button
if st.button("Submit"):
    if not name or not email:
        st.error("Name and Email are required!")
    else:
        record = {
            "name":   name,
            "age":    age,
            "email":  email,
            "phone":  phone,
            "city":   city,
            "gender": gender,
            "about":  about
        }
        collection.insert_one(record)
        st.success(f"✅ {name}'s details saved successfully!")