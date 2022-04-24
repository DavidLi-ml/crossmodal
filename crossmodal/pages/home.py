

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def app():
    local_css("style/style.css")
    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_zzytykf2.json")
    img_sphere = Image.open("images/sphere.jpg")
    img_phase_separation = Image.open("images/phase_separation.jpg")
    img_nano = Image.open("images/nano.jpg")
    image_cqupt = Image.open("images/cqupt.jpeg")


    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("重庆邮电大学智能媒体传输小组")
        st.title("Brief Introduction")
        st.write(
            """
            This presentation is mainly used for a mini demonstration of cross-modality retrieval algorithm.
            The codes and ideas are made by students from the Ubiquitous sensing and networking team.
            By no purposes this will be used in any other forms.
            """
        )
        

 # ---- WHO I AM ----
    with st.container():
        st.write("---")

        st.header("Who I AM")
        st.write("##")
        st.write(
                """
                - Name: LiJiaLun
                - Instructor: LiZhidu
                """
            )
    # ---- WHAT I DO ----
    with st.container():
        st.write("---")

        st.header("What I do")
        st.write("##")
        st.write(
                """
                Currently working on:
                - Multimodality.
                - Natural Language Processing.
                - Python & C++.

                """
            )
    with st.container():
        st.write("---")
        st.subheader('Major Model Structure')
        st.image('images/05.png')
    with st.container():
        st.write("---")
        st.subheader('Dataset Introduction')
        st.image('images/08.png')
    with st.container():
        st.write("---")
        st.subheader('Algorithm Coding using Matlab')
        st.image('images/16.png')
        


    
