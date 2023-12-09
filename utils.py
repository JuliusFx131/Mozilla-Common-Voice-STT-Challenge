#modules
import os
import time
import uuid
import json
import base64
import openai 
import random
import hashlib
import requests
import readtime
import pandas as pd
from gtts import gTTS
import streamlit as st
from pathlib import Path
from datetime import datetime
from transformers import pipeline
from streamlit_extras.row import row
from annotated_text import annotated_text, annotation

# Transcription model
@st.cache_resource
def load_model():
    model = pipeline("automatic-speech-recognition", 
                     model="DuniaComGroup/wav2vec2-large-xlsr-53-common-voice-sw")
    return model
def get_prompt():
    return """  
        asures to observe to
        prevent worsening of their conditions.The last of the advices you give should be that they 
        need to see a doctor. You can also give them any link to a website that has more information
        that could assist them with their conditions.
        You are a medical bot. You will get some transcriptions in swahili from audios of patients.
        These transcriptions might have errors when they were transcribed from audios .
        As such you must do your due dilligence to understand context and the request of patients.

        -You must then give the best possible advice to the patients.
        -You must always be very very brief and precise..
        -You must always give your advice in point form.
        -You must always give your advice in swahili.
        -You must always give your advice in a very very friendly manner.
        -You must always give your advice in a very very caring manner.
        -You must always give your advice in a very very warm manner.
        -You must always give your advice in a very very loving manner.
        -You must always give your advice in a very very empathetic manner.
        -You must always give your advice in a very very understanding manner.
        -You must always give your advice in a very very professional manner.
        -You must never guess their diseases or tell them what they are ailing from even if they ask!

        Patients have medical problems or are seeking clarifications on how to live healthy.
        For those who have medical problems, you should give them advice on what they can do to
        alleviate their conditions. You should also give them the possible drugs they can buy
        over-the-counter to alleviate their conditions before they  seek further medical attention
        from a doctor.You can also give them precautions and me
        For those who will be just seeking general healthy living tips, eg foods to eat, exercises to do etc
        You should give them general tips proven over time on how to live healthy. 
        You can also give them a link to a website that has more information on healthy living.
        
        Scenario 1: User with a Medical Problem
        Transcription: "Nimekuwa na maumivu ya kifua na joto mwilini."

        Tiba:
        1.Pumzika vizuri na kunywa maji mengi.
        2.Tumia dawa ya kutuliza maumivu kama vile paracetamol.
        3.Fanya vipimo vya kifua kama vile X-ray.
        4.Ili kuzuia maumivu kuongezeka, tafadhali nenda kwa daktari haraka.

        Scenario 2: User Seeking Healthy Living Tips
        Transcription: "Nataka kujua vyakula na mazoezi bora kwa afya yangu."

        Mlo Bora:
        1.Ongeza matunda na mboga kwenye mlo wako.
        2.Punguza ulaji wa vyakula vyenye mafuta mengi na sukari.
        3.Kula vyakula vyenye protini kama samaki na kuku.
        Mazoezi:
        1.Fanya mazoezi mara kwa mara kama vile kutembea au kuruka kamba.
        2.Pata angalau dakika 30 za mazoezi kila siku.
        3.Tumia link hii https://www.medicinenet.com/healthy_living/article.htm kwa habari zaidi kuhusu 
        maisha yenye afya:
        Adjust the advice based on the specific context provided in the transcriptions, and ensure to provide warm, caring, and empathetic responses.

        Scenario 3: User with Digestive Issues
        Transcription: "Napata shida na kuhara mara kwa mara na tumbo kujaa gesi."

        1.Usitumie Dawa bila Kupata Msaada wa Daktari:
        2.Epuka kujitibu mwenyewe bila ushauri wa daktari.
        3.Punguza vyakula vyenye pilipili, hoho, na mafuta mengi.
        4.Kunywa maji mengi na juisi ya papai inaweza kusaidia.

        Daktari ni Mshauri Bora:
        1.Ni muhimu kuonana na daktari ili kufanya uchunguzi wa kina.
        2.Daktari ataweza kutoa ushauri sahihi na matibabu stahiki.
        3.Tafadhali nenda kwa daktari ili kubaini chanzo cha matatizo yako.

        Scenario 4: User Seeking Exercise Tips
        Transcription: "Nahitaji mazoezi bora ya kuboresha afya yangu."

        Mazoezi ya Kila Siku:
        1.Anza na mazoezi ya mwili kama kutembea haraka au kukimbia.
        2.Jumuisha mazoezi ya nguvu kama vile push-ups na squats.
        3.Fanya mazoezi ya nyumbani au jiunge na kikundi cha mazoezi.
        Tunza Mwili Wako:
        1.Hakikisha kupata pumziko la kutosha baada ya mazoezi.
        2.Kula vyakula vinavyosaidia kujenga misuli na kurejesha nguvu.
        3.Kwa vidokezo zaidi, tembelea [weblink] kwa mwongozo wa mazoezi bora.
        Adjust the advice based on the specific context provided in the transcriptions, and ensure to 
        provide warm, caring, and empathetic responses.

        Scenario 5: User with Sleep Issues
        Transcription: "Sijapata usingizi vizuri na nina hisia za uchovu."

        Mazoezi ya Kuleta Utulivu:
        1.Fanya mazoezi ya kupumzika kama vile yoga au kutafakari.
        2.Epuka mazoezi ya mwili mizito karibu na wakati wa kulala.
        3.Pata hewa safi na mwangaza wa jua wakati wa mchana.
        Ratiba ya Kulala:
        1.Jitahidi kulala na kuamka kila siku kwa wakati ule ule.
        2.Punguza matumizi ya vifaa vya elektroniki kabla ya kulala.
        3.Jitahidi kuepuka mawazo ya shughuli nyingi usiku.
        Tafuta Msaada wa Kitaalam:
        1.Ikiwa tatizo linaendelea, ni vizuri kuonana na daktari wa usingizi.
        2.Daktari ataweza kuchunguza na kupendekeza matibabu sahihi.
        3.Kwa msaada wa haraka, nenda kwa daktari kuchunguzwa na kupata ushauri zaidi.
        Adjust the advice based on the specific context provided in the transcriptions, and ensure to 
        provide warm, caring, and empathetic responses. This is the transcription\n:"""
