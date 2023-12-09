import streamlit as st
import base64
from utils import *

st.set_page_config(page_title='SemaAfya', page_icon='🏥')

header_html = "<div style='text-align: left;'><img src='data:image/png;base64,{}' class='img-fluid' style='max-width: 700px;'></div>".format(
    img_to_bytes("Logo.png")
)

st.markdown(
    header_html, unsafe_allow_html=True,
)
st.caption("Kuhifadhi afya yako ni ahadi yetu kuu.")
#st.markdown("---") 

#st.title("Kuhusu")
#st.subheader("Kuhusu SemaAfya")
#st.title("Kuhusu SemaAfya")

   
tip_to_display="""

Karibu SemaAfya, jukwaa lako la huduma za afya mtandaoni! Kauli mbinu yetu : **``Kuhifadhi afya yako ni ahadi yetu kuu``**


**Dhamira Yetu**
Tunaamini kila mtu anastahili huduma bora za afya bila kujali eneo, lugha, au vizuizi vya upatikanaji. SemaAfya inajitolea kuondoa changamoto za kiafya kwa kutoa suluhisho lenye ubunifu na la haraka.

**Jukwaa la Tiba Mbali**
SemaAfya ni zaidi ya jukwaa la matibabu; ni mshirika wako wa kuaminika kwa maswala yote ya afya. Tunachanganya teknolojia mpya kama Mifano ya Kujifunza ya Lugha ya Asili (LLMS) na Mifumo ya Kutambulika kwa Kauli (ASR) na Kumbukumbu za Kielektroniki (EHRs) ili kutoa huduma bora za tiba.

**Kwa Nini SemaAfya?**
- Upatikanaji wa Haraka: Huduma za afya mara moja, popote pale ulipo.
- Mawasiliano kwa Sauti: Tueleze dalili zako kwa sauti, hata bila ujuzi wa kitaalamu.
- Usalama na Urahisi: Tunapunguza vizuizi vyote kwa kutoa huduma za afya bila kikwazo.

**Jinsi Tunavyosaidia**
Tunakabiliana na changamoto za kumbukumbu za elektroniki na kutambulika kwa sauti, tukiongeza kasi ya upatikanaji wa habari za matibabu. Hii inaweza kuleta mapinduzi katika jinsi unavyoshughulikia afya yako.

**Ungana Nasi Leo**
Chagua SemaAfya kwa huduma za afya zenye ubunifu, zinazopatikana, na zinazojali. Ungana nasi leo na uanze safari yako kuelekea afya bora!"""
st.markdown(f"""
<div style="border:2px solid #F0F2F6; padding:20px; border-radius:5px; box-shadow: 2px 2px 12px #aaa;">
    {tip_to_display}
</div>
""", unsafe_allow_html=True)


local_css("style/style.css")

#with st.expander('Maagizo'):
    #st.markdown(
                #'''     
                    #"Kuhifadhi afya yako ni ahadi yetu kuu"
                    #- Bonyeza kwenye kitufe cha Anza ili kuanza kusikiliza
                    #- Bonyeza kwenye kitufe cha Acha ili kuacha kusikiliza
                    #- Bonyeza kwenye kitufe cha ** Pakua Transkripti** ili kupakua transkripti
                    #*Angalia*: Transkripti inapakuliwa katika saraka ile ile na programu
                    #*Angalia*: Programu bado ipo kwenye maendeleo na inaweza isifanye kazi kama ilivyotarajiwa
                #'''
               # )
# streamlit run 🤖_Kuhusu.py
# pip freeze > requirements.txt
#pip install base64 io jsonlib openai requests numpy streamlit pydub audiorecorder pytz pyaudio google-cloud-firestore googletrans transformers readtime pandas gtts
# pip install pipreqs
# pipreqs --encoding=utf8

