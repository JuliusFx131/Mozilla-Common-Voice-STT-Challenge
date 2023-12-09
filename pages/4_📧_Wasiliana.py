from utils import*
import streamlit as st

header_html = "<div style='text-align: left;'><img src='data:image/png;base64,{}' class='img-fluid' style='max-width: 700px;'></div>".format(
    img_to_bytes("Logo.png")
)
st.markdown(
    header_html, unsafe_allow_html=True,
)
#st.title('Wasiliana')
st.write('Sema maoni yako! Nijulishe unachofikiria kuhusu wazo la programu hii na vipengele vipi ungependa kuona katika siku zijazo.')

contact_form = """
<form action="https://formsubmit.co/ad1b4a421f4310ed3e5b4d6903c79b2c" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Jina lako" required>
     <input type="email" name="email" placeholder="barua pepe yako" required>
     <textarea name="message" placeholder="Ujumbe wako" required></textarea>
     <button type="submit">Tuma</button>
</form>
"""
#<input type="tel" name="tel" placeholder="nambari ya simu" required>

st.markdown(contact_form, unsafe_allow_html=True)

st.sidebar.write("Made with ♥ by JuliusFx, Nairobi Kenya")
#st.sidebar.subheader("🔗 Wasiliana nami kupitia", anchor=False)
st.sidebar.write("🔗 Wasiliana nami kupitia", anchor=False)
st.sidebar.markdown(
    """
    - [🐙 Github](https://github.com/JuliusFx131)
    - [🎥 YouTube Channel](https://www.youtube.com/channel/UCHZF36W9SxemUXuygvd-ouw)
    - [🌐 Personal Website](https://juliusfx131.github.io/DataAnalystJulius/)
    - [👔 LinkedIn](https://www.linkedin.com/in/julius-mwangi-9742b7125/)
    - [☕ Ninunulie Kahawa](https://ko-fi.com/juliusfx)
    """
)

local_css("style/style.css")