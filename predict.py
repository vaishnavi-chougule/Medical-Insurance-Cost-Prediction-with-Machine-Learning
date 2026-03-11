# ==========================================
# 💊 Professional Insurance Dashboard
# ==========================================

import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="⚕️",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (REMOVE EXTRA SPACE + HIGHLIGHT)
# -------------------------------------------------
st.markdown("""
<style>

/* Remove top padding */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Title Gradient */
.main-title {
    background: linear-gradient(90deg, #2b5876, #4e4376);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

/* Highlight Section Header */
.section-header {
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Card Style */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Colorful Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-size: 16px;
    border-radius: 10px;
    padding: 8px 20px;
    border: none;
}

/* Prediction Result */
.result-box {
    background: linear-gradient(90deg, #11998e, #38ef7d);
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR INPUT
# -------------------------------------------------
st.sidebar.markdown("""
<div style="
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 15px;
">
🧾 Enter Patient Details
</div>
""", unsafe_allow_html=True)


age = st.sidebar.slider("Age", 18, 100, 30)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0)
children = st.sidebar.slider("Number of Children", 0, 5, 1)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
smoker = st.sidebar.selectbox("Smoker", ["Yes", "No"])
region = st.sidebar.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

# -------------------------------------------------
# TOP IMAGE (LOCAL IMAGE RECOMMENDED)
# -------------------------------------------------
st.image("healthcare_banner.jpg", width="stretch")

# -------------------------------------------------
# MAIN TITLE (NO EXTRA SPACE)
# -------------------------------------------------
st.markdown('<div class="main-title">💊Medical Insurance Cost Prediction💊</div>', unsafe_allow_html=True)

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
model = joblib.load("best_model.pkl")

# -------------------------------------------------
# TWO COLUMN LAYOUT
# -------------------------------------------------
col1, col2 = st.columns(2)

# ------------------ PATIENT SUMMARY ------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">📋 Patient Summary</div>', unsafe_allow_html=True)

    st.write(f"**Age:** {age}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Children:** {children}")
    st.write(f"**Sex:** {sex}")
    st.write(f"**Smoker:** {smoker}")
    st.write(f"**Region:** {region}")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ PREDICTION ------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🎯 Prediction</div>', unsafe_allow_html=True)

    if st.button("💰 Predict Insurance Cost"):

        input_data = pd.DataFrame({
            "age": [age],
            "sex": [sex.lower()],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker.lower()],
            "region": [region.lower()]
        })

        prediction = model.predict(input_data)

        st.markdown(
            f'<div class="result-box">₹ {prediction[0]:,.2f}</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)
