import streamlit as st
import requests
from streamlit_lottie import st_lottie


class Home:
    def __init__(self):
        pass

    def app(self):
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        # create lottie_anim1 and give it json url
        lottie_anim1 = load_lottieurl("https://lottie.host/c000f660-7b78-4b1f-b18c-5317da504732/bkc8emLuDH.json")

        # Create two columns
        left_column, right_column = st.columns([5, 3])

        # left column for intro
        with left_column:
            st.title("Aya's streamlit")
            st.write("---")
            st.write(
                """
                Hi everyone, and that's my project with streamlit framework!! 
                Using my website you can see three graphs which can answers on a questions about
                2018 ticket sales and also it is my ISTA131 project, so thanks for visit!!
                It is really important to mention libraries which was used here:

                - Pandas
                - Matplotlib
                - Numpy

                As well as auxiliary required libraries(Frameworks):

                - Streamlit
                """
            )
            st.write("---")
            st.subheader("A bit abt me")
            st.write(
                """
                Oh hi!!! How are you? I am always fine and hope that you too!!
                Ooh yeah, Happy New Year, Merry Christmas, Have a nice day, or
                Have a good evening!!!
                BYE!!!
                """
            )


        # right column for video player and animation
        with right_column:
            #add lottie_anim1
            if lottie_anim1:
                st_lottie(lottie_anim1, height=300, key="coding")

        # styles part
        st.markdown(
            """
            <style>
            h1 {
                color: pink;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )