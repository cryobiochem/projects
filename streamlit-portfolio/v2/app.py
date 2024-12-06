import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Bruno M. Guerreiro, Ph.D.",
    page_icon="📊",
    layout="wide"
)

# Title and subtitle
st.title("Bruno M. Guerreiro, Ph.D.")
st.markdown("""
**Biochemistry Doctorate with over 20,000 hours of lab experience over a decade, turned big data engineer with cloud experience.  
Expert in business-driven data science, ML and AI.**
""")

# Social media logos placeholder
st.markdown("### Connect with me:")
cols = st.columns(6)
social_links = ["Social 1", "Social 2", "Social 3", "Social 4", "Social 5", "Social 6"]
for col, social in zip(cols, social_links):
    with col:
        st.image("https://via.placeholder.com/64", caption=social, use_column_width=True)

# Grid for projects
st.markdown("### My Projects:")
projects = [
    {"title": "Project 1", "link": "#"},
    {"title": "Project 2", "link": "#"},
    {"title": "Project 3", "link": "#"},
    {"title": "Project 4", "link": "#"},
    {"title": "Project 5", "link": "#"},
    {"title": "Project 6", "link": "#"}
]

project_cols = st.columns(3)
for idx, project in enumerate(projects):
    with project_cols[idx % 3]:
        st.markdown(f"### [{project['title']}]({project['link']})")
        st.image("https://via.placeholder.com/150", use_column_width=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Research Life", 
    "Certifications", 
    "Honors & Awards", 
    "Volunteering", 
    "Hobby Projects"
])

with tab1:
    st.write("Details about research experience go here.")
with tab2:
    st.write("List of certifications goes here.")
with tab3:
    st.write("Honors and awards details go here.")
with tab4:
    st.write("Volunteering experiences go here.")
with tab5:
    st.write("Details of hobby projects go here.")
