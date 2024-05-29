# Import Libraries
import streamlit as st
# streamlit is a library that allows you to bild a POC(PROOF OF CONCEPT) simple application very quickly
# To run streamlit " streamlit run [file.py] "
import Langchain_Helper

# Set Application Title
st.title("Restaurant Name Generator")

# Text Input in Sidebar
cuisine_text = st.sidebar.text_input("Enter a Cuisine", " ")

st.sidebar.write("OR") # for user search

# Select Box in Sidebar
select_cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "Thai", "Chinese"))


if cuisine_text:
    # User selects from Select Box
    response = Langchain_Helper.generator_restaurant_name_and_fooditems(cuisine_text)  # Langchain_Helper
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.header("***Menu Items***")
    for items in menu_items:
        st.write(items)
elif select_cuisine:
    # User input text
    response = Langchain_Helper.generator_restaurant_name_and_fooditems(select_cuisine) # Langchain_Helper
    st.header(response['restaurant_name'].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.header("***Menu Items***")
    for items in menu_items:
        st.write(items)
