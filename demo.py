import streamlit as st

st.title("Hello streamlit")
st.header("Header")
st.subheader("SubHeader")
st.text("Pre formatted text. Can't change the style of this text")

st.markdown("""
    # header 1
    ## header 2
    ### header 3
            
    :sunglasses: 
    :moon:
""")