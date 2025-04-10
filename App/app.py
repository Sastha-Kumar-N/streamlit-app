import streamlit as st 
import json

# Set up the main layout and theme
st.set_page_config(page_title="BGDB-AI-ML Student Platform", layout="wide")

# Custom CSS for Sidebar Styling
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #030349;
        padding-top: 20px;
        padding-left: 10px;
        padding-right: 10px;
    }
    [data-testid="stSidebar"] h1 {
        color: #ffffff;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
        margin-top: 5px;
    }
    .stButton > button:hover {
        background-color: #E63E3E;
    }
    [data-baseweb="select"] {
        border-radius: 10px !important;
        background-color: #ffffff !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)


# Add logo to the top of the sidebar
with st.sidebar:
    st.image("drupal.png", width=125, caption="BGDB-AI-ML", use_container_width=False)

st.markdown("""
    <style>
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)








# Sidebar with topic navigation
st.sidebar.title("📚 Course Modules")
modules = {
    "Start": None,
    "Module 1: Basics": {"Introduction": None, " AI in Biology": None, "AI in Genomics": None},
    "Module 2: Advanced": {"Advanced Topic 1": None, "Advanced Topic 2": None},
    "Module 3: Applications": {"Case Study 1": None, "Case Study 2": None},
}

selected_module = st.sidebar.selectbox("Select a Module", list(modules.keys()))
selected_topic = None
if modules[selected_module]:
    selected_topic = st.sidebar.selectbox("Select a Topic", list(modules[selected_module].keys()))









# Navbar with Logo
st.markdown("""
    <style>
        .navbar {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            padding: 15px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        # .navbar img {
        #     # height: 50px;
        #     border-radius: 50%;
        }
        .navbar a {
            text-decoration: none;
            color: #ffffff;
            font-size: 18px;
            font-weight: 600;
            padding: 12px 20px;
            transition: all 0.3s ease-in-out;
            border-radius: 8px;
        }
        .navbar a:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        .heading {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-top: 30px;
            color: #1e3c72;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        }
        @media screen and (max-width: 768px) {
            .navbar {
                flex-direction: column;
                text-align: center;
            }
            .navbar div {
                margin-top: 10px;
            }
        }
    </style>

    <div class="navbar">
        <div>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#courses">Courses</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    
    <h1 class="heading">📖 Welcome to BGDB-AI-ML Student Platform</h1>
""", unsafe_allow_html=True)

# Load JSON content
with open("intro.json", "r", encoding="utf-8") as file:
    intro_content = json.load(file)

with open("aiinbio.json", "r", encoding="utf-8") as file:
    content = json.load(file)

with open("genomics.json", "r", encoding="utf-8") as file:
    aigenomics_content = json.load(file)


def add_download_button(note_path, label="📥 Download Notes (PDF)"):
    try:
        with open(note_path, "rb") as pdf_file:
            btn = st.download_button(
                label=label,
                data=pdf_file,
                file_name=note_path.split("/")[-1],
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning(f"⚠️ Notes not found: {note_path}")

# Main content area
if not selected_topic:
    st.image("p.png", width=720, caption="Welcome to the AI-ML Student Platform")

    st.markdown("""
    ## Introduction to the AI-ML Student Platform

    The **AI-ML Student Platform** is an interactive learning tool designed to help students explore the exciting world of artificial intelligence (AI) and machine learning (ML). Whether you're a beginner eager to grasp the basics or an advanced learner diving into complex concepts like neural networks, this platform provides a structured and engaging way to build your knowledge.

    ### How to Use It:
    To get started:
    1. Look at the **sidebar on the left**.
    2. Choose a **module** and a **specific topic** that interests you.
    3. Once selected, the **main content area** will update with detailed explanations, examples, and possibly interactive features to enhance your learning.
    """)

    st.image("https://via.placeholder.com/200x200", caption="Click a topic to start learning")

else:
    st.title(f"📌 {selected_topic}")
    
    if selected_module == "Module 1: Basics":
        if selected_topic == "Introduction":
            st.video("https://www.youtube.com/embed/YOUR_INTRO_VIDEO")  # Replace with actual video URL
            st.write("## Key Concepts of Python Introduction")
            st.image("https://your-image-url.com", caption="Introduction Illustration")
            st.write(intro_content["introduction"])
            add_download_button("resources/intro_notes.pdf")


        elif selected_topic == " AI in Biology":
            st.video("https://www.youtube.com/embed/YOUR_CONCEPT1_VIDEO")
            st.write("## Key Concepts of  AI in Biology")
            st.image("https://your-image-url.com", caption=" AI in Biology Illustration")
            st.write(content["AI_in_Biology"]["description"])
            add_download_button("resources/intro_notes.pdf")

        elif selected_topic == "AI in Genomics":
            st.video(aigenomics_content["AI_in_Genomics"]["video"])
            st.write(aigenomics_content["AI_in_Genomics"]["title"])
            st.image(aigenomics_content["AI_in_Genomics"]["image"]["url"], 
                    caption=aigenomics_content["AI_in_Genomics"]["image"]["caption"])
            st.write(aigenomics_content["AI_in_Genomics"]["description"])
    
    elif selected_module == "Module 2: Advanced":
        if selected_topic == "Advanced Topic 1":
            st.video("https://www.youtube.com/embed/YOUR_ADVANCED1_VIDEO")
            st.write("## Key Concepts of Advanced Topic 1")
            st.image("https://your-image-url.com", caption="Advanced Topic 1 Illustration")
            st.write("Detailed explanation about Advanced Topic 1.")
        
        elif selected_topic == "Advanced Topic 2":
            st.video("https://www.youtube.com/embed/YOUR_ADVANCED2_VIDEO")
            st.write("## Key Concepts of Advanced Topic 2")
            st.image("https://your-image-url.com", caption="Advanced Topic 2 Illustration")
            st.write("Detailed explanation about Advanced Topic 2.")
    
    elif selected_module == "Module 3: Applications":
        if selected_topic == "Case Study 1":
            st.video("https://www.youtube.com/embed/YOUR_CASESTUDY1_VIDEO")
            st.write("## Key Concepts of Case Study 1")
            st.image("https://your-image-url.com", caption="Case Study 1 Illustration")
            st.write("Detailed explanation about Case Study 1.")
        
        elif selected_topic == "Case Study 2":
            st.video("https://www.youtube.com/embed/YOUR_CASESTUDY2_VIDEO")
            st.write("## Key Concepts of Case Study 2")
            st.image("https://your-image-url.com", caption="Case Study 2 Illustration")
            st.write("Detailed explanation about Case Study 2.")
            st.write("This is a test program to run to see the application status.")