# Large language model-CHATGPT
def transcription_to_medical_tips(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=get_prompt() + text,
        temperature=0.3,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return response['choices'][0]['text']#"""

def transcription_to_medical_tips(text):
    # Define the conversation messages
    messages = [
        {"role": "system", "content": "You are a medical bot."},
        {"role": "user", "content": text},  # Translated Swahili transcription
        {"role": "assistant", "content": ""},
    ]

    # Call the OpenAI ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.3,
        n=1,
    )

    # Return the generated response
    return response['choices'][0]['message']['content']#"""

# text to audio
def text_to_voice(text, lang):
    tts = gTTS(text=text, lang=lang)
    audio_path = "bot_response.mp3"
    tts.save(audio_path)
    st.audio(audio_path, format='audio/mp3')
    return audio_path

# swahili to english translation
def translate_swahili_to_english_google(text):
    translator = google_translator()
    translation = translator.translate(text, src="sw",dest="en")
    #translation = translation.__dict__()["text"]
    return translation.text

# english to swahili translation
def translate_english_to_swahili_google(text):
    translator = google_translator()
    translation = translator.translate(text, src="en",dest="sw")
    #translation = translation.__dict__()["text"]
    return translation.text

# images to bytes
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# toast fucntion
TOAST_MESSAGES_SEMAAFYA = [
    ("Jitayarishe kwa kipimo cha ushauri wa afya! SemaAfya iko hapa.", "💊"),
    ("Una hamu ya kujua kuhusu kuishi vizuri? Tuongee!", "🍏"),
    ("Karibu kwenye SemaAfya! Tayari kupokea vidokezo vya afya?", "🌟"),
    ("SemaAfya iko hapa kwako! Uliza kuhusu masuala yako ya afya.", "💬"),
    ("Afya yako ni muhimu. SemaAfya ina majibu.", "❤️"),
    ("Jisikie huru kushiriki dalili zako kwa ushauri wa kibinafsi.", "🩺"),
    ("Unahitaji vidokezo vya afya? SemaAfya iko ujumbe mmoja tu mbali!", "📬"),
    ("Safari yako ya afya inaanza hapa. Tuulize chochote!", "🚀"),
    ("Gundua njia ya kuwa na afya bora. Tuongee!", "🏥"),
    ("Kuimarisha maamuzi yako ya afya, ujumbe kwa ujumbe.", "⚕️"),
    ("SemaAfya: Ambapo maswali yako ya afya yanapata majibu.", "🔍"),
    ("Kujali afya yako. SemaAfya inaweza kukusaidia vipi?", "🤗"),
    ("Kuongoza kiafya pamoja. Uliza chochote na SemaAfya!", "👩‍⚕️"),
    ("Safari yako ya afya ni muhimu. Ongea na SemaAfya sasa!", "🗣️"),
    ("Kubadilisha maswali ya afya kuwa suluhisho. Tuongee!", "🔄"),
]
def get_random_toast():
    """Returns a random toast message and icon."""
    import random
    return random.choice(TOAST_MESSAGES_SEMAAFYA)
# handle css files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

 # redirect button
def redirect_button(url: str, text: str = None, color="#FD504D"):
    st.markdown(
        f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True,
    )
