from PIL import Image
import streamlit as st
from streamlit_navigation_bar import st_navbar
from Pages import First
from Pages import Home
from Pages import Second
from Pages import Third
import os
import pandas as pd
import numpy as np

image = Image.open('./img/pingi.jpg')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "bomj.svg")
pages = [" ",'Home','First', 'Second', 'Third']

pages = ['Home', 'First', 'Second', 'Third']

styles = {
    "nav": {
        "background-color": "pink",
        "display":"flex",
        "justify-content" : "center"
    },
    "img" : {
        "position": "absolute",
        "left":"20px",
        "font-size":"15px",
        "top":"4px",
        "width":"100px",
        "height":"40px"
    },
    "div" : {
        "max-width":"32rem",
    },
    "span" : {
        "display":"block",
        "border-radius" : "0.5rem",
        "color":"white",
        "margin":"0 0.125rem",
        "padding" : "0.2rem 0.725rem",
    },
    "active" : {
        "color":"white",
        "font-weight":"normal",
        "padding":"14px"
    },
    "hover" : {
        "background-color": "wheat"
    }
}

options = {
    "show_menu":False,
    "show_sidebar":True,
}

page = st_navbar(pages, styles=styles,logo_path=logo_path,options=options )

if page == 'Home':
    Home.Home().app()
elif page == 'First':
    First.First().app()
elif page == 'Second':
    Second.Second().app()
elif page == 'Third':
    Third.Third().app()
else:
    Home.Home().app()

