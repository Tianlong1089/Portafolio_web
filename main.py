import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.header("Tianlong1089")

col1, col2 = st.columns(2)

with col1:
    st.image("/home/tianlong55/Downloads/PyCharm_Projects/app2_portafolio/images/photo.png")

with col2:
    st.title("Carlos Carrera")
    content = """
    Hi, I am Carlos! I am a physicist, data scientist, programmer and teacher at UNAM. I graduated in 2023.
     I  worked as undergraduate researcher by ICN, UNAM developing algorithms and software solutions for optimazing 
     science experiments.  Now, I have moved in order to reach new areas out of the scientific researching and I am focused in 
     continue my job career as a full time programmer. 
      """
    st.info(content)

content_1="""
        Below you can find some of the apps I have built in Python, C and other stuff. Feel free to contact me !!
        """
st.text(content_1)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("/home/tianlong55/Downloads/PyCharm_Projects/app2_portafolio/data.csv",sep=";")
images_path = '/home/tianlong55/Downloads/PyCharm_Projects/app2_portafolio/images'

page = 'https://www.google.com'
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.text(row['description'])
        st.image(images_path+'/'+row['image'])
        st.write(f'[Source Code]({page})')
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.text(row['description'])
        st.image(images_path+'/'+row['image'])
        st.write(f'[Source Code]({page})')