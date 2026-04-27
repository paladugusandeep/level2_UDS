import streamlit as st

st.set_page_config(
    page_title="Streamlit App Demo",
    page_icon="🖼️",
    layout="centered"
)

#<h1>
st.title("Ultimate Data Science")

#subheader
st.subheader("Level 1")

#write
st.write("This is batch number 2 of ultimate data science bootcamp")

#Tabs

tab1, tab2,tab3=st.tabs(["Home","Dashboard","Settings"])

with tab1:
    st.write("Welcome to Home Tab !! ")
    # to create columns within home tab
    col1,col2,col3= st.columns(3)
    
    with col1:
        st.write("Left section of Home")
        st.button("Left",type="primary")
    with col2:
        st.write("Centre section of Home")
        st.button("Centre",type="secondary")
    with col3:
        st.write("Right section of Home")
        st.button("Right",type="tertiary")
with tab2:
    st.write("Welcome to Dashboard Tab !! ")
with tab3:
    st.write("Welcome to Settings Tab !! ")

st.divider()
st.subheader("Level 2")

with st.container(height=200, border=True):
    for i in range(100):
        st.write(f"Hello {i}")

st.divider()
st.subheader("Level 3 Widgets")
#Input Widgets
if st.button("Say Hello"):
    st.write("Hello There !!")

st.link_button("Streamlit widgets redirect",url="https://docs.streamlit.io/develop/api-reference/widgets")
name=st.text_input("Enter Name")