'''
Description: 
Author: lunyang
Github: 
Date: 2022-02-02 16:00:26
LastEditors: lunyang
LastEditTime: 2022-02-02 17:34:55
'''
import streamlit as st 
import numpy as np 

def app():
    st.write("""
            This is a very small demo with small dataset.
            Our purspose is just to show how cross-modality in real life can do.
            """)

    pattern_name = st.sidebar.selectbox(
        'Mini Demo',
        ('Image2Text', 'Text2Image')
    )

    st.write(f"## {pattern_name} Retrieval")
    if pattern_name == 'Text2Image':
        with st.form(key="my_form"):
            st.write("example: A girl is playing a piano/My father is playing football")
            doc = st.text_area(
                    "Input your sentence below (max 10 words and only for English), key words might be sing,read,play piano and so on",
                    height=100,
                )
            MAX_WORDS = 20
            import re
            res = len(re.findall(r"\w+", doc))
            if res > MAX_WORDS:
                st.warning(
                    "Your text contains"
                    + str(res) + " words."   + " Only the first 20 words will be reviewed. Stay tuned as increased allowance is coming! "
                    )
           
            submit_button = st.form_submit_button(label="retrieve")

            if submit_button:
                sentences = re.sub("[.,!?]", '', doc.lower()).split() # filter '.', ',', '?', '!'
                #st.write(sentences)
                #subject check
                who = 0
                for word in sentences:
                    if word == 'man' or word == 'boy' or word == 'he' or word == 'guy' or word == 'men' or word == 'boys' or word == 'guys'\
                        or word == 'father' or word =='brother' or word == 'brothers' or word == 'grandfather' or word == 'son':
                        who = 1
                    elif word == 'woman' or word == 'girl' or word == 'she' or word == 'lady' or word == 'girls' or word == 'ladies' \
                        or word == 'mother' or word == 'sister' or word == 'sisters' or word == 'grandmother' or word == 'daughter':
                        who = 2
                #object check
                st.write(who)
                for word in sentences:
                    if word == 'piano' or word == 'pianos':
                        if who ==1:
                            st.image('images/manplayingpiano.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanplayingpiano.jpg')
                            break
                        else:
                            st.image('images/piano.jpg')
                            break
                    if word == 'football' or word == 'soccer':
                        if who ==1:
                            st.image('images/manplayingfootball.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanplayingfootball.jpg')
                            break
                        else:
                            st.image('images/football.jpg')
                            break
                    if word == 'horse' or word == 'horses':
                        if who ==1:
                            st.image('images/manridinghorse.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanridinghorse.jpg')
                            break
                        else:
                            st.image('images/horse.jpg')
                            break
                    if word == 'reading' or word == 'readings' or word == 'read':
                        if who ==1:
                            st.image('images/manplayingreading.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanplayingreading.jpg')
                            break
                        else:
                            st.image('images/reading.jpg')
                            break
                    if word == 'basketball':
                        if who ==1:
                            st.image('images/manplayingbas.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanplayingbas.jpg')
                            break
                        else:
                            st.image('images/bas.jpg')
                            break
                    if word == 'singing' or word == 'singings' or word == 'sing' or word == 'singed':
                        if who ==1:
                            st.image('images/manplayingsinging.jpg')
                            break
                        elif who ==2:
                            st.image('images/womanplayingsinging.jpg')
                            break
                        else:
                            st.image('images/singing.jpg')
    if pattern_name == 'Image2Text':
        option = st.selectbox(
            'Please choose a sample image',
            (i for i in range(1,15)))
        with st.form(key="my_form"):
            submit_button = st.form_submit_button(label="retrieve")
            if option == 1:
                st.image('images2/cat.jpg')
            if option == 2:
                st.image('images2/dog.jpg')
            if option == 3:
                st.image('images2/tiger.jpg')
            if option == 4:
                st.image('images2/lion.jpg')
            if option == 5:
                st.image('images2/hema.jpg')
            if option == 6:
                st.image('images2/bird.jpg')
            if option == 7:
                st.image('images2/dog.jpg')
            if option == 8:
                st.image('images2/tiger.jpg')
            if option == 9:
                st.image('images2/elephant.jpg')
            if option == 10:
                st.image('images2/hema.jpg')
            if option == 11:
                st.image('images2/bird.jpg')
            if option == 12:
                st.image('images2/tiger.jpg')
            if option == 13:
                st.image('images2/lion.jpg')
            if option == 14:
                st.image('images2/hema.jpg')
            if option == 15:
                st.image('images2/bird.jpg')
            
            if submit_button:
                if option == 1:
                    st.write('a cat is playing a little ball')
                if option == 2:
                    st.write('a dog is playing with a cat')
                if option == 3:
                    st.write('tigers are going to cross the river')
                if option == 4:
                    st.write('the lion is at rest')
                if option == 5:
                    st.write('the hippo is drinking water')
                if option == 6:
                    st.write('the bird is standing on the branch')
                if option == 7:
                    st.write('a dog is playing with a cat')
                if option == 8:
                    st.write('tigers are going to cross the river')
                if option == 9:
                    st.write('the elephant is running')
                if option == 10:
                    st.write('the hippo is drinking water')
                if option == 11:
                    st.write('the bird is standing on the branch')
                if option == 12:
                    st.write('tigers are going to cross the river')
                if option == 13:
                    st.write('the lion is at rest')
                if option == 14:
                    st.write('the hippo is drinking water')
                if option == 15:
                    st.write('the bird is standing on the branch')

    algorithm_name = st.sidebar.selectbox(
         'Algorithm',
         ('CMCP', 'HSNN', 'JGRHML')
    )

   
