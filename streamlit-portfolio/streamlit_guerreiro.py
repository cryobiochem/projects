import streamlit as st 
from streamlit_timeline import timeline
import numpy as np
import pandas as pd 
import plotly.express as px  
import base64
from plotly.subplots import make_subplots
import plotly.graph_objects as go

### METADATA
st.set_page_config(
    page_title="Bruno M. Guerreiro | Portfolio",
    page_icon="🇵🇹",
    layout="wide",
)

### SIDEBAR
st.sidebar.markdown('<div style="text-align: left; margin-bottom: 12px"><a href="https://guerreiro.streamlit.app/">''<img src="https://i.imgur.com/t3cH48K.png" alt="Bruno M. Guerreiro" width="250">'
    '</a></div>', unsafe_allow_html=True)
st.sidebar.markdown("##### A personal portfolio project © 2024.")
st.sidebar.caption('Bruno M. Guerreiro is a Biochemistry Ph.D. with 7 years of experience in cryopreservation research. '
           'Bruno is an internationally renowned scientist, with **9** scientific publications, **10** conference participations, **7** awards and **3** fellowships. '
           'With a life sciences background, Bruno is also a self-growth enthusiast, having accumulated a total of **23 online certifications** in Data Science, Deep Learning, TensorFlow and complementary fields.')

# Create 4 columns for the logos with reduced spacing
gmail, scholar, github, linkedin, c5, c6, c7, c8 = st.sidebar.columns(8)

