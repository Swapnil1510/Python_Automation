import streamlit as st
import time

# Page config - "centered" layout
st.set_page_config(page_title="Smart-Test Orchestrator", page_icon="🤖", layout="centered")

# --- MAGIC HAPPENS HERE: Custom CSS for Background, Glow & Hover ---
st.markdown("""
<style>
    /* Footer gayab rakhenge, par Header/Menu wapas laa rahe hain taaki theme switch ho sake */
    footer {visibility: hidden;}

    /* 1. Subtle Dot Pattern Background (Works on both Light & Dark) */
    .stApp {
        background-image: radial-gradient(rgba(150, 150, 150, 0.2) 2px, transparent 2px);
        background-size: 35px 35px;
    }
    
    /* 2. Sleek Gradient & Glowing Title */
    .glow-title {
        text-align: center;
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4B4B, #FFA07A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #888;
        margin-bottom: 2rem;
    }

    /* 3. UNIVERSAL HOVER GLOW EFFECTS (Looks sexy on both modes) */
    
    /* Prompt Box Glow on Hover */
    div[data-baseweb="input"]:hover {
        box-shadow: 0 0 12px rgba(255, 75, 75, 0.3);
        transition: box-shadow 0.3s ease-in-out;
    }
    
    /* Primary Button Glow (Fetch Tasks) */
    button[kind="primary"]:hover {
        box-shadow: 0 6px 18px rgba(255, 75, 75, 0.4);
        transform: translateY(-2px); /* Slight 3D pop up */
        transition: all 0.3s ease-in-out;
    }
    
    /* Secondary Button Glow (Generate Scenarios) */
    button[kind="secondary"]:hover {
        box-shadow: 0 6px 15px rgba(130, 130, 130, 0.3);
        transform: translateY(-2px);
        transition: all 0.3s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)
# -----------------------------------------------------------

# Applying the custom HTML Title
st.markdown("<div class='glow-title'>🤖 Smart-Test Orchestrator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Automate your Task-to-Code workflow seamlessly.</div>", unsafe_allow_html=True)

# Sleek Prompt Input
category_input = st.text_input(
    "Prompt", 
    placeholder="✨ Enter Task Category (e.g., Artemis Flow, Login Scenarios)...", 
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# Action Buttons
col_left, col_mid, col_right = st.columns([1, 0.5, 1])

with col_left:
    fetch_btn = st.button("🔍 Fetch Tasks", type="primary", use_container_width=True)

with col_right:
    generate_btn = st.button("⚡ Generate Scenarios", use_container_width=True)

st.divider()

# UI Logic Simulation
if fetch_btn:
    if category_input:
        with st.spinner('Scraping data from browser Excel...'):
            time.sleep(2) 
            st.success("✨ Tasks fetched successfully!")
            st.info("Found 5 unassigned tasks and 3 assigned to you.")
    else:
        st.warning("Please enter a category first!")

if generate_btn:
    st.markdown("<h3 style='text-align: center;'>📝 Generated Code</h3>", unsafe_allow_html=True)
    
    feature_code = '''Feature: Login Flow
  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    Then I should see the dashboard'''
    
    python_code = '''def test_login(page):
    page.goto('/login')
    # Playwright code implementation...'''
    
    with st.expander("📂 View & Download .feature File"):
        st.code(feature_code, language="gherkin")
        st.download_button(label="⬇️ Download .feature", data=feature_code, file_name="scenario.feature")
        
    with st.expander("🐍 View & Download Python Code"):
        st.code(python_code, language="python")
        st.download_button(label="⬇️ Download .py", data=python_code, file_name="test_script.py")