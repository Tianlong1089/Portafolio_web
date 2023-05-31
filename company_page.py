import streamlit as st
import pandas as pd

df=pd.read_csv('/home/tianlong55/Downloads/PyCharm_Projects/app2_portafolio/data_company.csv')

st.header("Company A. de CV.")

text_company = '''
Experience the AI revolution with NexusAI, the leading company at the forefront of artificial intelligence innovation.\n 
Our team of brilliant minds is dedicated to pushing boundaries and transforming industries worldwide.
 With state-of-the-art algorithms and advanced machine learning techniques, we offer tailored solutions for businesses, researchers, and government agencies, empowering them to optimize operations, make breakthrough discoveries, and enhance public services.
 At NexusAI, we prioritize ethical AI practices, ensuring transparency, fairness, and accountability.
 Join us in shaping a future where imagination meets reality. Contact NexusAI today and unlock the true potential of artificial intelligence.
'''
st.text(text_company)

st.subheader('Our Team')

col1 , col2, col3 = st.columns([1.5,1.5,1.5])

images_path = '/home/tianlong55/Downloads/PyCharm_Projects/app2_portafolio/images_company'

with col1:
    for index, row in df[:4].iterrows():
        name_leader = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        print(name_leader)
        st.subheader(name_leader)
        st.text(row['role'])
        st.image(images_path+'/'+str(index+1)+'.png')
with col2:
    for index, row in df[4:8].iterrows():
        name_leader = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        st.subheader(name_leader)
        st.text(row['role'])
        st.image(images_path+'/'+str(index+1)+'.png')
with col3:
    for index, row in df[8:12].iterrows():
        name_leader = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        st.subheader(name_leader)
        st.text(row['role'])
        st.image(images_path+'/'+str(index+1)+'.png')