# Add clickable logos side by side for Gmail, Google Scholar, Github, and Linkedin with reduced spacing
gmail.markdown('<div style="text-align: left"><a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&to=guerreiro.bms@gmail.com&su=New%20job%20opportunity%20for%20Bruno%20M.%20Guerreiro" target="_blank">'
    '<img src="https://lh3.googleusercontent.com/0rpHlrX8IG77awQMuUZpQ0zGWT7HRYtpncsuRnFo6V3c8Lh2hPjXnEuhDDd-OsLz1vua4ld2rlUYFAaBYk-rZCODmi2eJlwUEVsZgg" alt="Gmail" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)
scholar.markdown('<div style="text-align: left"><a href="https://scholar.google.com/citations?user=nbyAZasAAAAJ&hl=en" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/2048px-Google_Scholar_logo.svg.png" alt="Google Scholar" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)
github.markdown('<div style="text-align: left"><a href="https://github.com/cryobiochem" target="_blank">'
    '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Github" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)
linkedin.markdown('<div style="text-align: left"><a href="https://www.linkedin.com/in/bmguerreiro/" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

st.sidebar.write('')

# Resume/CV download button
st.sidebar.markdown(f'<a href="https://pouch.jumpshare.com/download/vP2xyACw55AUc-mr9IdBV0s2oNr9koOjYp5Wig6F4O_dhDGJS_bpYbGOeQIzCkLCQSWYV-nC3-IH4CkRIJWpzA" download="Resume_CV.pdf"><button style="cursor: pointer; padding: 10px; border: none; border-radius: 5px;">Download Resume/CV</button></a>', unsafe_allow_html=True)
st.sidebar.caption("📌 Based in Setúbal/Lisbon")
st.sidebar.info("⚠️ For optimal website experience, use light theme & wide mode.")

### CONTENT
aboutme, certs, phd, ds, gd, tw, proj, media = st.tabs(["About me",
                                                         "Certifications",
                                                         "Ph.D.",
                                                         "Data Science",
                                                         "Graphic Design",
                                                         "Technical Writing",
                                                         "Projects",
                                                         "Media"])


with aboutme:
    ### TIMELINE
    with open('streamlit-portfolio/timeline.json', "r") as f:
        data = f.read()
    timeline(data, height=600)

with certs:
    c1_img, c1_text = st.columns([2,5])
    with c1_img:
        st.image("https://udemy-certificate.s3.amazonaws.com/image/UC-ZZHX1T1F.jpg?v=1544266446000", use_column_width="auto")

    with c1_text:
        st.markdown("### Data Science A-Z™: Hands-On Exercises | :blue[*SuperDataScience.com* (2018)]")
        st.markdown("The full walkthrough of how to be a data scientist. This course taught me how to clean and prepare data for analysis, perform basic data visualisations, model and curve-fit data & present findings to stakeholders. The **first capstone project** involved advanced data visualization in Tableau to derive insights from Credit Score and Tenure relationships, while performing churn modelling and Chi-Squared testing. The **second capstone project** involved advanced data mining in Microsoft Visual Studio (SSIS/SQL) to deal with ETL Error Handling on a Vehicle Service database containing more than 1 million entries.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://ude.my/UC-ZZHX1T1F)")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1: st.info("Data Mining")
        with col2: st.info("Data Visualization")
        with col3: st.info("Tableau")
        with col4: st.info("Gretl")
        with col5: st.info("SSIS")
        with col6: st.info("SQL")

    st.divider()

    c2_img, c2_text = st.columns([2, 5])

    with c2_img:
        st.image("https://i.imgur.com/wUPtNuw.png", use_column_width="auto")

    with c2_text:
        st.markdown("### Data Science Specialization | :blue[*John Hopkins University* (2020)]")
        st.markdown(
            "Covered the concepts and tools for an entire data science pipeline in R programming. Successful participants learn how to use the tools of the trade, think analytically about complex problems, manage large data sets, deploy statistical principles, create visualizations, build and evaluate machine learning algorithms, publish reproducible analyses, and develop data products. The **capstone projects** involved the measuring of atmospheric pollution for assessing societal health problems, and analysis of Fitbit movement activity monitoring to derive activity levels and patterns.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3543a8a5fd1219abc4e65ffa3856c3a2)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("R programming")
        with col2: st.info("Regression Analysis")
        with col3: st.info("Machine Learning")
        with col4: st.info("Github")

    st.divider()

    c3_img, c3_text = st.columns([2, 5])

    with c3_img:
        st.image("https://i.imgur.com/SNs3nPL.png", use_column_width="auto")
    with c3_text:
        st.markdown("### Deep Learning Specialization | :blue[*deeplearning.ai* (2020)]")
        st.markdown("In this Specialization, I've built neural network architectures such as Convolutional Neural Networks, Recurrent Neural Networks, LSTMs, Transformers, and learned how to make them better with strategies such as Dropout, BatchNorm, and Xavier/He initialization. You mastered these theoretical concepts, learned their industry applications using Python and TensorFlow. As **capstone project**, I tackled real-world cases such as speech recognition, music synthesis, chatbots, machine translation, natural language processing, and more.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/347c89a8fab8b4ddeb55f29674c00d83)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("CNNs")
        with col4: st.info("Computer Vision")
        with col5: st.info("NLP")

    st.divider()

    c4_img, c4_text = st.columns([2, 5])
    with c4_img:
        st.image("https://i.imgur.com/XKb0yGo.png", use_column_width="auto")
    with c4_text:
        st.markdown("### TensorFlow Developer | :blue[*deeplearning.ai* (2020)]")
        st.markdown("Following the Deep Learning specialization, I enrolled in a Professional Certificate program to learn how to build and train neural networks using TensorFlow, how to improve network performance using convolutions when trained to identify real-world images, correcting for overfitting using augmentation and dropout, how to teach machines to understand, analyze, and respond to human speech with natural language processing systems. The **capstone projects** involved Customer Sentiment analysis using NLP, and prediction analysis in time-series.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3e4c0da4f54954f5cca49e43f5433e49)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("RNNs")
        with col4: st.info("GRUs")
        with col5: st.info("LSTMs")

    st.divider()

    c5_img, c5_text = st.columns([2, 5])
    with c5_img:
        st.image("https://i.imgur.com/qpbfMVJ.png", use_column_width="auto")
    with c5_text:
        st.markdown("### Responsive Web Design | :blue[*freeCodeCamp* (2020)]")
        st.markdown("As a 300 hour investment lecture, I learned the fundamentals of building websites that work seamlessly across various devices. Several projects were created to show expertise over HTML and CSS programming languages, applied visual design, applied accessibility, web design presentation principles and the creative ways CSS (flexboxes, grids) can be used to enhance user experience.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://www.freecodecamp.org/certification/brunoguerreiro/responsive-web-design)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Web design")
        with col2: st.info("HTML")
        with col3: st.info("CSS")
        with col4: st.info("Front-end")

    st.divider()

    c6_img, c6_text = st.columns([2, 5])
    with c6_img:
        st.image("https://i.imgur.com/MIu8dX4.png", use_column_width="auto")
    with c6_text:
        st.markdown("### Fundamentals of Digital Marketing | :blue[*Google* (2020)]")
        st.markdown("This Interactive Advertising Bureau-accredited course contained 26 modules created by Google trainers, packed full of practical exercises and real-world examples to help you turn knowledge into action in the field of digital marketing. I learned the concepts of creating an online business, building a strong presence that urges call-to-action, how to optimize search ads, geodemographic personalization of products, connect with customers through various forms of marketing (e-mail, video, paid search, local search), optimize website content and perform decision-making analytics. **This course allowed me to better understand how to present web content online to captivate audiences.**")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://drive.google.com/file/d/1La55rHhtuHFwiEpr3i1o3G1yu9XYgA-I/view?usp=sharing)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Marketing")
        with col2: st.info("Web design")
        with col3: st.info("e-Commerce")
        with col4: st.info("SEO")
        with col5: st.info("ROI")




with phd:
    st.header("My Ph.D. Journey")
    st.caption("I have a strong background in life sciences and scientific research, having accumulated 10 years of constant critical thinking and problem-solving capabilities, and almost 7 years of theoretical and applied research focus."
               " My 4-year Ph.D. journey in particular has equipped me with a core skillset of adaptability, efficiency, productivity and being able to get out of a rut. Producing new knowledge in a scientific field"
               " is often a arduous path and requires patience, determination and ambition. Backing up, defending and presenting our ideas is also a part of the research life, such that I have honed"
               "illustration, data visualization, data analysis and public speaking skills that complement my seek for knowledge with the ability to share that knowledge to various audiences.")

    with st.container(border=True):
        st.markdown("Skills demonstrated in this section:")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Critical Thinking")
        with col2: st.info("Problem Solving")
        with col3: st.info("Public Speaking")
        with col4: st.info("Technical Writing")
        with col5: st.info("Data Presentation")

    st.write("")

    st.image("https://i.imgur.com/H26Nnem.png")

    st.write("")
    st.write("")
    st.subheader("Cryopreservation fundamentals + my approach")
    with st.container(border=True):
        st.image("https://i.imgur.com/fW46l27.png")

    st.write("")
    st.write("")
    st.subheader("The organ transplant crisis")
    with st.container(border=True):
        st.image("https://i.imgur.com/5f6BDf9.png")

    st.write("")
    st.write("")
    st.subheader("Lab work methodology")
    with st.container(border=True):
        st.image("https://i.imgur.com/SNt2e6m.jpg")

    st.write("")
    st.write("")
    st.subheader("Some of my contributions (+ visuals)")
    with st.container(border=True):
        st.image("https://i.imgur.com/N74iMeP.jpg")
    


st.write('---')
st.markdown('<div style="text-align: right;"><sub>Bruno M. Guerreiro © 2024</sub></div>', unsafe_allow_html=True)
