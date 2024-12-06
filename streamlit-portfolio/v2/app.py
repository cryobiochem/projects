import streamlit as st 

### METADATA
st.set_page_config(
    page_title="Bruno M. Guerreiro, Ph.D.",
    page_icon="🇵🇹",
    layout="wide",
)

### SIDEBAR
st.sidebar.markdown('<div style="text-align: left; margin-bottom: 12px"><a href="https://guerreiro.streamlit.app/">''<img src="https://i.imgur.com/t3cH48K.png" alt="Bruno M. Guerreiro" width="250">'
    '</a></div>', unsafe_allow_html=True)
st.sidebar.markdown("##### A personal portfolio project © 2024.")
st.sidebar.caption("I am a Biochemistry Ph.D. with 7 years of experience in cryopreservation. The constant problem-solving had me teach myself Python, Data Science and ML to solve my research problems. "
                    "These tools granted me 8 research papers, 7 awards and 3 fellowships, including a stay at the prestigious UC-Berkeley (USA). "
                    "I'm a fast learner with a passion for computer vision algorithms & interactive web models. In my free time, I attempt Kaggle datasets & teach myself the piano.")
    
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
st.sidebar.markdown(f'<a href="https://pouch.jumpshare.com/download/vP2xyACw55AUc-mr9IdBV0s2oNr9koOjYp5Wig6F4O_dhDGJS_bpYbGOeQIzCkLCQSWYV-nC3-IH4CkRIJWpzA" download="Resume_CV.pdf"><button style="cursor: pointer; padding: 10px; border: none; border-radius: 5px;">Download CV</button></a>', unsafe_allow_html=True)
st.sidebar.caption("📌 Based in Setúbal/Lisbon")

### CONTENT
portfolio, certs, awards, sci, vol = st.tabs(["Portfolio",
                                             "Certifications",
                                             "Honors & Awards",
                                             "Scientific Research",
                                             "Volunteering"])


with portfolio:
    st.markdown("""
        <style>
        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .portfolio-item {
            position: relative;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .portfolio-item:hover {
            transform: scale(1.05);
        }
        .portfolio-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .portfolio-title {
            position: absolute;
            bottom: 0;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            width: 100%;
            text-align: center;
            padding: 10px;
        }
        .portfolio-hover {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .portfolio-item:hover .portfolio-hover {
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)

    projects = [
        {"title": "Project 1", "image": "https://via.placeholder.com/400", "description": "Description for Project 1", "link": "https://example.com/project1"},
        {"title": "Project 2", "image": "https://via.placeholder.com/400", "description": "Description for Project 2", "link": "https://example.com/project2"},
        {"title": "Project 3", "image": "https://via.placeholder.com/400", "description": "Description for Project 3", "link": "https://example.com/project3"},
        {"title": "Project 4", "image": "https://via.placeholder.com/400", "description": "Description for Project 4", "link": "https://example.com/project4"},
    ]

    # Render projects grid
    st.markdown('<div class="portfolio-grid">', unsafe_allow_html=True)
    for project in projects:
        st.markdown(f"""
            <div class="portfolio-item" onclick="window.open('{project['link']}', '_blank')">
                <img src="{project['image']}" alt="{project['title']}">
                <div class="portfolio-title">{project['title']}</div>
                <div class="portfolio-hover">{project['description']}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with certs:
    st.write("---")
    
with awards:
    st.write("---")

with sci:
    st.write("---")

with vol:
    st.write("---")
