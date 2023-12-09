import streamlit as st
from utils import*

# Header with logo
header_html = "<div style='text-align: left;'><img src='data:image/png;base64,{}' class='img-fluid' style='max-width: 700px;'></div>".format(
    img_to_bytes("Logo.png")
)
st.markdown(header_html, unsafe_allow_html=True)

# Title and introduction
#st.title('Jiunge na SemaAfya')
st.write('Jisajili ili kupata huduma bora zaidi!')

# Sign-up form
#st.write("Jaza taarifa zako:")
email = st.text_input('Barua pepe')
password = st.text_input('Nenosiri', type='password')
username = st.text_input('Jina la mtumiaji')
# You can add more fields as needed

if st.button('Jisajili'):
    # Handle form submission here (you can send data to your backend or Firebase)
    st.success(f'Umesajiliwa kwa mafanikio, {username}!')

