"""
Project: Personal Portfolio Web Application
Author: Shaikh Mohd Irfan Mohd Wakil (skirfanwakil)
Description: Minimalist, high-contrast monochrome portfolio built with Streamlit.
"""

import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM STYLING
# ==========================================
st.set_page_config(
    page_title="Shaikh Mohd Irfan | IT Portfolio",
    page_icon="◼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean minimalist monochrome cards & borders
st.markdown("""
    <style>
    .portfolio-card {
        background-color: #16181C;
        border: 1px solid #2D3139;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .skill-badge {
        display: inline-block;
        background-color: #262930;
        color: #F0F2F6;
        border: 1px solid #3E434D;
        padding: 5px 12px;
        border-radius: 15px;
        margin: 4px 4px 4px 0px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    a {
        color: #FFFFFF !important;
        text-decoration: underline !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR: IDENTITY & QUICK NAVIGATION
# ==========================================
with st.sidebar:
    st.title("◼️ skirfanwakil")
    st.caption("B.Sc. Information Technology (Final Year)")
    st.markdown("---")
    
    st.markdown("**📍 Location:** Byculla, Mumbai 400011")
    st.markdown("**📞 Phone:** +91 8657944080")
    st.markdown("**✉️ Email:** [skirfanwakil@gmail.com](mailto:skirfanwakil@gmail.com)")
    
    st.markdown("---")
    st.subheader("Quick Links")
    st.link_button("📂 Results & Certificates (Drive)", "https://drive.google.com/drive/folders/1nhu1qyxtzMBHBfKPGdiHfEbXrY_Nma7p", use_container_width=True)
    st.link_button("💻 Find Your Space (GitHub)", "https://github.com/skirfanwakil/find-your-space", use_container_width=True)
    st.link_button("🔗 UnityLink (GitHub)", "https://github.com/skirfanwakil/UnityLink", use_container_width=True)
    
    st.markdown("---")
    nav_section = st.radio(
        "Navigate Sections:",
        ["Overview & Skills", "Featured Projects", "Education & Experience", "Achievements & Contact"]
    )

# ==========================================
# 3. HERO HEADER (ALWAYS VISIBLE)
# ==========================================
st.title("SHAIKH MOHD IRFAN MOHD WAKIL")
st.markdown("##### B.Sc. Information Technology (Final Year) | Data Handling, System Design & Web Development")
st.markdown(
    "B.Sc. Information Technology (Final Year) student with practical exposure to computer applications, "
    "programming, databases, data handling, documentation, research, and project work. Experienced in using "
    "Microsoft Office, Google Workspace, programming languages, database tools, and digital platforms through "
    "academic projects, competitions, and practical activities."
)
st.markdown("---")

# ==========================================
# SECTION 1: OVERVIEW & SKILLS
# ==========================================
if nav_section == "Overview & Skills":
    # Academic Highlights as KPI Cards
    st.subheader("📊 Academic Highlights")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("B.Sc. IT CGPA", "8.77", "Up to 2nd Year")
    k2.metric("MHTCET (PCM) 2024", "86.22 %ile", "State Entrance")
    k3.metric("SSC Score", "83.20%", "Barkat English High School")
    k4.metric("HSC (PCMB + IT)", "62.67%", "Science Stream")
    
    st.markdown("---")
    st.subheader("🛠️ Technical & Productivity Stack")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### Programming Basics")
        prog_skills = ["Python", "Java", "C", "C++", "C#", "R", "JavaScript", "HTML", "CSS"]
        badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in prog_skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
    with c2:
        st.markdown("#### Database Systems")
        db_skills = ["SQL", "MySQL", "Microsoft Access", "Google Sheets DB"]
        badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in db_skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
    with c3:
        st.markdown("#### Tools & Documentation")
        tool_skills = ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Google Docs", "Google Sheets", "Google Forms", "Canva"]
        badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in tool_skills])
        st.markdown(badges_html, unsafe_allow_html=True)

# ==========================================
# SECTION 2: FEATURED PROJECTS
# ==========================================
elif nav_section == "Featured Projects":
    st.subheader("🚀 Featured Projects & Research")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="portfolio-card">
            <h4>1. Find Your Space | Product Planning & System Design</h4>
            <p>Designed the platform workflow, user interface, filtering logic, and Google Sheets database structure to deliver personalized place recommendations based on user preferences.</p>
            <a href="https://github.com/skirfanwakil/find-your-space" target="_blank">View Repository on GitHub ↗</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="portfolio-card">
            <h4>3. Personal Identity SEO Optimization</h4>
            <p>Built and optimized a personal digital identity, achieving first-page Google visibility through SEO, content optimization, and consistent cross-platform branding.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="portfolio-card">
            <h4>2. UnityLink | Product Planning & System Design</h4>
            <p>Conceptualized the platform, defined the UI workflow, resource matching logic, and database structure, and collaborated with the development team to build a functional prototype.</p>
            <a href="https://github.com/skirfanwakil/UnityLink" target="_blank">View Repository on GitHub ↗</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="portfolio-card">
            <h4>4. Digital Payment Awareness Program | Researcher</h4>
            <p>Conducted field research by designing surveys, collecting and analyzing primary data, and led a digital payment awareness initiative promoting secure transactions, fraud prevention, and safe digital payment practice.</p>
            <a href="https://drive.google.com/file/d/16SxlqVFWt0ELJ20l2qlh9JhVENWo0yL_/view?usp=drivesdk" target="_blank">View Research Report on Drive ↗</a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SECTION 3: EDUCATION & EXPERIENCE
# ==========================================
elif nav_section == "Education & Experience":
    col_edu, col_exp = st.columns(2)
    
    with col_edu:
        st.subheader("🎓 Education")
        st.markdown("""
        <div class="portfolio-card">
            <h4>B.Sc. Information Technology</h4>
            <p><b>University of Mumbai</b> | Final Year<br>
            <b>CGPA:</b> 8.77 <i>(up to 2nd year)</i></p>
        </div>
        <div class="portfolio-card">
            <h4>MHTCET (PCM) 2024</h4>
            <p><b>Percentile:</b> 86.22%ile</p>
        </div>
        <div class="portfolio-card">
            <h4>HSC — Science Stream (PCMB + IT)</h4>
            <p><b>Score:</b> 62.67%</p>
        </div>
        <div class="portfolio-card">
            <h4>SSC — Barkat English High School</h4>
            <p><b>Score:</b> 83.20%</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_exp:
        st.subheader("💼 Work Experience")
        st.markdown("""
        <div class="portfolio-card">
            <h4>Data Entry Operator</h4>
            <p>Responsible for accurately entering, updating, and maintaining structured information in computer systems and relational databases while ensuring data integrity.</p>
        </div>
        <div class="portfolio-card">
            <h4>Home Tutor</h4>
            <p>Teaches students by breaking down complex academic concepts, resolving individual doubts, and designing structured study routines to improve academic performance.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SECTION 4: ACHIEVEMENTS & CONTACT
# ==========================================
elif nav_section == "Achievements & Contact":
    st.subheader("🏆 Certifications & Competitions")
    
    achievements = [
        ("🥇 1st Position", "Inter College Model Presentation Competition"),
        ("🥈 2nd Position", "IT PPT Competition, Parvaaz 2023"),
        ("🥉 3rd Position", "Best Business Planning, Parvaaz 2025"),
        ("🥉 3rd Position", "Corporate Chanakya, Parvaaz 2025"),
        ("💻 Participant", "Datathon 2026 (Python, Pandas, Data Cleaning)"),
        ("🎯 Active Participant", "Multiple inter-college competitions, hackathons, and tech/non-tech events")
    ]
    
    for title, desc in achievements:
        st.markdown(f"- **{title}:** {desc}")
        
    st.markdown("---")
    st.subheader("📬 Get In Touch")
    
    c_info, c_form = st.columns([1, 1])
    with c_info:
        st.markdown("""
        **Name:** Shaikh Mohd Irfan Mohd Wakil  
        **Email:** skirfanwakil@gmail.com  
        **Phone:** +91 8657944080  
        **Location:** Byculla, Mumbai 400011, India  
        """)
        st.link_button("📁 Open Verified Certificates Folder", "https://drive.google.com/drive/folders/1nhu1qyxtzMBHBfKPGdiHfEbXrY_Nma7p")
        
    with c_form:
        with st.form("contact_form"):
            sender_name = st.text_input("Your Name")
            sender_email = st.text_input("Your Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                if sender_name and message:
                    st.success(f"Thank you, {sender_name}! Your message has been recorded for Shaikh Mohd Irfan.")
                else:
                    st.warning("Please enter your name and message before submitting.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888888; font-size: 0.9rem;'>"
    "© 2026 Shaikh Mohd Irfan Mohd Wakil (skirfanwakil) | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
