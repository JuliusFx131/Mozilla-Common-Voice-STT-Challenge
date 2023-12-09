import streamlit as st
from utils import*

# Header with logo
header_html = "<div style='text-align: left;'><img src='data:image/png;base64,{}' class='img-fluid' style='max-width: 700px;'></div>".format(
    img_to_bytes("Logo.png")
)
st.markdown(header_html, unsafe_allow_html=True)

# Title and introduction
#st.title('Ingia kwenye SemaAfya')
st.write('Tafadhali ingia ili kuendelea na huduma zetu.')

# Sign-in form
#st.write("Weka taarifa zako za kuingia:")
email = st.text_input('Barua pepe')
password = st.text_input('Nenosiri', type='password')

if st.button('Ingia 🔐'):
    # Handle sign-in logic here (you can authenticate using your backend or Firebase)
    st.success('Umefanikiwa kuingia! Karibu tena.')

# streamlit run 🔐_ingia_SemaAfya.py